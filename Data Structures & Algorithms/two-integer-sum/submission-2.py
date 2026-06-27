class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}

        for i, num in enumerate(nums):
            indices[num] = i

        for i, nums in enumerate(nums):
            diff = target - nums
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []            