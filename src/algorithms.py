import utils as ut


# ___INSERTION SORT___
def insertion_sort(data: list, index=0):
    """
    data = [19, 20, 28, 10, 26, 16, 13, 7]
    insertion_sort(data, 0)
    >>> [7, 10, 13, 16, 19, 20, 26, 28]
    """
    # base case
    if index < 0 or index >= len(data) - 1:
        return

    # recursive cases
    if data[index].get_height() > data[index + 1].get_height():
        ut.swap(data, index, index + 1)
        insertion_sort(data, index - 1)

    insertion_sort(data, index + 1)


# ___MERGE SORT___

def merge_sort(data: list):
    if len(data) == 1:
        return data

    left_half = data[:len(data) // 2]
    right_half = data[len(data) // 2:]

    return ut.merge(merge_sort(left_half), merge_sort(right_half))



