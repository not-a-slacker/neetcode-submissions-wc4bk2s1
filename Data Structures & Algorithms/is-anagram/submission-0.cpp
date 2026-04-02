class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_map[26];
        for(int i=0;i<26;i++)
        {
            s_map[i]=0;
        }
        int t_map[26];
        for(int i=0;i<26;i++)
        {
            t_map[i]=0;
        }
        for(int i=0;i<s.size();i++)
        {
            s_map[s[i]-'a']++;
        }
        for(int i=0;i<t.size();i++)
        {
            t_map[t[i]-'a']++;
        }
        for(int i=0;i<26;i++)
        {
            if(s_map[i]!=t_map[i])
            {
                return false;
            }
        }
        return true;
    }
};
