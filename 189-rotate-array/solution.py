class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = rotated[i]
            
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(l,r):
            while l <r:
                nums[l],nums[r]=nums[r],nums[l]
                l +=1
                r -=1

        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:k], nums[k:] = nums[-k:], nums[:-k]