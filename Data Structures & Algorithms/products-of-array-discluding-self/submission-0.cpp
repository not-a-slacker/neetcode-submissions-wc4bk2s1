class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len=nums.size();
        vector<int> prefix;
        prefix.push_back(1);
        vector<int> suffix(len);
        suffix[len-1]=1;
        int prod;
        for(int i=0;i<len-1;i++)
        {
            prod=prefix.back()*nums[i];
            prefix.push_back(prod);
        }
        for(int i=len-1;i>0;i--)
        {
            suffix[i-1]=suffix[i]*nums[i];
        }
        vector<int> ans(len);
        for(int i=0;i<len;i++)
        {
            ans[i]=prefix[i]*suffix[i];
        }
        return ans;

    }
};
