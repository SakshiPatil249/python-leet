class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """

        # Convert arrays into sets
        set1 = set(nums1)
        set2 = set(nums2)

        # Find common unique elements
        return list(set1 & set2)
