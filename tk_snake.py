#!/usr/bin/env python3

"""
Python version of the common game "Snake and apples".
"""

from random import randrange
from snake import Snake, Field
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

"""
Some constants that will be used: snake direction (str), symbols of snake (str) and apple (str)
 and number of apples to appear on the field (int)
"""
DOWN = "DOWN"
UP = 'UP'
RIGHT = "RIGHT"
LEFT = 'LEFT'

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
        self._apple_position = tuple()
        self._painted_apples = 0
        self._direction_action = {
            LEFT: lambda x, y: (y, (x - 1) % self._field.width()),
            RIGHT: lambda x, y: (y, (x + 1) % self._field.width()),
            UP: lambda x, y: ((y - 1) % self._field.height(), x),
            DOWN: lambda x, y: ((y + 1) % self._field.height(), x)
        }
        self._canvas = tk.Canvas(root, width=self._field.width()*10, height=self._field.height()*10, bg='green')
        self._canvas.pack()
        self._after_id = list()

    def put_apple(self):
        """
        Randomly puts an apple on the field, never on the snake

        :return: None
        """
        apple_coord = (randrange(self._field.height()), randrange(self._field.width()))
        if apple_coord in self._snake:
            self.put_apple()
        self._apple_position = apple_coord

    def _move_snake(self, direction):
        """
        Works with user input: transforms direction into snake_head coordinates (position)
        :return: None
        """
        y, x = self._snake.head()
        position = self._direction_action[direction](x, y)
        is_apple = position == self._apple_position
        if is_apple:
            self.put_apple()
            self.paint_apple()
        if len(self._snake) > 2 and position == self._snake.snake_coordinates()[-2]:
            self._snake.revert()
        else:
            self._snake.move(position, is_apple)
        self.paint_snake()
        self._after_id.append(self._canvas.after(500, self._move_snake, direction))
        self._canvas.after_cancel(self._after_id.pop(0))

    def paint_snake(self):
        """
        Paints snake on the field

        :return: None
        """
        self.check_snake()
        self._canvas.delete('snake')
        for coord in self._snake:
            self._canvas.create_rectangle(coord[1]*10, coord[0]*10, coord[1]*10 + 10, coord[0]*10 + 10,
                                          outline='white', fill='blue', tag='snake')
        self.win_check()

    def check_snake(self):
        """
        Checks snake accidents

        :return: None if everything is well
        :raise: message window "GAME OVER! Your snake crashed" if snake moves into itself and interrupts programme
        """
        if len(self._snake) != len(set(self._snake.snake_coordinates())):
            messagebox.showinfo("GAME OVER!", "Your snake crashed")
            quit()

    def win_check(self):
        """
        Checks winning conditional

        :return: None
        :raise: message window "YOU WIN! All apples are safely collected" when the game is finished
        """
        if len(self._snake) == NUMBER_OF_APPLES + 1:
            messagebox.showinfo("YOU WIN!", "All apples are safely collected")
            quit()

    def paint_apple(self):
        """
        Paints an apple on the field, no more than NUMBER_OF_APPLES times for the game

        :return: None
        """
        self._canvas.delete('apple')
        coord = self._apple_position
        if self._painted_apples < NUMBER_OF_APPLES:
            self._canvas.create_oval(coord[1]*10, coord[0]*10, coord[1]*10+10, coord[0]*10+10,
                                     fill='red', tag='apple')
            self._painted_apples += 1

    def paint(self):
        """
        Prints field with apples and snake and creates buttons
        :return: None
        """
        but = tk.Button(root, text='LEFT')
        but.pack(side="left")
        but.bind("<Button-1>", lambda event: self._move_snake('LEFT'))
        but2 = tk.Button(root, text='RIGHT')
        but2.pack(side='right')
        but2.bind("<Button-1>", lambda event: self._move_snake('RIGHT'))
        but3 = tk.Button(root, text='UP')
        but3.pack(side='top')
        but3.bind("<Button-1>", lambda event: self._move_snake('UP'))
        but4 = tk.Button(root, text='DOWN')
        but4.pack(side='bottom')
        but4.bind("<Button-1>", lambda event: self._move_snake('DOWN'))
        self.paint_snake()
        self.paint_apple()
        root.mainloop()

    def start(self):
        """
        Starts and controls the game.

        Randomly puts apple on the field, initiates snake movements, paints all on the window
        asks user for snake movement direction
        """
        self.put_apple()
        self._after_id.append(self._canvas.after(500, self._move_snake, "RIGHT"))
        self.paint()


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