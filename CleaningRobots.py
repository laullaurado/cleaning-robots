from mesa import Agent, Model  # type: ignore
from mesa.space import SingleGrid  # type: ignore
from mesa.space import MultiGrid  # type: ignore
from mesa.time import SimultaneousActivation  # type: ignore
import mesa
import random


def get_garbage(model):
    return model.garbage


class RobotAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pos = (1, 1)

    def step(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for cellmate in cellmates:
            if type(cellmate) is DirtyCell:
                if cellmate.isDirty:
                    cellmate.isDirty = False
                    self.model.garbage -= 1
                    return

        possibleSteps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        newPosition = self.random.choice(possibleSteps)
        self.model.grid.move_agent(self, newPosition)
        self.model.movements += 1


class DirtyCell(Agent):

    def __init__(self, model, x, y):
        super().__init__("dirty", model)
        self.pos = (x, y)
        self.isDirty = True


class CleaningModel(Model):
    def __init__(self, width, height, numAgents, dirtyCells):
        self.num_agents = numAgents
        self.grid = MultiGrid(width, height, False)
        self.schedule = SimultaneousActivation(self)
        self.running = True  # Para la visualizacion usando navegador
        self.steps = 0
        self.garbage = 0
        self.movements = 0

        for i in range(self.num_agents):
            agent = RobotAgent(i, self)
            self.grid.place_agent(agent, agent.pos)
            self.schedule.add(agent)

        coloredCells = int(dirtyCells * width * height)
        self.garbage = coloredCells
        for _ in range(coloredCells):
            x = random.randrange(width)
            y = random.randrange(height)
            colored = DirtyCell(self, x, y)
            self.grid.place_agent(colored, (x, y))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Garbage over time": get_garbage})

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
