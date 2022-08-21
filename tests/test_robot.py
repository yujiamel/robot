import pytest
from robot.robot import Robot


@pytest.fixture
def robot_obj():
    robot_obj = Robot(0, 5, 0, 5)
    return robot_obj


@pytest.mark.parametrize("x,y,f,expected",
                         [(0, 0, 'NORTH', True),
                          (0, 5, 'SOUTH', True),
                          (5, 0, 'EAST', True),
                          (5, 5, 'WEST', True),
                          (0, 1, ' ', False),
                          (0, -1, 'NORTH', False),
                          (0, 6, 'NORTH', False),
                          (-1, 0, 'NORTH', False),
                          (6, 0, 'NORTH', False)
                          ])
def test_is_valid_place(robot_obj, x, y, f, expected):
    assert robot_obj.is_valid_place(x, y, f) == expected


def test_is_on_table(robot_obj):
    # has not been placed on the table
    assert not robot_obj.is_on_table()

    # position is out of table range
    robot_obj.x = 1
    robot_obj.y = 6
    robot_obj.f = 'NORTH'
    assert not robot_obj.is_on_table()

    # position is valid
    robot_obj.x = 1
    robot_obj.y = 5
    robot_obj.f = 'NORTH'
    assert robot_obj.is_on_table()


@pytest.mark.parametrize("x,y,f,expected",
                         [(0, 0, 'NORTH', True),
                          (0, 0, 'SOUTH', False),
                          (0, 0, 'EAST', True),
                          (0, 0, 'WEST', False),
                          (0, 5, 'NORTH', False),
                          (0, 5, 'SOUTH', True),
                          (0, 5, 'EAST', True),
                          (0, 5, 'WEST', False),
                          (5, 0, 'NORTH', True),
                          (5, 0, 'SOUTH', False),
                          (5, 0, 'EAST', False),
                          (5, 0, 'WEST', True),
                          (5, 5, 'NORTH', False),
                          (5, 5, 'SOUTH', True),
                          (5, 5, 'EAST', False),
                          (5, 5, 'WEST', True)
                          ])
def test_is_valid_move(robot_obj, x, y, f, expected):
    # not on the table
    assert not robot_obj.is_valid_move()

    # on the table
    robot_obj.x = x
    robot_obj.y = y
    robot_obj.f = f
    assert robot_obj.is_valid_move() == expected


def test_place(robot_obj):
    assert robot_obj.place(0,0,'NORTH') == (0, 0, 'NORTH')
    # ignore invalid placement,
    assert robot_obj.place(1, 6, 'NORTH') == (0, 0, 'NORTH')


def test_move(robot_obj):
    # not on the table, no move
    assert robot_obj.move() == (-1, -1)

    # if it is to fall, don't move
    robot_obj.x = 5
    robot_obj.y = 0
    robot_obj.f = 'NORTH'
    robot_obj.move() == (5, 0)

    # valid move
    robot_obj.x = 1
    robot_obj.y = 1
    robot_obj.f = 'NORTH'
    assert robot_obj.move() == (1, 2)


def test_turn(robot_obj):
    # if not on the table, no turn
    assert robot_obj.left() == 'OFF'
    assert robot_obj.right() == 'OFF'

    robot_obj.x = 1
    robot_obj.y = 1
    robot_obj.f = 'NORTH'
    assert robot_obj.left() == 'WEST'
    assert robot_obj.left() == 'SOUTH'
    assert robot_obj.left() == 'EAST'
    assert robot_obj.left() == 'NORTH'
    assert robot_obj.right() == 'EAST'
    assert robot_obj.right() == 'SOUTH'
    assert robot_obj.right() == 'WEST'
    assert robot_obj.right() == 'NORTH'

