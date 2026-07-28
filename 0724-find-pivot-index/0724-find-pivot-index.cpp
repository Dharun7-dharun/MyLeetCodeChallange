class Solution {
public:
    int pivotIndex(vector<int>& arr) {

        for(int i=0;i<arr.size();i++){
            int left=0;
            int right=0;

            for(int j=0;j<i;j++){
                left=left+arr[j];
            }

            for(int j=i+1;j<arr.size();j++){
                right=right+arr[j];
            }

            if(left==right){
                return i;
            }

        }

        return -1;
    }
};