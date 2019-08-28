# estados
# nos: pai, filhos, profundidade, custo de trajetoria, estado
# operadores, expandir: criar novos nos
# Introduzir em QueueingFn sucessores na ordem de desejabilidade
import math


class Node:
    def __init__(self, id, city, lat, lng, state, population):
        self.id = int(id)
        self.city = city
        self.lat = float(lat)
        self.lng = float(lng)
        self.state = state
        self.population = population
        self.edges = []
        self.neighbourhood = []

    def get_id(self):
        return self.id

    def get_city(self):
        return self.city

    def get_lat(self):
        return self.lat

    def get_lng(self):
        return self.lng

    def add_edge(self, edge):
        #if edge not in self.edges:
        self.edges.append(edge)
        self.neighbourhood.append(edge.get_destiny_node())

    def get_edges(self):
        return self.edges

    def get_neighbourhood(self):
        return self.neighbourhood


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
        return math.sqrt(math.pow(delta_lat,2) + math.pow(delta_lng,2))

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


class MenorCaminho:
    def __init__(self, origin, destiny):
        self.file_path = "australia.csv"
        self.graph = Graph(self.file_path)
        self.initial_state = self.graph.get_id_by_name(origin)
        self.goal_state = self.graph.get_id_by_name(destiny)
        self.older_states = []
        self.older_states.append(self.initial_state)

    def get_initial_state(self):
        # return the initial state id
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state

    def is_goal_state(self, chosen_candidate):
        # Chosen candidate is a node tree type
        return self.get_goal_state() == chosen_candidate.get_state()

    def expand(self, chosen_candidate):
        # Chosen candidate is a node tree type
        self.older_states.append(chosen_candidate.get_state())
        node = self.graph.get_node_by_id(chosen_candidate.get_state())
        expanding_nodes = []
        for edge in node.get_edges():
            flag = True
            cost = edge.get_distance() + chosen_candidate.get_cost()
            state = edge.get_destiny_id()
            for old_state in self.older_states:
                if state == old_state:
                    flag = False
                    break
            if flag:
                expanding_nodes.append((state, cost))
        return expanding_nodes

    def heuristic(self, candidate):
        # Candidate is node tree type
        return self.graph.calculate_distance(self.graph.get_node_by_id(candidate.get_state()),
                                             self.graph.get_node_by_id(self.goal_state))

