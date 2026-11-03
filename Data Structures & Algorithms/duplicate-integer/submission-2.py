class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = set()
        for i in nums:
            new_nums.add(i)
        if len(new_nums) != len(nums):
            return True 
        return False

        