class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newArr = []

        for i in range(len(nums)):
            if nums[i] not in newArr:
                newArr.append(nums[i])
        
        if len(nums) > len(newArr):
            return True
        return False