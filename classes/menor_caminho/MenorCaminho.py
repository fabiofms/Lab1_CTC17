# estados
# nos: pai, filhos, profundidade, custo de trajetoria, estado
# operadores, expandir: criar novos nos
# Introduzir em QueueingFn sucessores na ordem de desejabilidade
from classes.menor_caminho.Graph import Graph


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

