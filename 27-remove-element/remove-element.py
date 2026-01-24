class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = -1
        for i in range(len(nums)):
            if nums[i] != val:
                k+=1
                nums[k] = nums[i]
        return k+1