#!/usr/bin/env python3

"""
Python version of the common game "Snake and apples".

Usage: snake.py [number_of_apples]
"""
from random import randrange
from snake import Snake, Field
from tkinter import *
from tkinter import messagebox

root = Tk()
# import sys sys.argv[1] = number_of_apples

"""
Some constants that will be used: snake direction (str), symbols of snake (str) and apple (str)
 and number of apples to appear on the field (int)
"""
DOWN = "DOWN"
UP = 'UP'
RIGHT = "RIGHT"
LEFT = 'LEFT'

SNAKE = 'z'
APPLE = 'o'

NUMBER_OF_APPLES = 5


class Game:
    """
    Information about the game process.

    Attributes:
        field (class) : class with parameters of the field for a game
        snake (class) : class with parameters of snake
    """
    def __init__(self, field, snake):
        self._field = field
        self._snake = snake
        self._apples_positions = set()
        self._direction_action = {
            LEFT: lambda x, y: (y, (x - 1) % self._field.width()),
            RIGHT: lambda x, y: (y, (x + 1) % self._field.width()),
            UP: lambda x, y: ((y - 1) % self._field.height(), x),
            DOWN: lambda x, y: ((y + 1) % self._field.height(), x)
        }
        self._canvas = Canvas(root, width=self._field.width()*10, height=self._field.height()*10, bg='green')
        self._canvas.pack()

    def put_apples(self, number=NUMBER_OF_APPLES):
        """
        Fills the set of _apples_positions

        :param number (int) : number of apples to be put on the field, default NUMBER_OF_APPLES
        :return: None
        """
        while len(self._apples_positions) < number and self._snake.head() not in self._apples_positions:
            self._apples_positions.add((randrange(self._field.height()), randrange(self._field.width())))

    def _move_snake(self, direction):
        """
        Works with user input: transforms direction into snake_head coordinates (position)
        :return: None
        """
        y, x = self._snake.head()
        position = self._direction_action[direction](x, y)
        is_apple = position in self._apples_positions
        if is_apple:
            self._apples_positions.remove(position)
        if len(self._snake) > 2 and position == self._snake.snake_coordinates()[-2]:
            self._snake.revert()
        else:
            self._snake.move(position, is_apple)
        self.paint_snake()
        self.paint_apples()

    def paint_snake(self):
        self.check_snake()
        self._canvas.delete('snake')
        for coord in self._snake:
            self._canvas.create_rectangle(coord[1]*10, coord[0]*10, coord[1]*10 + 10, coord[0]*10 + 10,
                                          outline='white', fill='blue', tag='snake')
        self.win_check()

    def paint_apples(self):
        self._canvas.delete('apple')
        for coord in self._apples_positions:
            self._canvas.create_oval(coord[1]*10, coord[0]*10, coord[1]*10+10, coord[0]*10+10,
                                     fill='red', tag='apple')

    def paint(self):
        """
        Prints field with apples and snake and creates buttons
        :return: None
        """
        but = Button(root, text='LEFT')
        but.pack(side="left")
        but.bind("<Button-1>", lambda event: self._move_snake('LEFT'))
        but2 = Button(root, text='RIGHT')
        but2.pack(side='right')
        but2.bind("<Button-1>", lambda event: self._move_snake('RIGHT'))
        but3 = Button(root, text='UP')
        but3.pack(side='top')
        but3.bind("<Button-1>", lambda event: self._move_snake('UP'))
        but4 = Button(root, text='DOWN')
        but4.pack(side='bottom')
        but4.bind("<Button-1>", lambda event: self._move_snake('DOWN'))
        self.paint_snake()
        self.paint_apples()
        root.mainloop()

    def check_snake(self):
        """
        Checks snake accidents

        :return: None if everything is well
        :print: "GAME OVER! Your snake crashed" if snake moves into itself and interrupts programme
        """
        if len(self._snake) != len(set(self._snake.snake_coordinates())):
            messagebox.showinfo("GAME OVER!", "Your snake crashed")
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

    def win_check(self):
        if len(self._apples_positions) == 0:
            messagebox.showinfo("YOU WIN!", "All apples are safely collected")
            quit()


def main():
    """
    Create objects of all classes and starts the game
    :return: None
    """
    field = Field(10, 10)
    snake = Snake((0, 0))
    game = Game(field, snake)
    game.start()

if __name__ == '__main__':
    main()