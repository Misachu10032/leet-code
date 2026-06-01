class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        valid_index=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[valid_index]=nums[i]
                valid_index +=1
        
        return valid_index