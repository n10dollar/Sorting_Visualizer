def insertion_sort(data: list, index: int):

    """

    data = [19, 20, 28, 10, 26, 16, 13, 7]
    insertion_sort(data, 0)
    >>> [7, 10, 13, 16, 19, 20, 26, 28]

    """

    # base case
    if index < 0 or index >= len(data) - 1:
        return

    # recursive cases
    if data[index] >= data[index + 1]:
        swap(data, index, index + 1)
        insertion_sort(data, index - 1)

    insertion_sort(data, index + 1)


# __HELPER_FUNCTIONS__

def swap(data: list, index1: int, index2: int):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp
