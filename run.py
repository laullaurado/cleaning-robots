from CleaningRobots import *  # type: ignore
from mesa.visualization.modules import CanvasGrid  # type: ignore
from mesa.visualization.ModularVisualization import ModularServer  # type: ignore


def agent_portrayal(agent):

    if isinstance(agent, RobotAgent):
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "blue",
                     "r": 0.5}  # Radio del círculo

    elif isinstance(agent, DirtyCell):
        if agent.isDirty == True:
            portrayal = {"Shape": "rect",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "grey",
                         "h": 1,
                         "w": 1}  # Radio del círculo
        else:
            portrayal = {"Shape": "rect",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "white",
                         "h": 1,
                         "w": 1}  # Radio del círculo

    return portrayal


width = 20
height = 20
num_agents = 10
ticks = 50
initial_gray_percentage = 0.2  # Porcentaje de celdas a colorear de gris al inicio

model = CleaningModel(width, height, num_agents, initial_gray_percentage)

grid = CanvasGrid(agent_portrayal, width, height, 500, 500)

# Configura el servidor de visualización
server = ModularServer(CleaningModel, [grid], "My Model", {
                       "width": width, "height": height, "numAgents": num_agents, "dirtyCells": initial_gray_percentage})
server.port = 8521  # Puedes ajustar el puerto según tus necesidades

# Ejecuta el servidor de visualización y la simulación
server.launch()
for i in range(ticks):
    model.step()
