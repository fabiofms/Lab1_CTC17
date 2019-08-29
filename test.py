from classes.GeneralSearch import GeneralSearch
from classes.algorithms.Greedy import Greedy
from classes.menor_caminho.MenorCaminho import MenorCaminho

# MenorCaminho('Alice Springs', 'Yulara')
# Romenia('Arad')

strategy = Greedy()
problem = MenorCaminho('Alice Springs', 'Yulara')
gs = GeneralSearch(problem, strategy)
solution = gs.search()
print('Solution:')
for node in solution:
    print(node.get_state())
print('Cost: ', solution[len(solution)-1].get_cost())
print('Quantidade de passos: ', len(solution)-1)
input()