class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
            # Perform bubble sort for the given array
        for i in range(n):
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                 # Swap if the element found is greater than the next element
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        
