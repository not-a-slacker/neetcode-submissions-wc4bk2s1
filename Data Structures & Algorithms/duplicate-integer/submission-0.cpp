class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> nums_map;
        for(int i=0;i<nums.size();i++)
        {
            if(nums_map.count(nums[i])==1)
            {
                return true;
            }
            nums_map[nums[i]]=1;
        }
        return  false;
    }
};
