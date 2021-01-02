# This is the implementation of selection sort
from Sorting.utils import exectime, generate_random_list, swap


@exectime
def selection_sort(arr: [int]) -> None:
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i :
            swap(arr, min_index, i)


if __name__ == "__main__":
    a = generate_random_list(0, 100000, 10000)
    selection_sort(a)

    """
    同样10000个数据，冒泡排序16~19s，但是选择排序只需要5秒？当数据量不是很大的时候，swap的次数对运行时间又很大的影响
    """