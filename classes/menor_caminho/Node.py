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
