
class NodeTree:
    def __init__(self, father, depth, cost, state):
        self.father = father
        self.depth = depth
        self.cost = cost
        self.children = []
        self.state = state

    def get_father(self):
        return self.father

    def get_depth(self):
        return self.depth

    def get_cost(self):
        return self.cost

    def get_children(self):
        return self.children

    def get_state(self):
        return self.state

    def add_child(self, child):
        self.children.append(child)


class Tree:
    def __init__(self, initial_state):
        self.root = NodeTree(None, 0, 0, initial_state)
        self.queue = []
        self.queueing_fn(self.root)

    def queueing_fn(self, node):
        self.queue.append(node)

    def get_candidates(self):
        return self.queue

    def get_solution(self, chosen_candidate):
        solution = [chosen_candidate]
        node = chosen_candidate.get_father()
        while node is not None:
            solution.append(node)
            node = node.get_father()
        solution.reverse()
        return solution

    def add(self, expanding_nodes, father_index):
        # Expanding nodes are tuples (state, cost)
        father = self.queue[father_index]
        for exp_node in expanding_nodes:
            node = NodeTree(father, father.get_depth() + 1,
                                      father.get_cost() + exp_node[1], exp_node[0])
            self.queueing_fn(node)
            father.add_child(node)

        self.queue.pop(father_index)


class GeneralSearch:
    def __init__(self, problem, strategy):
        self.problem = problem
        self.strategy = strategy
        # initialize the search tree using the initial state of problem
        self.tree = Tree(self.problem.get_initial_state())

    def search(self):
        #######################################################
        #i=1                                                   #
        #print("goal state: ", self.problem.get_goal_state())  #
        #######################################################
        while True:
            # Candidates must be tree nodes, because of the cost
            ##################
            #print("i = ", i) #
            #i+=1             #
            ##################
            candidates = self.tree.get_candidates()
            ###################################################################################################################################
            #to_print = 'Candidates: '                                                                                                         #
            #for candidate in candidates:                                                                                                      #
            #    to_print = to_print + str(candidate.get_state()) + ': ' + str(candidate.get_cost() + self.problem.heuristic(candidate)) + '\t'#
            #print(to_print)                                                                                                                   #
            ###################################################################################################################################
            if len(candidates) == 0:
                return None
            # Chosen index is for the candidates list
            chosen_index = self.strategy.choose(candidates, self.problem)
            ###############################################################################################################################
            #print("No que sera expandido: ", candidates[chosen_index].get_state(), 'Valor: ', candidates[chosen_index].get_cost(), "\n")  #
            ###############################################################################################################################
            if self.problem.is_goal_state(candidates[chosen_index]):
                return self.tree.get_solution(candidates[chosen_index])
            else:
                # Expanding nodes are tuples (state, cost)
                expanding_nodes = self.problem.expand(candidates[chosen_index])
                self.tree.add(expanding_nodes, chosen_index)
