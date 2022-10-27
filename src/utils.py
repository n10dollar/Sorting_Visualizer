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

        bar_coords = [top_left_x, top_left_y, bottom_right_x, bottom_right_y]
        canvas.create_rectangle(bar_coords, fill=self.color)

    def get_height(self):
        return self.height


# __________________

def swap(bars: list, index1, index2):
    temp = bars[index1]
    bars[index1] = bars[index2]
    bars[index2] = temp


# __________________

def merge(sorted_bars_1: list, sorted_bars_2: list):
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
def sort_max_heap(bars_heap: list, index: int):
    if 2 * index >= len(bars_heap):
        return

    children_indices = [2 * index, 2 * index + 1]
    children_values = [bars_heap[2 * index].get_height(), bars_heap[2 * index + 1].get_height()]

    biggest_child_index = children_indices[children_values.index(max(children_values))]
    # print(biggest_child_index)

    if bars_heap[biggest_child_index].get_height() > bars_heap[index].get_height():
        swap(bars_heap, index, biggest_child_index)
        sort_max_heap(bars_heap, biggest_child_index)


def create_max_heap(bars: list):
    for index in range(len(bars) // 2, 0, -1):
        sort_max_heap(bars, index)









