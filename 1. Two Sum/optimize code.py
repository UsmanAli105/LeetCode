class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in dic:
                return [i, dic[r]]
            else:
                dic[j] = i