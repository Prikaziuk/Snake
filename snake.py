#!/usr/bin/env python3

"""
Python version of the common game "Snake and apples".

Usage: snake.py [number_of_apples]
"""
from random import randrange
from collections import deque

# import sys sys.argv[1] = number_of_apples

"""
Some constants that will be used: snake direction (str), symbols of snake (str) and apple (str)
 and number of apples to appear on the field (int)
"""
DOWN = 's'
UP = 'w'
RIGHT = 'd'
LEFT = 'a'

SNAKE = 'z'
APPLE = 'o'

NUMBER_OF_APPLES = 5


class Field:
    """
    Information about the field.

    Attributes:
        width (int) : width of the field
        height (int) : height of the field
    """
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def width(self):
        """
        :return: (int)
            width
        """
        return self._width

    def height(self):
        """
        :return: (int)
            height
        """
        return self._height


class Snake:
    """
    Information about the snake.
    """
    def __init__(self, head_coord):
        """
        Arg:
            head_coord (tuple) : coordinates of the snake head (x, y)
        """
        self._snake_coord = deque([head_coord])

    def __len__(self):
        """
        :return:
            int : length of the snake
        """
        return len(self._snake_coord)

    def __iter__(self):
        """
        :return: tuple from the list of tuples
        """
        return iter(self._snake_coord)

    def head(self):
        """
        :return:
            (tuple) : coordinates of the snake head (x, y)
        """
        return self._snake_coord[-1]

    def snake_coordinates(self):
        """
        :return:
            (list of tuples) : list of coordinates of the snake (x, y)
        """
        return self._snake_coord

    def move(self, position, is_apple):
        """
        Moves the snake in the given direction

        :param position (tuple) : new coordinates of the snake head (new step direction)
        :param is_apple (bool) : True if apple is at the position, False otherwise
        :return: None
        """
        self._snake_coord.append(position)
        if not is_apple:
            self._snake_coord.popleft()

    def revert(self):
        """
        Reverts the snake

        :return: None
        """
        self._snake_coord.reverse()


def user_input():
    """
    When everything is well
    :return:
        direction (str) : DOWN, UP, RIGHT, LEFT

    When something goes wrong (typo in input)
    :print:
        (str) : "input() does not give any direction. Available directions are: DOWN, UP, RIGHT,LEFT"
                 "Please, type valid command to set snake direction:"
        and asks user for new input of direction
    """
    direction = input()
    while direction not in [DOWN, UP, RIGHT, LEFT]:
        print("'{}' does not set any direction. \n Available directions are:"
              " \n \tDOWN : '{}' \n \tUP : '{}' \n \tRIGHT : '{}' \n \tLEFT : '{}' \n "
              "Please, type valid command to set snake direction:".format(direction, DOWN, UP, RIGHT, LEFT))
        direction = input()
    return direction


class Game:
    """
    Information about the game process.

    Attributes:
        field (class) : class with parameters of the field for a game
        snake (class) : class with parameters of snake
        user (function) : user_input()
    """
    def __init__(self, field, snake, user):
        self._field = field
        self._snake = snake
        self._user_function = user
        self._apples_positions = set()
        self._direction_action = {
            LEFT: lambda x, y: ((x - 1) % self._field.width(), y),
            RIGHT: lambda x, y: ((x + 1) % self._field.width(), y),
            UP: lambda x, y: (x, (y - 1) % self._field.height()),
            DOWN: lambda x, y: (x, (y + 1) % self._field.height())
        }

    def put_apples(self, number=NUMBER_OF_APPLES):
        """
        Fills the set of _apples_positions

        :param number (int) : number of apples to be put on the field, default NUMBER_OF_APPLES
        :return: None
        """
        while len(self._apples_positions) < number and self._snake.head() not in self._apples_positions:
            self._apples_positions.add((randrange(self._field.height()), randrange(self._field.width())))

    def _move_snake(self):
        """
        Works with user input: transforms direction into snake_head coordinates (position)
        :return: None
        """
        direction = self._user_function()
        y, x = self._snake.head()
        position = self._direction_action[direction](x, y)
        is_apple = position in self._apples_positions
        if is_apple:
            self._apples_positions.remove(position)
        if len(self._snake) > 2 and position == self._snake.snake_coordinates()[-2]:
            self._snake.revert()
        else:
            self._snake.move(position, is_apple)

    def paint(self):
        """
        Prints field with apples and snake at the terminal
        :return: None
        """
        screen = [['_'] * self._field.width() for _ in range(self._field.height())]
        for coord in self._apples_positions:
            screen[coord[0]][coord[1]] = APPLE
        for coord in self._snake:
            screen[coord[0]][coord[1]] = SNAKE
        for line in screen:
            print(''.join(line))

    def check_snake(self):
        """
        Checks snake accidents

        :return: None if everything is well
        :print: "GAME OVER! Your snake crashed" if snake moves into itself and interrupts programme
        """
        if len(self._snake) != len(set(self._snake.snake_coordinates())):
            print("\n GAME OVER! Your snake crashed")
            quit()

    def start(self):
        """
        Starts and controls the game.

        Randomly puts apples on the field, asks user for snake movement direction,
        :return: None
        :print: "YOU WIN! All apples are safely collected" when the game is finished
        """
        self.put_apples()
        self.paint()
        while len(self._snake) < NUMBER_OF_APPLES + 1:
            self._move_snake()
            self.check_snake()
            self.paint()
        print("\n YOU WIN! All apples are safely collected")


def main():
    """
    Create objects of all classes and starts the game
    :return: None
    """
    field = Field(10, 10)
    snake = Snake((0, 0))
    game = Game(field, snake, user_input)
    game.start()


if __name__ == '__main__':
    main()