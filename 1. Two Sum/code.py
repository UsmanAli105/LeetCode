class Solution(object):
    def twoSum(self, nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if (x != y):
                    if (nums[x]+nums[y]) == target:
                        return x,y
        return -1,-1