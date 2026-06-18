class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        Time Complexity: O(n + m)
        Space Complexity: O(min(n, m))
        """

        freq = {}
        result = []

        # Count frequency of elements in nums1
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # Check elements in nums2
        for num in nums2:

            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1

        return result
