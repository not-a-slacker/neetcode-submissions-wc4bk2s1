class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int len=strs.size();
        unordered_map<string,vector<string>> words;
        for(int i=0;i<len;i++)
        {
            vector<int> freq(26,0);
            int word_len=strs[i].size();
            cout << "word_len" << word_len << "\n";
            for(int j=0;j<word_len;j++)
            {
                cout << strs[i][j]-'a';
                freq[strs[i][j]-'a']++;
            }
            cout << "\n";
            for(int k=0;k<26;k++)
            {
                cout << freq[k];
            }
            cout << "\n";
            string freq_str="";
            for(int k=0;k<26;k++)
            {
                freq_str+=char(freq[k]);
            }
            words[freq_str].push_back(strs[i]);
            
        }
        vector<vector<string>> ans;
        for(const auto& pair : words)
        {
            ans.push_back(pair.second);

        }
        return ans;
    }
};
