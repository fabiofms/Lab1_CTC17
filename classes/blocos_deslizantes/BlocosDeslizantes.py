from classes.blocos_deslizantes.State import State


class BlocosDeslizantes:
    def __init__(self, n, shuffle_repetitions, str, values=None, empty_var=None):
        self.size = n
        self.initial_state = State(n)
        if str == 'sh':
            self.initial_state.shuffle(shuffle_repetitions)
        elif str == 'iv':
            self.initial_state.begin_with_values(values, empty_var)
        self.goal_state = State(n)
        self.older_states = []
        self.older_states.append(self.initial_state)

    def get_initial_state(self):
        # return the initial state id
        return self.initial_state

    def get_goal_state(self):
        return self.goal_state

    def is_goal_state(self, chosen_candidate):
        # Chosen candidate is a node tree type
        return self.goal_state == chosen_candidate.get_state()

    def expand(self, chosen_candidate):
        self.older_states.append(chosen_candidate.get_state())
        expanding_states = []
        movements = chosen_candidate.get_state().get_possible_movements()
        for movement in movements:
            flag = True
            state = State(self.size, chosen_candidate.get_state())
            state.move(movement)
            for old_state in self.older_states:
                if state == old_state:
                    flag = False
                    break
            if flag:
                expanding_states.append((state, 1))
        return expanding_states

    def heuristic(self, candidate):
        return candidate.get_state().manhattan()