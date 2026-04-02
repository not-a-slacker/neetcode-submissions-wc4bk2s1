class Solution {
public:
    int rob(vector<int>& nums) {
        int m=nums.size();
        int dp[m][2];
        dp[0][0]=0;
        dp[0][1]=nums[0];
        dp[1][0]=nums[0];
        dp[1][1]=max(nums[0],nums[1]);
        for(int i=2;i<m;i++)
        {
            dp[i][0]=dp[i-1][1];
            dp[i][1]=max((dp[i-1][0]+nums[i]),dp[i-2][0]+nums[i]);
        }
        return max(dp[m-1][0],dp[m-1][1]);

    }
};
