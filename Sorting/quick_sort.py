# This is the implementation of quick sort
from Sorting.utils import generate_random_list, exectime


# 快排相当于找一个pivot，然后把所有小于pivot的数全部放到前面，把所有大于pivot的数全部放到后面
def place_pivot(arr: [int], left: int, right: int) -> int:
    key = arr[left]
    while left < right:
        # 找到右边第一个小于key的数
        while left < right and arr[right] >= key:
            right -= 1

        if left < right:
            arr[left] = arr[right]
            left += 1

        # 找到左边第一个大于key的数
        while left < right and arr[left] < key:
            left += 1

        if left < right:
            arr[right] = arr[left]
            right -= 1

    arr[left] = key
    return left


# 假设我们把数组第一个数当成pivot
def run_sort(arr: [int], left: int, right: int) -> None:

    if left < right:
        pivot_index = place_pivot(arr, left, right)
        run_sort(arr, left, pivot_index - 1)
        run_sort(arr, pivot_index + 1, right)


@exectime
def quick_sort(arr: [int]) -> None:
    run_sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    a = generate_random_list(0, 1000000, 1000000)
    quick_sort(a)
