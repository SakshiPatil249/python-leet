class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        Remove duplicates from a sorted array in-place.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Edge case
        if not nums:
            return 0

        # Points to position where next unique element
        # should be placed
        write = 1

        # Start from second element
        for read in range(1, len(nums)):

            # Found a new unique element
            if nums[read] != nums[read - 1]:

                nums[write] = nums[read]
                write += 1

        return write
