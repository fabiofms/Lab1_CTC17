class Greedy:
    def choose(self, candidates, problem):
        # greedy expands the node that seems closer to the target according to a heuristic
        chosen_index = 0

        # selecting the candidate (node trees) with the best heuristic
        for i in range(1, len(candidates)):
            if problem.heuristic(candidates[i]) < problem.heuristic(candidates[chosen_index]):
                chosen_index = i
        return chosen_index
