class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int,int> prev_nums;
        int max_len=0;
        for(int i=0;i<nums.size();i++)
        {
            prev_nums[nums[i]]=1;
        }
        int curr=0;
        int curr_idx=0;
        int curr_len=0;
        for(int i=0;i<nums.size();i++)
        {
            if(prev_nums.count(nums[i]-1))
            {
                continue;
            }
            curr = nums[i];
            while(prev_nums.count(curr))
            {
                curr_len++;
                max_len=max(curr_len,max_len);
                curr++;
            }
            curr_len=0;
        }
        return max_len;
    }
};
