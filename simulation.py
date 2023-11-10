from CleaningRobots import *  # type: ignore
import seaborn  # type: ignore
import matplotlib.pyplot as plt


def run(width, height, num_agents, dirty_cells, max_time):
    model = CleaningModel(width, height, num_agents, dirty_cells)

    stepCounter = 0
    while stepCounter < max_time and model.garbage > 0:
        model.step()
        stepCounter += 1

    print(f"Número de agentes: {num_agents}")

    if (model.garbage == 0):
        print(
            f"Tiempo necesario hasta que todas las celdas estén limpias: {stepCounter} pasos")
    else:
        print(
            f"Se ha llegado al tiempo máximo de ejecución: {stepCounter} pasos")

    print(
        f"Porcentaje de celdas limpias: {100 - model.garbage * 100 / (width * height)}%")

    print(
        f"Número de movimientos realizados por los agentes: {model.movements} \n")

    garbage = model.datacollector.get_model_vars_dataframe()
    g = seaborn.lineplot(data=garbage)
    g.set(title="Quantity of garbage over time",
          xlabel="Steps",
          ylabel="Garbage",)
    plt.show()


print("***MISMO TAMAÑO, PORCENTAJE DE CELDAS SUCIAS Y TIEMPO MÁXIMO***")

print("***Simulación 1***")
print()
run(50, 50, 5, .2, 30)
print()

print("***Simulación 2***")
print()
run(50, 50, 10, .2, 30)
print()

print("***Simulación 3***")
print()
run(50, 50, 50, .2, 30)
print()

print("***Simulación 4***")
print()
run(50, 50, 100, .2, 30)
print()

print("***Simulación 5***")
print()
run(50, 50, 1000, .2, 30)
print()

print("***Simulación 6***")
print()
run(50, 50, 2000, .2, 30)
print()
