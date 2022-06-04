# https://leetcode.com/problems/two-sum/
# TC: O(n)
# SC: O(n)
def twoSum(nums, target):
    f_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in f_dict:
            return [f_dict[complement],i]
        else:
            f_dict[nums[i]] = i

nums = [2,3,5,9,11,13]
target = 20
twoSum = twoSum(nums,target)
print(twoSum)
