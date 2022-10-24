class Bar:
    width = 15

    def __init__(self, x_base, y_base, height, color):
        self.x_base = x_base
        self.y_base = y_base
        self.height = height
        self.color = color

    def __repr__(self):
        return f"{self.height}"

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

def swap(data: list, index1, index2):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp


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

def divide(data: list):
    pass
