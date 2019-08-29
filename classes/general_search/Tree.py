from classes.NodeTree import NodeTree


# class 'Tree': simulates the data structure tree
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
        # expanding nodes are tuples (state, cost)
        father = self.queue[father_index]
        for exp_node in expanding_nodes:
            node = NodeTree(father, father.get_depth() + 1, father.get_cost() + exp_node[1], exp_node[0])
            self.queueing_fn(node)
            father.add_child(node)
        self.queue.pop(father_index)