class Solution {
public:
    int maxArea(vector<int>& heights) {
        int len=heights.size();
        int max_area=(len-1)*min(heights[0],heights[len-1]);
        int left=0;
        int right=len-1;
        int curr_area;
        while(left<right)
        {
            curr_area=(right-left)*min(heights[left],heights[right]);
            if(curr_area>max_area)
            {
                max_area=curr_area;
            }
            if(heights[left]<=heights[right])
            {
                left++;
            }
            else
            {
                right--;
            }
            
        }
        return max_area;
    }
};
