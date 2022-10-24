import utils as ut


# ___INSERTION SORT___

# in-place
def insertion_sort(bars: list, index=0):
    """
    data = [19, 20, 28, 10, 26, 16, 13, 7]
    insertion_sort(data, 0)
    >>> [7, 10, 13, 16, 19, 20, 26, 28]
    """
    # base case
    if index < 0 or index >= len(bars) - 1:
        return

    # recursive cases
    if bars[index].get_height() > bars[index + 1].get_height():
        ut.swap(bars, index, index + 1)
        insertion_sort(bars, index - 1)

    insertion_sort(bars, index + 1)


# ___MERGE SORT___

# non-in-place
def merge_sort(bars: list):
    if len(bars) == 1:
        return bars

    left_half = bars[:len(bars) // 2]
    right_half = bars[len(bars) // 2:]

    return ut.merge(merge_sort(left_half), merge_sort(right_half))


# ___BUBBLE SORT___

# in-place
def bubble_sort(bars: list, sorted_bars=0):
    is_sorted = True

    for i in range(len(bars) - sorted_bars - 1):
        if bars[i].get_height() > bars[i + 1].get_height():
            ut.swap(bars, i, i + 1)
            is_sorted = False

    if not is_sorted:
        bubble_sort(bars, sorted_bars + 1)


# ___QUICK SORT___

# in-place
def quick_sort(bars: list):
    pivot = bars[len(bars) // 2]
    bars.pop(len(bars) // 2)
    bars.append(pivot)

    smaller_than_pivot = 0
    larger_than_pivot = 0

    ind_left = 0
    ind_right = len(bars) - 1

    while ind_left >= ind_right:
        if bars[ind_left].get_height() < pivot.get_height():
            ind_left += 1
        if bars[ind_right].get_height() >= pivot.get_height():
            ind_right += 1

