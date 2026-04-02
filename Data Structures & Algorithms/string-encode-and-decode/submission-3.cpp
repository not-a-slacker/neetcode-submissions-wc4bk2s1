class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded="";
        for(int i=0;i<strs.size();i++)
        {
            int no_of_digits=0;
            int str_len=strs[i].size();
            while(str_len>0)
            {
                no_of_digits++;
                str_len=str_len/10;
            }
            if(no_of_digits==0){no_of_digits++;};
            encoded+=to_string(no_of_digits);
            encoded+=to_string(strs[i].size());
            encoded+=strs[i];
        }
        cout << "encoded: " << encoded;
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int curr=0;
        while(curr<s.size())
        {
            int no_of_digits=s[curr]-'0';
            int len=0;
            int digit;
            cout << "no_of_digits" << no_of_digits << endl;
            for(int i=no_of_digits;i>0;i--)
            {
                curr++;
                digit=s[curr]-'0';
                len+=digit*int(pow(10,i-1));
            }
            cout << "len: " << len << "\n";
            string curr_s="";
            for(int i=0;i<len;i++)
            {
                curr++;
                curr_s+=s[curr];
            }
            decoded.push_back(curr_s);
            curr++;
        }
        return decoded;
    }
};
