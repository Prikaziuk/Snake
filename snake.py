__author__ = 'Admin'
#!/usr/bin/env python3

import random


class Canvas:
    def __init__(self, width, height, fill='.'):
        self._width = width
        self._height = height
        self._fill = fill
        self._screen = [[fill] * width for _ in range(height)]
        self._figures = []


    def put_snake(self, x, y, fill):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return
        self._x = x
        self._y = y
        self._screen[y][x] = fill

    def move_snake(self, direction):
        if direction == 'w':
            self._y -=1
        elif direction == 's':
            self._y +=1
        elif direction == 'a':
            self._x -=1
        elif direction == 'd':
            self._x +=1


    def put_apple(self, number, fill):
        while number:
            self._x = random.randint(0, self._width)
            self._y = random.randint(0, self._height)
            self._screen[self._x][self._y] = fill
            number -=1

    def paint(self):
        for figure in self._figures:
            figure.paint()
        for line in self._screen:
            print(''.join(line))
        print()




def main():
    canvas = Canvas(10, 10)
    canvas.paint()
    canvas.put_apple(3, 'o')
    canvas.paint()
    canvas.put_snake(0, 0, 'x')
    canvas.paint()
    canvas.move_snake('s')
    canvas.paint()

if __name__ == '__main__':
    main()