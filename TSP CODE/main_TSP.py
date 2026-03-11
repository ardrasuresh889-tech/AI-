import TSPGeneticAlgorithm as TSPGA
import Chromosome as Ch
import numpy as np
import matplotlib.pyplot as plt
import time


numbers_of_generations = 100
population_size = 100
mutation_rate = 0.2
dataset = Ch.dataset
start_time = time.time()


def genetic_algorithm(no_of_generations, population_size, mutation_rate, data_list):
    new_gen = TSPGA.initialization(data_list, population_size)

    cost_plot = []
    print("Generations       cost")
    for iteration in range(0, no_of_generations):
        new_gen = TSPGA.create_new_generation(new_gen, mutation_rate)

        print(str(iteration) + "             " + str(new_gen[0].cost))
        cost_plot.append(TSPGA.find_best(new_gen).cost)


    return new_gen, cost_plot
def draw_cost_generation(y_list):
    x_list = np.arange(1, len(y_list)+1)  # create a numpy list from 1 to the numbers of generations

    plt.plot(x_list, y_list)

    plt.title("Route Cost through Generations")
    plt.xlabel("Generations")
    plt.ylabel("Cost")

    plt.show()



def draw_path(solution):
    x_list = []
    y_list = []

    for m in range(0, len(solution.chromosome)):
        x_list.append(solution.chromosome[m].x)
        y_list.append(solution.chromosome[m].y)

    fig, ax = plt.subplots()
    plt.scatter(x_list, y_list)

    ax.plot(x_list, y_list, '--', lw=1, color='red', ms=10)
    ax.set_xlim(0,100)
    ax.set_ylim(0,100)

    plt.show()


last_generation, y_axis = genetic_algorithm(
    no_of_generations=numbers_of_generations, population_size=population_size, mutation_rate=mutation_rate, data_list=dataset
)

best_solution = TSPGA.find_best(last_generation)
end_time = time.time()
print('The Best solution path is:'+ str(best_solution.chr_representation))
print('Best cost:'+ str(best_solution.cost))
print('elapsed time was{0:.1f}seconds' .format(end_time-start_time))
draw_cost_generation(y_axis)
draw_path(best_solution)

