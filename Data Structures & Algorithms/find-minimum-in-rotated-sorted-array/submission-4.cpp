class Solution {
public:
    int findMin(vector<int> &nums) {
        int n = nums.size();
        int l= 0;
        int r = n-1;
        if (nums[l] < nums[r] )
        {
            return nums[l];
        }
        int mini = nums[0];
        while(l<=r)
        {
            cout << "l : " << l << " ; r : " << r << "\n";
            if (l==r)
            {
                mini = min(mini,nums[l]);
                return mini;
            }
            if (nums[l] < nums[r])
            {
                return nums[l];
            }
            int mid = (r+l)/2;
            mini = min(mini,nums[mid]);
            if (nums[l] <= nums[mid])
            {
                l = mid+1;
                continue;
            }
            else
            {
                r = mid;
                continue;
            }
        }
        return mini;

        
    }
};
