import numpy as np
from classes.algorithms.AStar import AStar
from classes.algorithms.Greedy import Greedy
from classes.blocos_deslizantes.BlocosDeslizantes import BlocosDeslizantes
from classes.general_search.GeneralSearch import GeneralSearch

test_easy = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [10, 11, 12, 13, 14, 15, 16, 17, 18],
             [19, 20, 21, 22, 23, 24, 25, 26, 27],
             [28, 29, 30, 31, 32, 33, 34, 35, 36],
             [37, 38, 39, 40, 41, 42, 43, 44, 45],
             [46, 47, 48, 49, 50, 51, 52, 53, 54],
             [55, 56, 57, 58, 59, 0, 61, 62, 63],
             [64, 65, 66, 67, 68, 60, 71, 79, 72],
             [73, 74, 75, 76, 77, 69, 78, 70, 80]]
empty_easy = [6, 5]

test_other = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
             [10, 11, 0, 12, 14, 15, 16, 17, 18],
             [19, 20, 22, 13, 23, 24, 25, 26, 27],
             [28, 29, 21, 30, 31, 32, 34, 35, 36],
             [37, 38, 39, 40, 41, 33, 43, 44, 45],
             [46, 47, 48, 49, 50, 42, 52, 53, 54],
             [55, 56, 57, 58, 59, 51, 60, 61, 62],
             [64, 65, 66, 67, 68, 69, 70, 71, 63],
             [73, 74, 75, 76, 77, 78, 79, 80, 72]]
empty_other = [1, 2]

test_not_that_easy = [[10, 44, 27, 28, 61, 8, 14, 17, 0],
             [22, 6, 16, 43, 48, 51, 36, 2, 68],
             [24, 38, 37, 45, 18, 41, 70, 34, 46],
             [55, 4, 1, 30, 50, 58, 32, 12, 9],
             [3, 23, 60, 56, 40, 15, 72, 54, 20],
             [7, 25, 11, 47, 5, 74, 29, 35, 26],
             [52, 57, 73, 65, 49, 42, 77, 78, 21],
             [31, 67, 13, 53, 62, 66, 80, 33, 69],
             [39, 75, 64, 19, 59, 76, 63, 79, 71]]
empty_not_that_easy = [0, 8]

# if 'str' is 'sh', than initial state is obtained by shuffling
# if it is 'iv', it is obtained by passing initial values
strategy = AStar()
problem = BlocosDeslizantes(9, 35, str='iv', values=test_other, empty_var=empty_other)
gs = GeneralSearch(problem, strategy)
solution = gs.search()

print('Solution:')
for node in solution:
    node.get_state().print_state()
print('Cost: ', solution[len(solution)-1].get_cost())
print('Quantidade de passos: ', len(solution)-1)

input()
