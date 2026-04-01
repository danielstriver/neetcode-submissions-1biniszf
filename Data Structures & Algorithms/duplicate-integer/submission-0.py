from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = Counter(nums)

        for number, count in nums_dict.items():
            if count > 1:
                return True
        return False