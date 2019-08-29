# importing libraries
import numpy
import random


class State:
    def __init__(self, n, other_state=None):
        self.size = n
        self.empty = [n-1, n-1]
        self.state = self.init_state(n, other_state)

    def __eq__(self, other):
        size = self.get_size()
        my_state = self.get_state()
        other_state = other.get_state()
        if self.get_empty() != other.get_empty():
            return False
        if size != other.get_size():
            return False
        for i in range(size):
            for j in range(size):
                if my_state[i][j] != other_state[i][j]:
                    return False
        return True

    def init_state(self, n, other_state):
        state = numpy.zeros((n, n))
        if other_state is not None:
            self.empty = other_state.get_empty()
            other = other_state.get_state()
            for i in range(n):
                for j in range(n):
                    state[i][j] = other[i][j]
        else:
            for i in range(n):
                for j in range(n):
                    state[i][j] = ((n * i) + (j) + 1)
            state[n-1][n-1] = 0
        return state

    def get_state(self):
        return self.state

    def get_size(self):
        return self.size

    def get_empty(self):
        return self.empty

    def get_possible_movements(self):
        movements = []
        empty = self.get_empty()
        size = self.get_size()
        if empty[0] != 0:
            movements.append('up')
        if empty[0] != size - 1:
            movements.append('down')
        if empty[1] != 0:
            movements.append('left')
        if empty[1] != size - 1:
            movements.append('right')
        return movements

    def move(self, movement, print_it=False):
        direction_dict = {'up': (0, -1), 'down': (0, 1), 'left': (1, -1), 'right': (1, 1)}
        direction = direction_dict[movement]
        new_empty = self.empty.copy()
        new_empty[direction[0]] += direction[1]
        self.state[self.empty[0]][self.empty[1]] = self.state[new_empty[0]][new_empty[1]]
        self.state[new_empty[0]][new_empty[1]] = 0
        self.empty = new_empty
        if print_it:
            self.print_state()

    def manhattan_position(self, number, position):
        if number == 0:
            return 0
        size = self.get_size()
        position_ideal = [int((number - 1)/size), int(number - 1)%size]
        return abs(position[0] - position_ideal[0]) + abs(position[1] - position_ideal[1])

    def manhattan(self):
        size = self.get_size()
        manhattan_distance = 0
        for i in range(size):
            for j in range(size):
                manhattan_distance += self.manhattan_position(self.get_value([i, j]), [i, j])
        return manhattan_distance

    def get_value(self, position):
        return self.state[position[0], position[1]]

    def shuffle(self, shuffle_repetitions):
        for i in range(shuffle_repetitions):
            movements = self.get_possible_movements()
            index = random.randint(0, len(movements) - 1)
            movement_chosen = movements[index]
            self.move(movement_chosen, False)
        self.print_state()

    def print_state(self):
        for i in range(self.size):
            for j in range(self.size):
                print(int(self.state[i][j]), end = '\t')
            print()
        print()