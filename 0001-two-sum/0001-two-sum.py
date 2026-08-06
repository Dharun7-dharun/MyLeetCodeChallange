class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        


#         class Solution {
# public:
#     vector<int> twoSum(vector<int>& nums, int target) {
#         for(int i=0;i<nums.size();i++){
#             for(int j=i+1;j<nums.size();j++){
#                 if(nums[i]+nums[j]==target)
#                     return {i,j};
#             }
#         }
        
#         return {};
#     }
    
# };



