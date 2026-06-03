class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = []

        for number in nums:
            if number in seen:
                if number not in duplicates:
                    duplicates.append(number)
            else:
                seen.add(number)

        if len(duplicates) > 0:
            return True

        return False