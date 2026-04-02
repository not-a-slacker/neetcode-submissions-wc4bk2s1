class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,vector<int>> nums_map;
        for(int i=0;i<nums.size();i++)
        {
            nums_map[nums[i]].push_back(i);
        }
        for(int i=0;i<nums.size();i++)
        {

            if(nums_map.count(target-nums[i])==1)
            {
                if(target-nums[i]==nums[i])
                {
                    if(nums_map[target-nums[i]].size()>1)
                    {
                        vector<int> ans;
                        ans.push_back(i);
                        ans.push_back(nums_map[target-nums[i]][1]);
                        return ans;
                    }
                    else
                    {
                        continue;
                    }
                }
                vector<int> ans;
                ans.push_back(i);
                ans.push_back(nums_map[target-nums[i]][0]);
                return ans;
            }
        }
    }
};
