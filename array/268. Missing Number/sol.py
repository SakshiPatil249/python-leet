class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        n = len(nums)

        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Actual sum of array elements
        actual_sum = sum(nums)

        return expected_sum - actual_sum
