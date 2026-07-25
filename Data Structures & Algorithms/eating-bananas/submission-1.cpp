using namespace std;
class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int min = *min_element(piles.begin(),piles.end());
        int max = *max_element(piles.begin(),piles.end());
        int l = 1;
        int r = max;
        int curr = 1000000001;
        while (l<r)
        {
            int mid = (r+l) / 2;
            int time = 0;
            for(auto i : piles)
            {
                time = time + int(i/mid);
                if (i%mid != 0)
                {
                    time++;
                }
            }
            if (time<=h)
            {
                r = mid-1;
                if (mid<curr)
                {
                    curr=mid;
                }
                continue;
            }
            if (time>h)
            {
                l = mid+1;
                continue;
            }
        }
        if (l==r)
        {
            int time = 0;
            for(auto i : piles)
            {
                time = time + int(i/r);
                if (i%r != 0)
                {
                    time++;
                }
            }
            if (time<=h && l < curr)
            {
                curr = l;
            }
        }
        return curr;

        
    }
};
