class Solution:
    def removeElement(self, nums, val):
        """
        Remove all occurrences of val in-place.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Position where next valid element should be placed
        write = 0

        # Traverse the array
        for read in range(len(nums)):

            # Keep only elements not equal to val
            if nums[read] != val:

                # Move valid element forward
                nums[write] = nums[read]

                # Move write pointer
                write += 1

        # Number of valid elements
        return write
