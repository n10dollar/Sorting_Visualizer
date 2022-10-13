# ___INSERTION SORT___
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


def swap(data: list, index1: int, index2: int):
    temp = data[index1]
    data[index1] = data[index2]
    data[index2] = temp


# ___MERGE SORT___

def merge_sort(data: list):
    if len(data) == 1:
        return data

    left_half = data[:len(data) // 2]
    right_half = data[len(data) // 2:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(sorted_1: list, sorted_2: list):
    combined = []
    index_sorted_1 = 0
    index_sorted_2 = 0

    while True:
        if index_sorted_1 >= len(sorted_1) or index_sorted_2 >= len(sorted_2):
            break

        if sorted_1[index_sorted_1] < sorted_2[index_sorted_2]:
            combined.append(sorted_1[index_sorted_1])
            index_sorted_1 += 1
        elif sorted_1[index_sorted_1] > sorted_2[index_sorted_2]:
            combined.append(sorted_2[index_sorted_2])
            index_sorted_2 += 1
        else:
            combined.append(sorted_1[index_sorted_1])
            combined.append(sorted_2[index_sorted_2])
            index_sorted_1 += 1
            index_sorted_2 += 1

    combined.extend(sorted_1[index_sorted_1:])
    combined.extend(sorted_2[index_sorted_2:])

    return combined
