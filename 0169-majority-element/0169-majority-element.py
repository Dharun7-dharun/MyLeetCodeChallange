class Solution(object):
    def majorityElement(self, nums):
        count=0
        temp=0
        for a in nums:
            if count==0:
                temp=a
            
            if a==temp:
                count+=1

            else:
                count-=1
        return temp

        