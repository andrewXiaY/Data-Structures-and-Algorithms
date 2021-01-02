from Sorting.utils import exectime, generate_random_list, is_sorted


def merge_array(arr1: [int], arr2: [int]) -> [int]:
    index_arr1 = index_arr2 = 0
    ret = []

    while index_arr1 < len(arr1) and index_arr2 < len(arr2):
        if arr1[index_arr1] < arr2[index_arr2]:
            ret.append(arr1[index_arr1])
            index_arr1 += 1
        else:
            ret.append(arr2[index_arr2])
            index_arr2 += 1

    if index_arr1 < len(arr1):
        ret.extend(arr1[index_arr1:])

    if index_arr2 < len(arr2):
        ret.extend(arr2[index_arr2:])

    return ret


def _merge_sort(arr: [int], left: int, right: int) -> [int]:

    if left == right:
        return arr[left: left + 1]

    mid = (left + right) // 2

    half_left = _merge_sort(arr, left, mid)
    half_right = _merge_sort(arr, mid + 1, right)

    return merge_array(half_left, half_right)


@exectime
def merge_sort(arr: [int]):
    return _merge_sort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    a = generate_random_list(0, 100000, 1000000)
    a = merge_sort(a)
    print(is_sorted(a))