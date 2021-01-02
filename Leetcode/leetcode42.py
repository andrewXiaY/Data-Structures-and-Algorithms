# trap water
# 对于每个点，找到这个点左边最高的点以及右边最高的点，取其中最小值，然后减去当前高度即为可以存储的水量


# 方法1，使用两个列表记录每个点左边和右边的最大值
def trap_water(arr):
    if not arr:
        return 0

    size = len(arr)
    left_max = [0] * size
    right_max = [0] * size

    left_max[0] = arr[0]
    right_max[-1] = arr[-1]

    for i in range(1, size):
        left_max[i] = max(arr[i], left_max[i - 1])

    for i in range(size - 2, -1, -1):
        right_max[i] = max(arr[i], right_max[i + 1])

    ans = 0
    for i in range(size):
        ans += min(left_max[i], right_max[i]) - arr[i]

    return ans


# 方法2，使用两个pointer来指定最大高度
def trap_water_2pointers(arr):
    if not arr:
        return 0

    left, right = 0, len(arr) - 1
    left_max, right_max = 0, 0
    ans = 0
    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                ans += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                ans += right_max - arr[right]
            right -= 1

    return ans


if __name__ == '__main__':
    case1 = [4,2,0,3,2,5]
    print(trap_water(case1))  # answer should be 9

    case2 = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_water(case2))  # answer should be 6

    print(trap_water_2pointers(case1))
    print(trap_water_2pointers(case2))