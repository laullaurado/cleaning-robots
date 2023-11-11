from CleaningRobots import *  # type: ignore
import seaborn  # type: ignore
import matplotlib.pyplot as plt


def run(width, height, numAgents, dirtyCells, maxTime):
    """
    Runs the simulation with the parameters provided.
    """
    model = CleaningModel(width, height, numAgents, dirtyCells)

    stepCounter = 0
    # Run the model until all the cells are clean or the maximum time is reached
    while stepCounter < maxTime and model.garbage > 0:
        model.step()
        stepCounter += 1

    print(f"Número de agentes: {numAgents}")

    if (model.garbage == 0):
        print(
            f"Tiempo necesario hasta que todas las celdas estén limpias: {stepCounter} pasos")
    else:
        print(
            f"Se ha llegado al tiempo máximo de ejecución: {stepCounter} pasos")

    print(
        f"Porcentaje de celdas limpias: {30 - model.garbage * 30 / (width * height)}%")

    print(
        f"Número de movimientos realizados por los agentes: {model.movements} \n")

    # Plot the quantity of garbage over time
    garbage = model.datacollector.get_model_vars_dataframe()
    g = seaborn.lineplot(data=garbage)
    g.set(title="Quantity of garbage over time",
          xlabel="Steps",
          ylabel="Garbage",)
    plt.show()


print("***MISMO TAMAÑO, PORCENTAJE DE CELDAS SUCIAS Y TIEMPO MÁXIMO***")

print("***Simulación 1***")
print()
run(50, 50, 5, 0.3, 30)
print()

print("***Simulación 2***")
print()
run(50, 50, 10, 0.3, 30)
print()

print("***Simulación 3***")
print()
run(50, 50, 50, 0.3, 30)
print()

print("***Simulación 4***")
print()
run(50, 50, 30, 0.3, 30)
print()

print("***Simulación 5***")
print()
run(50, 50, 300, 0.3, 30)
print()

print("***Simulación 6***")
print()
run(50, 50, 2000, 0.3, 30)
print()
