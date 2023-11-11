from mesa import Agent, Model  # type: ignore
from mesa.space import SingleGrid  # type: ignore
from mesa.space import MultiGrid  # type: ignore
from mesa.time import SimultaneousActivation  # type: ignore
import mesa
import random


def getGarbage(model):
    """
    Obtains the amount of garbage in the model provided.
    """
    return model.garbage


class RobotAgent(Agent):
    """
    Represents a robot agent that moves randomly through the grid and cleans the cells it passes through.
    """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.pos = (1, 1)  # Initial position

    def step(self):
        # Obtain all the agents contained in a cell
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for cellmate in cellmates:
            if isinstance(cellmate, DirtyCell):
                if cellmate.isDirty:
                    # Change isDirty variable if the RobotAgent agent is in the cell
                    cellmate.isDirty = False
                    self.model.garbage -= 1
                    return

        possibleSteps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        # Select a random cell from the list of cells to which it is possible to move
        newPosition = self.random.choice(possibleSteps)
        # Move agent to the new random position
        self.model.grid.move_agent(self, newPosition)
        self.model.movements += 1


class DirtyCell(Agent):
    """
    Represents a dirty cell that can be cleaned by the RobotAgent agent.
    """

    def __init__(self, model):
        super().__init__("dirty", model)
        self.isDirty = True


class CleaningModel(Model):
    """
    Represents the model of the cleaning robots.
    """

    def __init__(self, width, height, numAgents, dirtyCells):
        self.num_agents = numAgents
        self.grid = MultiGrid(width, height, False)
        self.schedule = SimultaneousActivation(self)
        self.running = True  # Para la visualizacion usando navegador
        self.steps = 0
        self.garbage = 0
        self.movements = 0

        # Create agents and add them to the grid and the scheduler
        for i in range(self.num_agents):
            agent = RobotAgent(i, self)
            self.grid.place_agent(agent, agent.pos)
            self.schedule.add(agent)

        # Create dirty cells and add them to the grid
        coloredCells = int(dirtyCells * width * height)
        self.garbage = coloredCells
        for _ in range(coloredCells):
            x = random.randrange(width)
            y = random.randrange(height)
            colored = DirtyCell(self)
            self.grid.place_agent(colored, (x, y))

        # Create data collector
        self.datacollector = mesa.DataCollector(
            model_reporters={"Quantity of garbage over time": getGarbage})

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
