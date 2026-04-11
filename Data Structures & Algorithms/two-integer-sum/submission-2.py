class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # The brute-force approach:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # THE OPTIMIZED VERSION - HASHTABLE

        nums_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_dict:
                return [nums_dict[diff], i]
            else:
                nums_dict[num] = i