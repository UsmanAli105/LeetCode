def buildArray(nums: list[int]):
    q = len(nums)
    for i in range(len(nums)):
        r = nums[i]
        b = nums[nums[i]] % q
        nums[i] = q*b + r
    for i in range(len(nums)):
        nums[i] = nums[i] // q  
    return nums


arr = [2, 3, 4, 2, 1, 5]
print(buildArray(arr))