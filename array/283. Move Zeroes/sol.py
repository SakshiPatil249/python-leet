class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Move all zeroes to the end while maintaining
        the relative order of non-zero elements.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Position where the next non-zero element
        # should be placed
        write = 0

        # Traverse the entire array
        for read in range(len(nums)):

            # If current element is non-zero
            if nums[read] != 0:

                # Swap current non-zero element
                # with the write position
                nums[write], nums[read] = nums[read], nums[write]

                # Move write pointer forward
                write += 1
