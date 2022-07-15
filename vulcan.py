from re import I


class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff not in dict:
                dict[nums[index]] = index
            else:
                return [dict[diff], index]

print(Solution().twoSum([2,7,11,15],13))

