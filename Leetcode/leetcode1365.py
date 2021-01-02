import collections


# First, counts frequency of each number, and sort by this frequency
# second, calculate cumulative sum of this sorted frequency
def smaller_numbers_than_current(nums: [int]):
    frequency = collections.Counter(nums)
    sorted_frequency = sorted(frequency.items())
    ans = {}
    acc = 0
    for k, c in sorted_frequency:
        ans[k] = acc
        acc += c

    return [ans[n] for n in nums]


if __name__ == "__main__":
    case = [7,7,7,7]

    print(smaller_numbers_than_current(case))