class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 in-place.

        Time Complexity: O(m + n)
        Space Complexity: O(1)

        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """

        # Pointer to last position of nums1
        p = m + n - 1

        # Convert counts into indices
        m = m - 1
        n = n - 1

        # Compare elements from the back
        while m >= 0 and n >= 0:

            if nums1[m] > nums2[n]:
                nums1[p] = nums1[m]
                m -= 1
            else:
                nums1[p] = nums2[n]
                n -= 1

            p -= 1

        # Copy remaining elements from nums2
        while n >= 0:
            nums1[p] = nums2[n]
            n -= 1
            p -= 1
