import sys
import utils as ut


# ___INSERTION_SORT___

# in-place
def insertion_sort(bars: list, frame, canvas, index=0, descending=False):
    """
    data = [19, 20, 28, 10, 26, 16, 13, 7]
    insertion_sort(data, 0)
    >>> [7, 10, 13, 16, 19, 20, 26, 28]
    """
    # base case
    if index < 0 or index >= len(bars) - 1:
        return

    sys.setrecursionlimit(100_000)
    # recursive cases
    if bars[index].get_height() > bars[index + 1].get_height():
        ut.swap(bars, index, index + 1)
        ut.update_bars(bars, frame, canvas)
        insertion_sort(bars, frame, canvas, index - 1, True)

    if not descending:
        insertion_sort(bars, frame, canvas, index + 1)


# ___MERGE_SORT___

# non-in-place
def merge_sort(bars: list, frame, canvas, index_offset=0):
    if len(bars) == 1:
        return bars

    left_half = bars[:len(bars) // 2]
    right_half = bars[len(bars) // 2:]

    return ut.merge(merge_sort(left_half, frame, canvas, index_offset),
                    merge_sort(right_half, frame, canvas, index_offset + len(bars) // 2),
                    frame, canvas, index_offset)


# ___BUBBLE_SORT___

# in-place
def bubble_sort(bars: list, frame, canvas, sorted_bars=0):
    is_sorted = True

    for i in range(len(bars) - sorted_bars - 1):
        if bars[i].get_height() > bars[i + 1].get_height():
            ut.swap(bars, i, i + 1)
            ut.update_bars(bars, frame, canvas)
            is_sorted = False

    if not is_sorted:
        bubble_sort(bars, frame, canvas, sorted_bars + 1)


# ___QUICK_SORT___

# non-in-place
def quick_sort(bars: list, frame, canvas):
    if len(bars) == 1 or len(bars) == 0:
        return bars
    if len(bars) == 2:
        if bars[0].get_height() > bars[1].get_height():
            ut.swap(bars, 0, 1)
        return bars

    pivot = ut.determine_pivot(bars)

    bars.remove(pivot)
    bars.append(pivot)

    i_rightward = 0
    i_leftward = len(bars) - 2

    while i_rightward <= i_leftward:
        if bars[i_rightward].get_height() > bars[i_leftward].get_height():
            ut.swap(bars, i_rightward, i_leftward)

        if bars[i_rightward].get_height() <= pivot.get_height():
            i_rightward += 1
        if bars[i_leftward].get_height() >= pivot.get_height():
            i_leftward -= 1

    bars.remove(pivot)
    bars.insert(i_rightward, pivot)

    # ut.update_bars(bars, frame, canvas)
    bars = quick_sort(bars[:i_rightward], frame, canvas) + quick_sort(bars[i_rightward:], frame, canvas)
    ut.update_bars(bars, frame, canvas)
    return bars


# ___HEAP_SORT___

# ?-in-place
def heap_sort(bars: list, frame, canvas):
    for index in range(len(bars) - 1, 0, -1):
        ut.create_max_heap(bars, index, frame, canvas)
        ut.swap(bars, 0, index)
    ut.update_bars(bars, frame, canvas)

