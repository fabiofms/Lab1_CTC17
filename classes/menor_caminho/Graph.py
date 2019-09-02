from classes.menor_caminho.Node import Node
from classes.menor_caminho.Edge import Edge
import math


class Graph:
    def __init__(self, file_path):
        self.file = open(file_path, "r")
        self.nodes = []
        self.nodes_dictionary = {}
        self.generate_graph()

    def generate_graph(self):
        self.generate_nodes()
        self.generate_edges()

    def generate_nodes(self):
        lines = self.file.readlines()
        self.label = lines[0]
        for line in lines[1:]:
            node = Node(*line.split(","))
            self.nodes.append(node)
            self.nodes_dictionary[node.get_city()] = node.get_id()
        self.file.close()

    def generate_edges(self):
        for node in self.nodes:
            if node.get_id() % 2 == 0 and node.get_id() > 1:
                self.calculate_edges(node, True)
            elif node.get_id() % 2 != 0 and node.get_id() > 2:
                self.calculate_edges(node, False)

    def calculate_edges(self, node, even):
        id = node.get_id()
        id_index = id - 1

        # caso seja

        def set_edges(node_a, node_b):
            distance = 1.1 * self.calculate_distance(node_a, node_b)
            if node_b not in node_a.get_neighbourhood():
                node_a.add_edge(Edge(node_a, node_b, distance))
            if node_a not in node_b.get_neighbourhood():
                node_b.add_edge(Edge(node_b, node_a, distance))

        if even:
            # conecta x com x+2
            if id + 2 <= len(self.nodes):
                other_node = self.nodes[id_index + 2]
                set_edges(node, other_node)
            # conecta x com x-1
            other_node = self.nodes[id_index - 1]
            set_edges(node, other_node)
        else:
            # conecta x com x+1
            if id + 1 <= len(self.nodes):
                other_node = self.nodes[id_index + 1]
                set_edges(node, other_node)
            # conecta x com x-2
            other_node = self.nodes[id_index - 2]
            set_edges(node, other_node)

    def calculate_distance(self, node, other_node):
        delta_lat = node.get_lat() - other_node.get_lat()
        delta_lng = node.get_lng() - other_node.get_lng()
        return math.sqrt(delta_lat**2 + delta_lng**2)

    def get_id_by_name(self, name):
        return self.nodes_dictionary[name]

    def get_node_by_id(self, id):
        return self.nodes[id-1]

    def print_graph(self):
        print('nodes')
        for node in self.nodes:
            print(node.get_id())
            for edge in node.get_edges():
                for edge_node in edge.get_nodes():
                    if edge_node != node:
                        print ('\t',edge_node.get_id(), '\t', edge.get_distance())
