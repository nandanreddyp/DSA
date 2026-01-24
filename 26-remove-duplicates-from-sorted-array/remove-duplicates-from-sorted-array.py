class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0; last_seen = None
        for i in range(len(nums)):
            if last_seen != nums[i]:
                nums[k] = nums[i]
                last_seen = nums[i]; k+=1
        return k