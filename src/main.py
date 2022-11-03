import tkinter as tk
import algorithms as al
import utils as ut
import random as rd

window = tk.Tk()

width, height = 800, 800
window.geometry(f"{width}x{height}")

window.title("Sorting Visualizer")
canvas = tk.Canvas(window, bg="white", height=height, width=width)
# window.iconbitmap()

x_base = width * .1
y_base = height * .9

# __________________

# colors = ["red", "green", "blue", "cyan", "magenta", "orange"]
colors = ["red", "green", "blue"]
bars = []

for i in range(20):
    bars.append(ut.Bar(x_base, y_base,
                       rd.randrange(0, 500),
                       colors[rd.randrange(0, len(colors))]
                       ))

# update()

print(bars)
# bars = al.quick_sort(bars)
# al.bubble_sort(bars)
# print(bars)

al.heap_sort(bars)

for i in range(len(bars)):
    bars[i].draw(i, canvas)

print(bars)

canvas.pack()
window.mainloop()
