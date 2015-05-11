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

# apple parameters
APPLE = 'o'
NUMBER_OF_APPLES = 5


class Field:
# create a field
    def __init__(self, width, height):
        self._width = width
        self._height = height


class Snake:
# coordinates in tuple (x, y)
    def __init__(self, head_coord):
        self._head_coord = head_coord
        self._snake_coord = []
        self._snake_coord.append(head_coord)

    def length(self):
        return len(self._snake_coord)

    def head(self):
        return self._head_coord

# moves snake in the given direction
    def move(self, position, is_apple):
        self._head_coord = position
        self._snake_coord.append(position)
        if is_apple == False:
            self._snake_coord.pop(0)
# test snake accidents
        if self.length() != len(set(self._snake_coord)):
            print("GAME OVER! Your snake crashed")
            quit()


class User:
    def __init__(self):
        pass

    def get_direction(self):
        direction = input()
        if direction in [DOWN, UP, RIGHT, LEFT]:
            return direction


class Game:
    def __init__(self, field, snake, user):
        self._field = field
        self._snake = snake
        self._user = user
        self._apples_positions = []

# randomly put "number" quantity of apples on the screen
    def put_apples(self, number = NUMBER_OF_APPLES):
        for _ in range(number):
            self._apples_positions.append([random.randint(0, self._field._width-1), random.randint(0, self._field._height-1)])
# test that all apples are at unique positions and are not already on snake's place. If more then one apple is at the same position put_apple again.
        if len(self._apples_positions) != number or self._snake.head() in self._apples_positions:
            self.put_apples()

    def move_snake(self):
# works with User input: transforms commands into snake_head coordinates (position)
        direction = self._user.get_direction()
        x = self._snake.head()[0]
        y = self._snake.head()[1]
        print(self._snake.head())
        if direction == LEFT:
            x = (x - 1) % self._field._width
        elif direction == RIGHT:
            x = (x + 1) % self._field._width
        elif direction == UP:
            y = (y - 1) % self._field._height
        elif direction == DOWN:
            y = (y + 1) % self._field._height
        position = (x, y)
        print(position)
# checks if there is an apple at this point
        if position in self._apples_positions:
            is_apple = True
            self._apples_positions.remove(position)
        else:
            is_apple = False
        self._snake.move(position, is_apple)

    def paint(self):
        screen = [['_'] * self._field._width for _ in range(self._field._height)]
        for coord in self._apples_positions:
            screen[coord[0]][coord[1]] = APPLE
        for coord in self._snake._snake_coord:
             screen[coord[0]][coord[1]] = SNAKE
        for line in screen:
            print(''.join(line))

    def start(self):
        self.put_apples()
        while self._snake.length() < NUMBER_OF_APPLES + 1:
            self.move_snake()
            self.paint()
        print("Finish")

def main():
    field = Field(10, 10)
    snake = Snake((0,0))
    user = User()
    game = Game(field, snake, user)
    game.paint()
    game.start()



if __name__ == '__main__':
    main()