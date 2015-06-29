#!/usr/bin/env python3

"""
Python version of the common game "Snake and apples"
"""

from random import randrange
from snake import Snake, Field
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

"""
Some constants that will be used: snake direction (str), number of apples to appear on the field (int),
speed of snake movements in ms (int), scale of the field (int), shift for one step (int),
colours of field (str), snake (str) and apple (str)
"""
DOWN = "DOWN"
UP = "UP"
RIGHT = "RIGHT"
LEFT = "LEFT"

NUMBER_OF_APPLES = 20
SNAKE_SPEED = 250
SCALE = SHIFT = 10

FIELD_COLOUR = 'green'
SNAKE_COLOUR = 'blue'
APPLE_COLOUR = 'red'


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
            LEFT: lambda x, y: ((x - 1) % self._field.width(), y),
            RIGHT: lambda x, y: ((x + 1) % self._field.width(), y),
            UP: lambda x, y: (x, (y - 1) % self._field.height()),
            DOWN: lambda x, y: (x, (y + 1) % self._field.height())
        }
        self._canvas = tk.Canvas(root, width=self._field.width()*SCALE, height=self._field.height()*SCALE,
                                 bg=FIELD_COLOUR)
        self._canvas.pack()
        self._after_id = []

    def put_apple(self):
        """
        Randomly generates coordinate for an apple on the field

        :return: False if no place for an apple
        """
        self._apple_position = (randrange(self._field.width()), randrange(self._field.height()))
        while self._apple_position in self._snake:
            self._apple_position = (randrange(self._field.width()), randrange(self._field.height()))

    def _move_snake(self, direction):
        """
        Works with user input: transforms direction into snake_head coordinates (position)
        :return: None
        """
        position = self._direction_action[direction](*self._snake.head())
        is_apple = position == self._apple_position
        if is_apple:
            self.put_apple()
            self.paint_apple()
        if len(self._snake) > 2 and position == self._snake.snake_coordinates()[-2]:
            self._snake.revert()
        else:
            self._snake.move(position, is_apple)
        self.paint_snake()
        self._after_id.append(self._canvas.after(SNAKE_SPEED, self._move_snake, direction))
        self._canvas.after_cancel(self._after_id.pop(0))
        if self.check_win() or self.check_snake():
            self._canvas.after_cancel(self._after_id.pop(0))
            self.check_progress()

    def paint_snake(self):
        """
        Paints snake on the field

        :return: None
        """
        if not self.check_snake():
            self._canvas.delete('snake')
            for x, y in self._snake:
                self._canvas.create_rectangle(x*SCALE, y*SCALE, x*SCALE+SHIFT, y*SCALE+SHIFT,
                                              outline='white', fill=SNAKE_COLOUR, tag='snake')

    def check_snake(self):
        """
        Checks snake accidents

        :return: True when snake crashes
        """
        return len(self._snake) != len(set(self._snake.snake_coordinates()))

    def check_win(self):
        """
        Checks winning conditional

        :return: True when all apples are collected
        """
        return len(self._snake) == NUMBER_OF_APPLES + 1

    def check_progress(self):
        """
        Stops the game, when something happen

        :return: None
        :raise: message window "YOU WIN! All apples are safely collected" when the game is finished
        :raise: message window "GAME OVER! Your snake crashed" if snake moves into itself
        """
        if self.check_snake():
            but = tk.Button(root, text="Again?")
            but.pack()
            but.bind("<Button-1>", lambda event: [but.destroy(), main()])
            messagebox.showinfo("GAME OVER!", "Your snake crashed")
        if self.check_win():
            but = tk.Button(root, text="New level")
            but.pack()
            but.bind("<Button-1>", lambda event: [but.destroy(), main()])
            messagebox.showinfo("YOU WIN!", "All apples are safely collected")

    def paint_apple(self):
        """
        Paints an apple on the field, no more than NUMBER_OF_APPLES times for the game

        :return: None
        """
        self._canvas.delete('apple')
        x, y = self._apple_position
        if self._painted_apples < NUMBER_OF_APPLES:
            self._canvas.create_oval(x*SCALE, y*SCALE, x*SCALE+SHIFT, y*SCALE+SHIFT, fill=APPLE_COLOUR, tag='apple')
            self._painted_apples += 1

    def paint(self):
        """
        Prints field with apples and snake and creates buttons
        :return: None
        """
        self.paint_snake()
        self.paint_apple()
        root.mainloop()

    def start(self):
        """
        Starts and controls the game.

        Binds arrow buttons with canvas, randomly puts apple on the field,
        initiates snake movements, paints all on the window, asks user for snake movement direction
        """
        self._canvas.focus_set()
        self._canvas.bind('<Left>', lambda event: self._move_snake(LEFT))
        self._canvas.bind('<Right>', lambda event: self._move_snake(RIGHT))
        self._canvas.bind('<Up>', lambda event: self._move_snake(UP))
        self._canvas.bind('<Down>', lambda event: self._move_snake(DOWN))
        self.put_apple()
        self._after_id.append(self._canvas.after(SNAKE_SPEED, self._move_snake, RIGHT))
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