class AStar:
    def choose(self, candidates, problem):
        # A* expands the node that seems closer to the target, considering the cost of the trajetory to achieve
        # that node from the initial node
        chosen_index = 0

        # selecting the candidate (node trees) with the best heuristic and route
        for i in range(1, len(candidates)):
            if (candidates[i].get_cost() + problem.heuristic(candidates[i])) < (candidates[chosen_index].get_cost() + problem.heuristic(candidates[chosen_index])):
                chosen_index = i
        return chosen_index
