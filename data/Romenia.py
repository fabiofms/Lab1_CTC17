import math

class Node:
    def __init__(self, id, city, dist_bucharest):
        self.id = int(id)
        self.city = city
        self.dist_to_target = dist_bucharest
        self.edges = []

    def get_id(self):
        return self.id

    def get_city(self):
        return self.city

    def get_dist_to_target(self):
        return self.dist_to_target

    def add_edge(self, edge):
        #if edge not in self.edges:
        self.edges.append(edge)

    def get_edges(self):
        return self.edges


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

class Graph:
    def __init__(self):
        self.nodes = []
        self.nodes_dictionary = {}
        self.edges = []
        self.generate_graph()

    def generate_graph(self):
        self.generate_nodes()
        self.generate_edges()

    def generate_nodes(self):
        self.generate_one_node(1, 'Arad', 366)
        self.generate_one_node(2, 'Bucharest', 0)
        self.generate_one_node(3, 'Craiova', 160)
        self.generate_one_node(4, 'Dobreta', 242)
        self.generate_one_node(5, 'Eforie', 161)
        self.generate_one_node(6, 'Fagaras', 178)
        self.generate_one_node(7, 'Giurgiu', 77)
        self.generate_one_node(8, 'Hirsova', 151)
        self.generate_one_node(9, 'Iasi', 226)
        self.generate_one_node(10, 'Lugoj', 244)
        self.generate_one_node(11, 'Mehadia', 241)
        self.generate_one_node(12, 'Neamt', 234)
        self.generate_one_node(13, 'Oradea', 380)
        self.generate_one_node(14, 'Pitesti', 98)
        self.generate_one_node(15, 'Rimnicu Vilcea', 193)
        self.generate_one_node(16, 'Sibiu', 253)
        self.generate_one_node(17, 'Timisoara', 329)
        self.generate_one_node(18, 'Urziceni', 80)
        self.generate_one_node(19, 'Vaslui', 199)
        self.generate_one_node(20, 'Zerind', 374)

    def generate_one_node(self, id, city, dist):
        node = Node(id, city, dist)
        self.nodes.append(node)
        self.nodes_dictionary[node.get_city()] = node.get_id()

    def generate_edges(self):
        self.generate_one_edge('Oradea', 'Zerind', 71)
        self.generate_one_edge('Oradea', 'Sibiu', 151)
        self.generate_one_edge('Zerind', 'Arad', 75)
        self.generate_one_edge('Arad', 'Sibiu', 140)
        self.generate_one_edge('Arad', 'Timisoara', 118)
        self.generate_one_edge('Timisoara', 'Lugoj', 111)
        self.generate_one_edge('Lugoj', 'Mehadia', 70)
        self.generate_one_edge('Mehadia', 'Dobreta', 75)
        self.generate_one_edge('Dobreta', 'Craiova', 120)
        self.generate_one_edge('Craiova', 'Rimnicu Vilcea', 146)
        self.generate_one_edge('Rimnicu Vilcea', 'Sibiu', 80)
        self.generate_one_edge('Sibiu', 'Fagaras', 99)
        self.generate_one_edge('Fagaras', 'Bucharest', 211)
        self.generate_one_edge('Bucharest', 'Pitesti', 101)
        self.generate_one_edge('Pitesti', 'Rimnicu Vilcea', 97)
        self.generate_one_edge('Pitesti', 'Craiova', 138)
        self.generate_one_edge('Bucharest', 'Giurgiu', 90)
        self.generate_one_edge('Bucharest', 'Urziceni', 80)
        self.generate_one_edge('Urziceni', 'Hirsova', 98)
        self.generate_one_edge('Hirsova', 'Eforie', 86)
        self.generate_one_edge('Urziceni', 'Vaslui', 142)
        self.generate_one_edge('Vaslui', 'Iasi', 92)
        self.generate_one_edge('Iasi', 'Neamt', 87)

    def generate_one_edge(self, city_a, city_b, distance):
        node_a = self.get_node_by_id(self.get_id_by_name(city_a))
        node_b = self.get_node_by_id(self.get_id_by_name(city_b))
        edge = Edge(node_a, node_b, distance)
        self.edges.append(edge)
        node_a.add_edge(edge)
        node_b.add_edge(Edge(node_b, node_a, distance))

    def calculate_distance(self, node):
        return node.get_dist_to_target()

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


class Romenia:
    def __init__(self, origin):
        self.graph = Graph()
        self.initial_state = self.graph.get_id_by_name(origin)
        self.goal_state = self.graph.get_id_by_name('Bucharest')

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
        node = self.graph.get_node_by_id(chosen_candidate.get_state())
        expanding_nodes = []
        for edge in node.get_edges():
            cost = edge.get_distance()
            expanding_nodes.append((edge.get_destiny_id(), cost))
        return expanding_nodes

    def heuristic(self, candidate):
        # Candidate is node tree type
        return self.graph.calculate_distance(self.graph.get_node_by_id(candidate.get_state()))

