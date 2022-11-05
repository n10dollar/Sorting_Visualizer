import tkinter as tk
import algorithms as al
import utils as ut

frame = tk.Tk()
width, height = 800, 800
frame.geometry(f"{width}x{height}")
frame.title("Sorting Visualizer")
canvas = tk.Canvas(frame, bg="white", height=height, width=width)

x_base = width * .1
y_base = height * .9

bars = []
ut.add_randomized_bars(bars, ["red", "green", "blue"], 15, 500, x_base, y_base)

al.heap_sort(frame, bars, canvas)
# ut.draw_bars(bars, canvas)

# canvas.pack()
# frame.mainloop()