import copy
import collections
import time

import numpy as np
import pandas as pd


class Direction:
    def __init__(self, dx, dy):
        self.move = [dx, dy]

    def get_move(self):
        return self.move


def compare_direction(direct1: Direction, direct2: Direction):
    l1 = direct1.get_move()
    l2 = direct2.get_move()
    return l1[0] == l2[0] and l1[1] == l2[1]


class GameField:
    FILE_SPLITTER = ";"
    S_EMPTY = "0"
    MOVE_MAX_COUNT = 200
    FIELD_SIZE = 32  # Assuming the field is always 32x32
    MAX_TIME = 5*60

    class Cell:
        EMPTY = 0
        APPLE = 1

    class direction:
        RIGHT = Direction(0, 1)
        DOWN = Direction(1, 0)
        LEFT = Direction(0, -1)
        UP = Direction(-1, 0)

    def __init__(self):
        self.init_field = np.zeros((self.FIELD_SIZE, self.FIELD_SIZE), dtype=int)
        self.start_time = time.time()
        #print(self.start_time)

    def fill(self, filename):
        colname = [f"col{i}" for i in range(self.FIELD_SIZE)]
        df = pd.read_csv(filename, header=None, sep=";", names=colname)
        self.init_field = df.values

    def check_time(self):
        cur_time = time.time()
        if cur_time - self.start_time > self.MAX_TIME:
            raise Exception("The maximum running time of the program has been exceeded.")

    def testAnt(self, chromosome):
        self.check_time()
        from Ant import Ant  # Assuming Ant class has been defined and is in ant.py
        ant = Ant(chromosome)
        field = copy.deepcopy(self.init_field)
        eaten_apple_count = 0
        ant_direction = self.direction.RIGHT
        ant_pos = [0, 0]

        for _ in range(self.MOVE_MAX_COUNT):
            forward_pos = self.get_forward_cell_coord(ant_pos, ant_direction)
            forward_cell = field[forward_pos[0], forward_pos[1]]
            ant_action = ant.getAction(forward_cell)

            if ant_action == Ant.Action.MOVE_FORWARD:
                ant_pos = forward_pos
                if field[ant_pos[0], ant_pos[1]] == self.Cell.APPLE:
                    field[ant_pos[0], ant_pos[1]] = self.Cell.EMPTY
                    eaten_apple_count += 1

            ant_direction = self.get_new_direction(ant_direction, ant_action)

        return eaten_apple_count

    def get_forward_cell_coord(self, cur_pos, direction: Direction):
        move = direction.get_move()
        new_pos = [cur_pos[0] + move[0], cur_pos[1] + move[1]]
        # new_pos = [n % field_size for n in new_pos]  # Wrap around for toroidal field
        if self.isInField(new_pos):
            return new_pos

        # Если муравей выходит за поле, то заходит с другой стороны (поле кольцевое)
        if new_pos[0] >= self.FIELD_SIZE:
            new_pos[0] = 0
        elif new_pos[0] < 0:
            new_pos[0] = self.FIELD_SIZE - 1

        elif new_pos[1] >= self.FIELD_SIZE:
            new_pos[1] = 0
        else:
            new_pos[1] = self.FIELD_SIZE - 1
        return new_pos

    def isInField(self, cellCoord) -> bool:
        return self.FIELD_SIZE > cellCoord[0] >= 0 and self.FIELD_SIZE > cellCoord[1] >= 0

    def get_new_direction(self, old_direction, action):
        from Ant import Ant
        if action == Ant.Action.TURN_LEFT:
            return self.direction.LEFT if compare_direction(old_direction, self.direction.UP) else \
                   self.direction.DOWN if compare_direction(old_direction, self.direction.LEFT) else \
                   self.direction.RIGHT if compare_direction(old_direction, self.direction.DOWN) else \
                   self.direction.UP

        elif action == Ant.Action.TURN_RIGHT:
            return self.direction.RIGHT if compare_direction(old_direction, self.direction.UP) else \
                   self.direction.UP if compare_direction(old_direction, self.direction.LEFT) else \
                   self.direction.LEFT if compare_direction(old_direction, self.direction.DOWN) else \
                   self.direction.DOWN

        return old_direction
