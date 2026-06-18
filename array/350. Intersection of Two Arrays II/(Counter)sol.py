from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time Complexity: O(n + m)
        Space Complexity: O(n)
        """

        # Create frequency map of nums1
        count = Counter(nums1)

        result = []

        # Check elements in nums2
        for num in nums2:

            if count[num] > 0:
                result.append(num)

                # Use one occurrence
                count[num] -= 1

        return result
