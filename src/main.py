import tkinter as tk
import algorithms as al
import random

window = tk.Tk()

width, height = 500, 500
window.geometry(str(width) + "x" + str(height))

window.title("Sorting Visualizer")

window.iconbitmap()

canvas = tk.Canvas(window, bg="white", height=height, width=width)

label = tk.Label(text="Label!")
# label.pack()


# __________________

"""

bar_width, bar_height = 10, 300
bar_x, bar_y = 60, 30
bar_coords = [bar_x, bar_y, bar_x + bar_width, bar_y]

bar_count = 10
for i in range(1, bar_count + 1):
    bar_coords = [bar_x + bar_width * (i - 1), bar_y, bar_x + bar_width * i, bar_y + random.randrange(bar_height // 10, bar_height)]
    # bar_height * i
    # [bar_x * i, bar_y, bar_x + bar_width * i, bar_y + bar_height * i]
    canvas.create_rectangle(bar_coords, fill="red")
canvas.pack()

window.mainloop()

"""

# __________________

li = random.sample(range(0, 30), 8)
print(li)
al.insertion_sort(li, 0)
print(li)
