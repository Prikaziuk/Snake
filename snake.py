__author__ = 'Admin'
#!/usr/bin/env python3

class Canvas:
    def __init__(self, width, height, fill='.'):
        self._width = width
        self._height = height
        self._fill = fill
        self._screen = [[fill] * width for _ in range(height)]
        self._figures = []


    def put_snake(self, x, y, fill, command):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return
        self._screen[y][x] = fill

    def move_snake(self, x, y, сommand, fill):
        while True:# надо для бесконечного хождения змеёй по полю
            command = input()
            if command == '8':
                y -= 1
            if command == '2':
                y += 1
            if command == '4':
                x -= 1
            if command == '6':
                x += 1


    def put_apple(self, x, y, fill):
        if x < 0 or x >= self._width or y < 0 or y >= self._height:
            return
        self._screen[y][x] = fill

    def paint(self):
        for figure in self._figures:
            figure.paint()
        for line in self._screen:
            print(''.join(line))
        print()


class Snake:
    def __init__(self, canvas, x, y, command = None, fill = 'x'):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._fill = fill
        self._command = command

    def set_parameters(self, *args):
        self._x, self._y = args

    def paint(self, fill=None):
        if fill is None:
            fill = self._fill
        # noinspection PyProtectedMember
        self._canvas.put_snake(self._x, self._y, command, fill)


class Apple:# надо добавить число яблок и поставить рандом в пределах canvas на координаты
    def __init__(self, canvas, x, y, fill = 'o'):
        self._canvas = canvas
        self._x = x
        self._y = y
        self._fill = fill

    def set_parameters(self, *args):
        self._x, self._y = args

    def paint(self, fill=None):
        if fill is None:
            fill = self._fill
        # noinspection PyProtectedMember
        self._canvas.put_apple(self._x, self._y, fill)


def main():
    print('Введите координаты яблока')
    print('x = ')
    x = int(input())
    print('y = ')
    y = int(input())
    canvas = Canvas(10, 10)
    canvas.paint()
    canvas.put_apple(x, y, 'o')
    canvas.paint()
    canvas.put_snake(0, 0, None, 'x')
    canvas.paint()

if __name__ == '__main__':
    main()