class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for merged array

        # Merge nums1 and nums2 from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements from nums2 to nums1 (only if nums2 has remaining elements)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
