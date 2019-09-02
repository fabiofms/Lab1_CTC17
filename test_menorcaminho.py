from classes.general_search.GeneralSearch import GeneralSearch
from classes.algorithms.Greedy import Greedy
from classes.algorithms.AStar import AStar
from classes.menor_caminho.MenorCaminho import MenorCaminho

# options to include in problem:
#   - MenorCaminho('Alice Springs', 'Yulara')
#   - Romenia('Arad')
strategy = Greedy()
problem = MenorCaminho('Alice Springs', 'Yulara')
gs = GeneralSearch(problem, strategy)
solution = gs.search()

print('Solution for Greedy:')
for node in solution:
    print(node.get_state(), end = ' ')
print()
print('Cost: ', solution[len(solution)-1].get_cost())
print('Quantidade de passos: ', len(solution)-1)

strategy = AStar()
problem = MenorCaminho('Alice Springs', 'Yulara')
gs = GeneralSearch(problem, strategy)
solution = gs.search()

print()
print('Solution for A Star:')
for node in solution:
    print(node.get_state(), end = ' ')
print()
print('Cost: ', solution[len(solution)-1].get_cost())
print('Quantidade de passos: ', len(solution)-1)

input()
