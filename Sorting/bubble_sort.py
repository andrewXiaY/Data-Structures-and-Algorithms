# Implementation of bubble sort
from Sorting.utils import swap, generate_random_list, exectime


# 把当前最小值移到当前最前面
# 关键点：从后往前比较并交换，当前最小值一定会一直往前交换
@exectime
def bubble_sort(arr: [int]) -> None:
    size = len(arr)
    for i in range(size):
        for j in range(size - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)


@exectime
def bubble_sort_improved(arr: [int]):
    size = len(arr)
    for i in range(size):
        not_finished = False
        for j in range(size - 1, i, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)
                not_finished = True

        if not not_finished:
            break


if __name__ == "__main__":

    a = generate_random_list(0, 1000000, 1000)
    # b = generate_random_list(0, 1000000, 1000)
    bubble_sort(a)
    # bubble_sort_improved(b)

    print(a)
    # print(b)
    """
    当list大小10000时，bubble sort运行时间 19s， bubble sort improved运行时间 17s。
    list大小较小时不会有显著改善，并且因为增加了条件判断，运行时间可能更长
    """
