def insertion_sort(data: list, index: int):
    if index < 0 or index >= len(data) - 1:
        return

    if data[index] >= data[index + 1]:
        swap(data, index, index + 1)
        insertion_sort(data, index - 1)

    insertion_sort(data, index + 1)


# __HELPER_FUNCTIONS__

def swap(data: list, index1: int, index2: int):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp
