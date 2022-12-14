import logging


class Robot:
    N = 'NORTH'
    S = 'SOUTH'
    W = 'WEST'
    E = 'EAST'
    CMD_PLACE = 'PLACE'
    CMD_MOVE = 'MOVE'
    CMD_RIGHT = 'RIGHT'
    CMD_LEFT = 'LEFT'
    CMD_REPORT = 'REPORT'

    def __init__(self, min_x, max_x, min_y, max_y):
        # TODO: use a config file for settings
        # set the range of a table for robot to roam
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        # set a list of turns allowed
        self.f_list = {Robot.N, Robot.S, Robot.W, Robot.E}
        # set default values before a valid placement on the table
        self.x = -1
        self.y = -1
        self.f = 'OFF'
        # init a logger to include the class name
        self.log = logging.getLogger(self.__class__.__name__)

    # not valid place command, if position and facing values are not valid
    def is_valid_place(self, x, y, f):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if (x >= self.min_x) and (
                x <= self.max_x) and (
                y >= self.min_y) and (
                y <= self.max_y) and (
                f in self.f_list
        ):
            self.log.debug("Valid Place Command: {},{},{}".format(x, y, f))
            return True
        else:
            self.log.debug("Invalid Place Command: {},{},{}".format(x, y, f))
            return False

    # not on the table, if self.x,self.y are not in min-max range and self.f is not in the list
    def is_on_table(self):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if (self.x >= self.min_x) and (
                self.x <= self.max_x) and (
                self.y >= self.min_y) and (
                self.y <= self.max_y) and (
                self.f in self.f_list
        ):
            self.log.debug("On Table: {},{},{}".format(self.x, self.y, self.f))
            return True
        else:
            self.log.debug("Not On Table: {},{},{}".format(self.x, self.y, self.f))
            return False

    # not valid move, if not on the table
    # not valid move, if falling
    def is_valid_move(self):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if (self.is_on_table()) and (
                (self.f == Robot.N and self.y < self.max_y) or
                (self.f == Robot.E and self.x < self.max_x) or
                (self.f == Robot.S and self.y > self.min_y) or
                (self.f == Robot.W and self.x > self.min_x)
        ):
            self.log.debug("Valid Move Command: {},{},{}".format(self.x, self.y, self.f))
            return True
        else:
            self.log.debug("Invalid Move Command: {},{},{}".format(self.x, self.y, self.f))
            return False

    # ignore, if place is not valid
    def place(self, x, y, f):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        self.log.debug("Place Command: {},{},{}".format(x, y, f))
        if self.is_valid_place(x, y, f):
            self.x = x
            self.y = y
            self.f = f
        self.log.debug("End Position: {},{},{}".format(self.x, self.y, self.f))
        return self.x, self.y, self.f

    # ignore, if move is not valid
    def move(self):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if self.is_valid_move():
            if self.f == Robot.N:
                self.y = self.y+1
            elif self.f == Robot.E:
                self.x = self.x+1
            elif self.f == Robot.S:
                self.y = self.y-1
            else:
                self.x = self.x-1
        self.log.debug("End Position: {},{},{}".format(self.x, self.y, self.f))
        return self.x, self.y

    # ignore, if robot is not on the table
    def left(self):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if self.is_on_table():
            if self.f == Robot.N:
                self.f = Robot.W
            elif self.f == Robot.W:
                self.f = Robot.S
            elif self.f == Robot.S:
                self.f = Robot.E
            else:
                self.f = Robot.N
        self.log.debug("End Position: {},{},{}".format(self.x, self.y, self.f))
        return self.f

    # ignore, if robot is not on the table
    def right(self):
        self.log.debug("Start Position: {},{},{}".format(self.x, self.y, self.f))
        if self.is_on_table():
            if self.f == Robot.N:
                self.f = Robot.E
            elif self.f == Robot.E:
                self.f = Robot.S
            elif self.f == Robot.S:
                self.f = Robot.W
            else:
                self.f = Robot.N
        self.log.debug("End Position: {},{},{}".format(self.x, self.y, self.f))
        return self.f

    # return current position of robot
    def get_position(self):
        if self.f not in self.f_list:
            position = "Robot is not on the table"
        else:
            position = "{},{},{}".format(self.x, self.y, self.f)
        return position

    # report position
    def report(self):
        position = self.get_position()
        print(position)
        return position

