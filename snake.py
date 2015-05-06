__author__ = 'Admin'
#!/usr/bin/env python3

import random

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

# sign of apple
APPLE = 'o'

class Field:
# create a field
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._screen = [['_'] * width for _ in range(height)]

# put snake in the beginning of the field (beginning coordinates are x = 0, y = 0)
    def put_snake(self, x = 0, y = 0):
        self._x = x
        self._y = y
        self._screen[x][y] = SNAKE
        snake_trace.append([self._x, self._y])

    def move_snake(self, direction, snake_length = snake_length):
        # remove snake from the screen
        for coord in snake_trace[-snake_length:]:
            self._screen[coord[1]][coord[0]] = '_'
        if direction == UP:
            self._y -=1
        elif direction == DOWN:
            self._y +=1
        elif direction == LEFT:
            self._x -=1
        elif direction == RIGHT:
            self._x +=1
        # append new coordinates of snake
        snake_trace.append([self._x, self._y])
        if self._screen[self._y][self._x] == APPLE:
            snake_length +=1
        # add whole snake to the screen again
        for coord in snake_trace[-snake_length:]:
            self._screen[coord[1]][coord[0]] = SNAKE

    def put_apples(self, number):
        for _ in range(number):
            self._screen[random.randint(0, self._width-1)][random.randint(0, self._height-1)] = APPLE

    def paint(self):
        for line in self._screen:
            print(''.join(line))
        print()

def main():
    field = Field(10, 10)
    field.paint()
    field.put_apples(5)
    field.paint()
    field.put_snake()
    field.paint()
    field.move_snake('s')
    field.paint()


if __name__ == '__main__':
    main()