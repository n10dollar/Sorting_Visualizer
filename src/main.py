import tkinter as tk
import algorithms as al
import random

window = tk.Tk()

width, height = 800, 800
window.geometry(str(width) + "x" + str(height))

window.title("Sorting Visualizer")

window.iconbitmap()

canvas = tk.Canvas(window, bg="white", height=height, width=width)

label = tk.Label(text="Label!")

# label.pack()


# __________________

x_base = 100


class Bar:
    index = None
    height = None
    color = None

    width = 50
    x_base = x_base
    y_base = 300

    def __init__(self, index, height, color):
        self.index = index
        self.height = height
        self.color = color

    def __repr__(self):
        return f"{self.index}: {self.height}"

    def draw(self, canvas):
        # bar_coords = [bar_x + bar_width * (i - 1), bar_y, bar_x + bar_width * i,
        #               bar_y + random.randrange(bar_height // 10, bar_height)]
        top_left_x = self.x_base + self.index * self.width
        top_left_y = self.y_base - self.height
        bottom_right_x = self.x_base + (self.index + 1) * self.width
        bottom_right_y = self.y_base

        bar_coords = [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        canvas.create_rectangle(bar_coords, fill=self.color)

    def get_height(self):
        return self.height

    def set_index(self, index):
        self.index = index


# __________________

colors = ["red", "green", "blue", "cyan", "magenta", "orange"]
bars = []

for i in range(6):
    bars.append(Bar(i, random.randrange(0, 250),
                    colors[random.randrange(0, len(colors))]
                    ))


def update():
    for index in range(len(bars)):
        bars[index].set_index(index)
        bars[index].draw(canvas)
    canvas.pack()
    window.mainloop()


# update()

print(bars)
al.insertion_sort(bars)
print(bars)

# x_base *= 5
update()

"""
bar_width, bar_height = 10, 300
bar_x, bar_y = 60, 30
bar_coords = [bar_x, bar_y, bar_x + bar_width, bar_y]

bar_count = 10
for i in range(1, bar_count + 1):
    bar_coords = [bar_x + bar_width * (i - 1), bar_y, bar_x + bar_width * i,
                  bar_y + random.randrange(bar_height // 10, bar_height)]
    # bar_height * i
    # [bar_x * i, bar_y, bar_x + bar_width * i, bar_y + bar_height * i]
    canvas.create_rectangle(bar_coords, fill="red")
canvas.pack()

window.mainloop()

"""

# __________________


# li = random.sample(range(0, 30), 8)
# print(li)
# al.insertion_sort(li, 0)
# print(li)

# li_2 = random.sample(range(0, 30), 8)
# li_2 = al.merge_sort(li_2)
# print(li_2)
