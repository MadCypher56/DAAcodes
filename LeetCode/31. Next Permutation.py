class Solution:
    def is_decrement(self, nums: List[int]) -> bool:
        return all(nums[i] >= nums[i+1] for i in range(len(nums)-1))

    def nextPermutation(self, nums: List[int]) -> None:
        if self.is_decrement(nums):
            nums.sort()
            return
        
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i-=1
        
        if i>=0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j-=1
            nums[j], nums[i] = nums[i], nums[j]
        
        nums[i+1:] = reversed(nums[i+1:])
