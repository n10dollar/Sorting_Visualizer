import tkinter as tk
from PIL import Image, ImageTk
import algorithms as al
import utils as ut

root = tk.Tk()
width, height = 1600, 800
root.geometry(f"{width}x{height}")
root.title("Sorting Visualizer")
ico = Image.open('res/Sauron_Colorful.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

bars = []
bar_count = 100
bar_height = 500
x_base = 5
y_base = height * .9

def l1():
    global bars
    bars = []
    ut.add_randomized_bars(bars, ["red", "green"], bar_count, bar_height, x_base, y_base)
    ut.update_bars(bars, frame, canvas)
l2 = lambda: al.insertion_sort(bars, frame, canvas)

frame = tk.Frame(root, width=width, height=height, bg="grey")
canvas = tk.Canvas(frame, bg="white", height=.9 * height, width=.95 * width)
generate = tk.Button(frame, text="Generate", command=l1, bg='red')  # error here
sort = tk.Button(frame, text="Sort", command=l2, bg='red')
close = tk.Button(frame, text="Close", command=root.destroy, bg='red')

frame.grid(row=0, column=0, padx=5, pady=5)
canvas.grid(row=1, column=0, columnspan=999, padx=5, pady=5)
generate.grid(row=0, column=1, padx=5, pady=5)
sort.grid(row=0, column=2, padx=5, pady=5)
close.grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
