# class 'NodeTree': simulates a node in data structured as a tree
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