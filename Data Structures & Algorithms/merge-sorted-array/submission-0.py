class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # INTUITION
        # Copying elements of nums2 into the empty spots in nums1

        nums1[m:] = nums2[:n]
        nums1.sort()
        