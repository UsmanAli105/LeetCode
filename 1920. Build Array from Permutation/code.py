class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        ans = []
        q = len(nums)
        for i in range(len(nums)):
            ans.append(nums[nums[i]] % q)
        return ans
            

obj = Solution()
arr = [2, 3, 4, 2, 1, 5]
print(obj.buildArray(arr))