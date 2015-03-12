__author__ = 'Admin'
#!/usr/bin/env python3

import random

DOWN = 's'
UP = 'w'
RIGHT = 'd'
LEFT = 'a'
SNAKE = []
APPLE = 'o'
snake_length = 1

class Field:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._screen = [['_'] * width for _ in range(height)]


    def put_snake(self, x, y):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return
        self._x = x
        self._y = y
        self._screen[y][x] = 'x'

    def move_snake(self, direction):
        self._screen[self._y][self._x] = '_'
        SNAKE.append([self._x, self._y])
        if direction == UP:
            self._y -=1
        elif direction == DOWN:
            self._y +=1
        elif direction == LEFT:
            self._x -=1
        elif direction == RIGHT:
            self._x +=1
        SNAKE.append([self._x, self._y])
        if self._screen[self._y][self._x] == APPLE:
            snake_length +=1
        for coord in range(snake_length):
            self._screen[SNAKE[-coord][1]][SNAKE[-coord][0]] = 'x'

    def put_apple(self, number):
        for _ in range(number):
            self._screen[random.randint(0, self._width-1)][random.randint(0, self._height-1)] = APPLE

    def paint(self):
        for line in self._screen:
            print(''.join(line))
        print()

def main():
    field = Field(10, 10)
    field.paint()
    field.put_apple(5)
    field.paint()
    field.put_snake(0, 0)
    field.paint()
    field.move_snake('s')
    field.paint()
    print(SNAKE)

if __name__ == '__main__':
    main()