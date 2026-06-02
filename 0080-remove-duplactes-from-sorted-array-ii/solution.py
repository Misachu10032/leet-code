class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictionary=dict()

        k=0
        for i in range(1,len(nums)):
            if nums[i] > nums[k]:
                dictionary[nums[i]]=1
                k +=1
                nums[k]=nums[i]
            else:
                if nums[i] == nums[k]:
                    if nums[i] not in dictionary or dictionary[nums[i]] ==1:
                        dictionary[nums[i]]=2
                        k +=1
                        nums[k]= nums[i]
        return k+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        occurence=1

        k=0
        for i in range(1,len(nums)):
            if nums[i] > nums[k]:
                occurence=1
                k +=1
                nums[k]=nums[i]
            elif nums[i] == nums[k]:
                if occurence ==1:
                    k +=1
                    nums[k] = nums[i]
                    occurence=2
            

                
        return k+1