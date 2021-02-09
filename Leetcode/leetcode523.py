"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous
subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

"""

"""
思路：congruence modulo

reference: https://leetcode.com/problems/continuous-subarray-sum/solution/

we can define a "group" relationship on the integers 
(refer: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo)
if the results of two integers i1 and i2 modulo k are the same, then we can say they are in the same group
e.g. 7 % 13 = 7 and 46 % 13 = 7, so we can think of 7 and 46 are in the same group
we can name the group using the result of modulo
if we know two integers i1 and i2 are in the same group d, then we have:
i1 = 13 * a + d and i2 = 13 * b + d where a and b are both integers
if then we calculate their difference, we can get:
i1 - i2 = 13 * a - 13 * b + d - d = 13 * (a - b)
since a and b are both integers, (a - b) must be integers as well

Conclusion: if two integers are in the same group, their difference must be divisible by the divisor k
Now back to prefix sum, if we know that the difference of two prefix sum is divisible by k, then we 
can learn that sum of the subarray corresponds to this difference must be divisible by k (aka, it is 
multiple of k
"""


def solve(nums, k):
    rem = {0: -1}
    sums = 0
    for i, c in enumerate(nums):
        sums += c
        if k != 0:
            sums = sums % k

        if sums in rem:
            if i - rem[sums] > 1:
                return True
        else:
            rem[sums] = i
    return False
