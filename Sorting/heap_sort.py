# This is the implementation of heap sort
from Sorting.utils import generate_random_list, exectime, swap, is_sorted


# Parameter "end" is used to control the size of heap
# because we sort array using max heap, each time we move the maximum value
# to the tail of the array, at the same time we should shrink the size of remain heap by 1,
# which means we pass the iteration index of heap sort function as the "end" parameter of "max heapify"
def max_heapify(arr: [int], pos: int, end: int):
    left = 2 * pos + 1  # 左子节点
    right = 2 * pos + 2  # 右子节点

    max_index = pos

    if left < end and arr[max_index] < arr[left]:
        max_index = left
    if right < end and arr[max_index] < arr[right]:
        max_index = right

    if max_index != pos:
        swap(arr, pos, max_index)
        max_heapify(arr, max_index, end)


def make_max_heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))


@exectime
def heap_sort(arr: [int]):
    make_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, 0, i)
        max_heapify(arr, 0, i)


if __name__ == '__main__':
    a = generate_random_list(0, 1000000, 1000000)
    heap_sort(a)
    print(is_sorted(a))