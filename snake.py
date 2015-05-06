__author__ = 'Admin'
#!/usr/bin/env python3

# run like ./snake.py number_of_apples

import random
#import sys sys.argv[1] = number_of_apples


# some constants that will be used

# direction of snake movements
DOWN = 's'
UP = 'w'
RIGHT = 'd'
LEFT = 'a'

# snake parameters
SNAKE = 'z'
snake_length = 1
snake_trace = []

# apple parameters
APPLE = 'o'
NUMBER_OF_APPLES = 5

class Field:
# create a field
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._screen = [['_'] * width for _ in range(height)]

    # randomly put "number" quantity of apples on the screen
    def put_apples(self, number = NUMBER_OF_APPLES):
        for _ in range(number):
            self._screen[random.randint(0, self._width-1)][random.randint(0, self._height-1)] = APPLE
        # test that all apples are at unique positions
        actual_number_of_apples = 0
        for line in self._screen:
            actual_number_of_apples += line.count(APPLE)
        # if more then one apple is at the same position put_apple again
        if actual_number_of_apples != number:
            self.put_apples()


# paint all what is on the field
    def paint(self):
        for line in self._screen:
            print(''.join(line))
        print()


class Snake:
# put snake in the beginning of the field (beginning coordinates are x = 0, y = 0)
    def __init__(self, field, x = 0, y = 0):
        self._field = field
        self._x = x
        self._y = y
        self._field._screen[x][y] = SNAKE
        snake_trace.append([x, y])

# moves snake in the given direction
    def move(self, direction):
        # remove snake from the screen
        global snake_length
        for coord in snake_trace[-snake_length:]:
            self._field._screen[coord[1]][coord[0]] = '_'

        if direction == UP:
            self._y = (self._y - 1) % self._field._height
        elif direction == DOWN:
            self._y = (self._y + 1) % self._field._height
        elif direction == LEFT:
            self._x = (self._x - 1) % self._field._width
        elif direction == RIGHT:
            self._x = (self._x + 1) % self._field._width

        # append new coordinates of snake
        snake_trace.append([self._x, self._y])
        if self._field._screen[self._y][self._x] == APPLE:
            snake_length += 1

        # add whole snake to the screen again
        for coord in snake_trace[-snake_length:]:
            self._field._screen[coord[1]][coord[0]] = SNAKE

        # test snake accidents
        actual_snake_length = 0
        for line in self._field._screen:
            actual_snake_length += line.count(SNAKE)
        # if more then one apple is at the same position put_apple again
        if actual_snake_length != snake_length:
            print("GAME OVER! Your snake crashed")
            quit()


def main():
    field = Field(10, 10)
    field.put_apples()
    snake = Snake(field)
    field.paint()
    while True:
        direction = input()
        if direction not in [DOWN, UP, RIGHT, LEFT]:
            print("This is not direction, please, try again")
            continue
        else:
            snake.move(direction)
            field.paint()
        if snake_length == NUMBER_OF_APPLES + 1:
            print("Finish")
            break


if __name__ == '__main__':
    main()