class AStar:
    def choose(self, candidates, problem):
        # A busca greedy expande o nó que parece mais próximo do objetivo
        chosen_index = 0
        # Candidates are node tree types
        for i in range(1,len(candidates)):
            if candidates[i].get_cost() + problem.heuristic(candidates[i]) < candidates[chosen_index].get_cost() + problem.heuristic(candidates[chosen_index]):
                chosen_index = i

        return chosen_index
