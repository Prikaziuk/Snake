#!/usr/bin/env python3

import tkinter as tk
import time
root = tk.Tk()

canvas = tk.Canvas(root, width=100, height=100, bg="green")
x = 0
y = 0

#canvas.pack()

canvas.focus_set()
canvas.bind("a", lambda event: print ('asd'))
canvas.pack()


root.mainloop()

"""

def level():

    canvas = tk.Canvas(root, width=100, height=100, bg="yellow")
    canvas.pack()
    var = tk.IntVar()
    tk.Label(canvas, text="Difficulty").pack()
    tk.Radiobutton(canvas, text="Easy", variable=var, value=[500, 5]).pack()
    tk.Radiobutton(canvas, text="Med", variable=var, value=[100, 15]).pack()
    tk.Radiobutton(canvas, text="Hard", variable=var, value=[100, 30], comand=print(var.get())).pack()
    canvas.create_text(10, 10, anchor="nw", text="Select difficulty")
    #canvas.destroy()
"""