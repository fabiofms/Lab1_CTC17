from classes.general_search.Tree import Tree


# class 'GeneralSearch': simulates the data structure tree
class GeneralSearch:
    def __init__(self, problem, strategy):
        self.problem = problem
        self.strategy = strategy
        # initialize the search tree using the initial state of problem
        self.tree = Tree(self.problem.get_initial_state())

    def search(self):
        # ----------------------------------------------------- #
        # i=1                                                   #
        # print("goal state: ", self.problem.get_goal_state())  #
        # ----------------------------------------------------- #
        while True:
            # candidates must be tree nodes, because of the cost
            # ----------------- #
            # print("i = ", i)  #
            # i+=1              #
            # ----------------- #

            candidates = self.tree.get_candidates()

            # -----------------------------------------------------------------------------------------------------#
            # to_print = 'Candidates: '                                                                            #
            # for candidate in candidates:                                                                         #
            #    to_print = to_print + str(candidate.get_state()) + ': ' + str(candidate.get_cost()
            #                                                           + self.problem.heuristic(candidate)) + '\t'#
            # print(to_print)                                                                                      #
            # -----------------------------------------------------------------------------------------------------#

            if len(candidates) == 0:
                return None

            # chosen index is for the candidates list
            chosen_index = self.strategy.choose(candidates, self.problem)

            # ---------------------------------------------------------------------------------------------------------#
            # print("No que sera expandido: ", candidates[chosen_index].get_state(), 'Valor: ',
            #                                                              candidates[chosen_index].get_cost(), "\n")  #
            # ---------------------------------------------------------------------------------------------------------#

            if self.problem.is_goal_state(candidates[chosen_index]):
                return self.tree.get_solution(candidates[chosen_index])
            else:
                # Expanding nodes are tuples (state, cost)
                expanding_nodes = self.problem.expand(candidates[chosen_index])
                self.tree.add(expanding_nodes, chosen_index)
