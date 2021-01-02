# This is the implementation of insertion sort
from Sorting.utils import exectime, generate_random_list, swap


@exectime
def insertion_sort(arr: [int]):
    size = len(arr)

    for i in range(size - 1):
        for j in range(i + 1, 1, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)


if __name__ == "__main__":
    a = generate_random_list(0, 10000, 1000)
    insertion_sort(a)
