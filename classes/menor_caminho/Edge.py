class Edge:
    def __init__(self, node_a, node_b, distance):
        self.nodes = [node_a, node_b]
        self.distance = distance

    def get_nodes(self):
        return self.nodes

    def get_distance(self):
        return self.distance

    def get_destiny_id(self):
        return self.nodes[1].get_id()

    def get_origin_node(self):
        return self.nodes[0]

    def get_destiny_node(self):
        return self.nodes[1]
