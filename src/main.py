import tkinter as tk
import algorithms as al
import utils as ut

root = tk.Tk()
width, height = 800, 800
root.geometry(f"{width}x{height}")
root.title("Sorting Visualizer")
canvas = tk.Canvas(root, bg="white", height=height, width=width)
canvas.grid(row=1, column=0, padx=10, pady=5)

x_base = width * .1
y_base = height * .9

frame = tk.Frame(root, width=.8 * width, height=.8 * height, bg="grey")
frame.grid(row=0, column=0, padx=10, pady=5)

bars = []
ut.add_randomized_bars(bars, ["red", "green", "blue"], 15, 500, x_base, y_base)

l1 = lambda: ut.draw_bars(bars, canvas)
tk.Button(frame, text="Generate", command=l1, bg='red').grid(row=0, column=1, padx=5, pady=5)

l2 = lambda: al.quick_sort(bars, frame, canvas)
tk.Button(frame, text="Sort", command=l2, bg='red').grid(row=0, column=2, padx=5, pady=5)

# canvas.pack()
root.mainloop()