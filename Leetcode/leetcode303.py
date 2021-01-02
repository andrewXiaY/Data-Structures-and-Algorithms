# Range sum query

# Implement the NumArray class:
# 1. NumArray(int[] nums) Initializes the object with the integer array nums.
# 2. Int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j]
#    inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))


# just calculated the accumulative sum and then use acc_sum[j] - acc_sum[i - 1]
# initialize the accumulative sum array by 0 with length len(nums) + 1


# it is very easy, so do not show the answer here