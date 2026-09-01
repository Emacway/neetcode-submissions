class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans = nums;
        ans.resize(nums.size()*2);
        for(int i = 0; i < nums.size(); i++){
            ans[i + nums.size()] = nums[i];
        }
        return ans;
    }
};