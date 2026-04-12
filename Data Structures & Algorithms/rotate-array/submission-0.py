class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Handling cases where k is larger than the length of the arr
        n = len(nums)
        k %= n

        # Repeat k times, store the last element in a temp var, shift all elements one position to the right, 
        # place the saved element at index 0

        while k:
            temp = nums[n - 1]
            for i in range(n - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp
            k -= 1
        