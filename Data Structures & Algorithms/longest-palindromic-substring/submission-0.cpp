class Solution {
public:
    string longestPalindrome(string s) {
        int len=s.size();
        int max_length=1;
        int max_left=0;
        int max_right=0;
        for(int i=0;i<s.size();i++)
        {
            int left=i-1;
            int right=i+1;
            int curr_length=1;
            while(left>=0 && right<len)
            {
                if(s[left]==s[right])
                {
                    curr_length++;
                    curr_length++;
                    left--;
                    right++;
                }
                else
                {
                    break;
                }
            }
            if(curr_length>max_length)
            {
                max_length=curr_length;
                
                    max_left=left+1;
                    max_right=right-1;
                
            }
            left=i;
            right=i+1;
            curr_length=0;
            while(left>=0 && right<len)
            {
                if(s[left]==s[right])
                {
                    curr_length++;
                    curr_length++;
                    left--;
                    right++;
                }
                else
                {
                    break;
                }
            }
            if(curr_length>max_length)
            {
                max_length=curr_length;
                
                    max_left=left+1;
                    max_right=right-1;
                
            }

        }
        return s.substr(max_left,(max_right-max_left+1));
    }
};
