class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> seenBefore;
        for (int i = 0; i < nums.size(); i++){
            if(seenBefore.contains(nums[i])){
                return true;
            }
            else{
                seenBefore.insert(nums[i]);
            }
        }
        return false;
    }
};