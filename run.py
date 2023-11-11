from CleaningRobots import *  # type: ignore
from mesa.visualization.modules import CanvasGrid  # type: ignore
from mesa.visualization.ModularVisualization import ModularServer  # type: ignore


def agentPortrayal(agent):
    """
    Defines the portrayal of the agents in the visualization.
    """

    # Blue circle for RobotAgent agents
    if isinstance(agent, RobotAgent):
        portrayal = {"Shape": "circle",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "blue",
                     "r": 0.5  # Radio del círculo
                     }

    elif isinstance(agent, DirtyCell):
        # Gray rectangle for DirtyCell agents if they are dirty
        if agent.isDirty == True:
            portrayal = {"Shape": "rect",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "grey",
                         "h": 1,
                         "w": 1
                         }

        # White rectangle for DirtyCell agents if they are not dirty
        else:
            portrayal = {"Shape": "rect",
                         "Filled": "true",
                         "Layer": 0,
                         "Color": "white",
                         "h": 1,
                         "w": 1
                         }

    return portrayal


width = 20
height = 20
numAgents = 10
dirtyCellsPercentage = 0.2

model = CleaningModel(width, height, numAgents, dirtyCellsPercentage)

grid = CanvasGrid(agentPortrayal, width, height, 500, 500)

# Configure the server, providing the model and the port where the server will listen
server = ModularServer(CleaningModel, [grid], "My Model", {
                       "width": width, "height": height, "numAgents": numAgents, "dirtyCells": dirtyCellsPercentage})
server.port = 8521  # Puedes ajustar el puerto según tus necesidades

# Execute the server
server.launch()
model.step()
