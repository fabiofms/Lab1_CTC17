from classes.algorithms.AStar import AStar
from classes.blocos_deslizantes.BlocosDeslizantes import BlocosDeslizantes
from classes.GeneralSearch import GeneralSearch

strategy = AStar()
problem = BlocosDeslizantes(9, 30)
gs = GeneralSearch(problem, strategy)
solution = gs.search()
print('Solution:')
for node in solution:
    node.get_state().print_state()
print('Cost: ', solution[len(solution)-1].get_cost())
print('Quantidade de passos: ', len(solution)-1)