class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> freq(2001,0);
        for(int i=0;i<nums.size();i++)
        {
            freq[nums[i]+1000]++;
        }
        vector<vector<int>> buckets(nums.size()+1);
        for(int i=0;i<2001;i++)
        {
            buckets[freq[i]].push_back(i-1000);
        }
        int count=k;
        vector<int> ans;
        for(int i=nums.size();i>=0 && count>0;i--)
        {
            while(buckets[i].size()!=0)
            {
                ans.push_back(buckets[i].back());
                buckets[i].pop_back();
                count--;
            }
        }
        return ans;
    }
};
