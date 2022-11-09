import random as rd
import time


class Bar:
    width = 15

    def __init__(self, x_base, y_base, height, color):
        self.x_base = x_base
        self.y_base = y_base
        self.height = height
        self.color = color

    def __str__(self):
        return f"{self.height}"

    def __repr__(self):
        return self.__str__()

    def draw(self, index, canvas):
        top_left_x = self.x_base + index * self.width
        top_left_y = self.y_base - self.height
        bottom_right_x = self.x_base + (index + 1) * self.width
        bottom_right_y = self.y_base

        bar_coordinates = [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        canvas.create_rectangle(bar_coordinates, fill=self.color)

    def get_height(self):
        return self.height


def add_bars(bars: list, colors: list, heights: list, x_base, y_base):
    for i in heights:
        bars.append(Bar(x_base, y_base, i,
                        colors[rd.randrange(0, len(colors))]
                        ))


def add_randomized_bars(bars: list, colors: list, count, span, x_base, y_base):
    for i in range(count):
        bars.append(Bar(x_base, y_base,
                        rd.randrange(0, span),
                        colors[rd.randrange(0, len(colors))]
                        ))


def draw_bars(bars: list, canvas):
    for i in range(len(bars)):
        bars[i].draw(i, canvas)


# __________________


def update_bars(bars: list, frame, canvas):
    canvas.delete("all")
    draw_bars(bars, canvas)
    frame.update_idletasks()
    # frame.update()
    time.sleep(.001)


# __________________

def swap(bars: list, index1, index2):
    bars[index1], bars[index2] = bars[index2], bars[index1]


# __________________

def merge(sorted_bars_1: list, sorted_bars_2: list, frame, canvas, index_offset=0):
    combined = []
    i_bars_1 = 0
    i_bars_2 = 0

    while True:
        if i_bars_1 >= len(sorted_bars_1) or i_bars_2 >= len(sorted_bars_2):
            break

        if sorted_bars_1[i_bars_1].get_height() < sorted_bars_2[i_bars_2].get_height():
            combined.append(sorted_bars_1[i_bars_1])
            i_bars_1 += 1
        elif sorted_bars_1[i_bars_1].get_height() > sorted_bars_2[i_bars_2].get_height():
            combined.append(sorted_bars_2[i_bars_2])
            i_bars_2 += 1
        else:
            combined.append(sorted_bars_1[i_bars_1])
            combined.append(sorted_bars_2[i_bars_2])
            i_bars_1 += 1
            i_bars_2 += 1

        update_bars(combined, frame, canvas)

    combined.extend(sorted_bars_1[i_bars_1:])
    combined.extend(sorted_bars_2[i_bars_2:])

    return combined


# __________________

def determine_pivot(bars: list):
    v_1 = bars[0].get_height()
    v_2 = bars[-1].get_height()
    v_3 = bars[len(bars) // 2].get_height()

    avg = (v_1 + v_2 + v_3) // 3
    curr_ind = 0
    while avg != bars[curr_ind].get_height():
        if curr_ind == len(bars) - 1:
            return bars[len(bars) // 2]

        curr_ind += 1

    return bars[curr_ind]


# __________________

# assumes heap is already sorted except for the topmost element
# index * 2 = left child, index * 2 + 1 = right child
def sort_max_heap(bars_heap: list, heap_bottom: int, frame, canvas, index=0):
    # if children are greater than current node,
    # swap current node with the biggest child
    # then recur sort_max_heap
    if not (0 <= index <= heap_bottom):
        return
    if left_child(index) > heap_bottom:
        return
    if right_child(index) > heap_bottom:
        if bars_heap[left_child(index)].get_height() > bars_heap[index].get_height():
            swap(bars_heap, index, left_child(index))
        return

    update_bars(bars_heap, frame, canvas)
    # now left and right children both exist
    if bars_heap[index].get_height() >= bars_heap[left_child(index)].get_height() and \
            bars_heap[index].get_height() >= bars_heap[right_child(index)].get_height():
        return

    # now current bar must be than one child
    if bars_heap[left_child(index)].get_height() > bars_heap[right_child(index)].get_height():
        swap(bars_heap, index, left_child(index))
        sort_max_heap(bars_heap, heap_bottom, frame, canvas, left_child(index))
    else:
        swap(bars_heap, index, right_child(index))
        sort_max_heap(bars_heap, heap_bottom, frame, canvas, right_child(index))


def create_max_heap(bars: list, heap_bottom: int, frame, canvas):
    for index in range((heap_bottom + 1) // 2 - 1, -1, -1):
        sort_max_heap(bars, heap_bottom, frame, canvas, index)


def left_child(index: int):
    return (index + 1) * 2 - 1


def right_child(index: int):
    return (index + 1) * 2 + 1 - 1
