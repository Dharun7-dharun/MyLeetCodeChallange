class Solution(object):
    def containsDuplicate(self, nums):
        arr=set()
        for i in range(len(nums)):
            if nums[i] in arr:
                return True

            arr.add(nums[i])

        return False
            

            
        