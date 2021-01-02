# Count number of teams
"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

1. Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
2. A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
   where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).
"""


# dynamic programing
# we iterate rating from back to front, and counts how many numbers are larger than current number and smaller than current number
# if rating[j] > rating[i], which means only ascending pattern can be valid here, so we add larger[j]
# (remember we iterate backwards, so larger[j] is determined)
# if rating[j] < rating[i], which means only descending pattern can be valid here, so we add smaller[j]
# (remember we iterate backwards, so smaller[j] is determined)
def solve(rating) -> int:
    size = len(rating)
    ans = 0
    larger = [0] * size
    smaller = [0] * size

    for i in range(size - 1, -1, -1):
        for j in range(i + 1, size):
            if rating[i] < rating[j]:
                larger[i] += 1
                ans += larger[j]
            else:
                smaller[i] += 1
                ans += smaller[j]
    return ans


if __name__ == "__main__":
    rating = [2,5,3,4,1]
    print(solve(rating))