class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        int n = board[0].size();
        cout << "m : " << m << " n : " << n; 
        queue<pair<int,int>> q;
        for (int i=0;i<m;i++)
        {
            if (board[i][0]=='O')
            {
                pair<int,int> a = {i,0};
                q.push(a);
            }
            if (board[i][n-1]=='O')
            {
                pair<int,int> a = {i,n-1};
                q.push(a);
            }
        }
        for (int i=0;i<n;i++)
        {
            if (board[0][i]=='O')
            {
                pair<int,int> a = {0,i};
                q.push(a);
            }
            if (board[m-1][i]=='O')
            {
                pair<int,int> a = {m-1,i};
                q.push(a);
            }
        }
        while(q.size())
        {
            pair<int,int> a = q.front();
            q.pop();
            int i = a.first;
            int j = a.second;
            board[i][j] = '*';
            if ((i+1) < m && board[i+1][j] == 'O')
            {
                q.push({i+1,j});
            }
            if ((j+1) < n && board[i][j+1] == 'O')
            {
                q.push({i,j+1});
            }
            if ((i-1) >=0 && board[i-1][j] == 'O')
            {
                q.push({i-1,j});
            }
            if ((j-1) >=0 && board[i][j-1] == 'O')
            {
                q.push({i,j-1});
            }

        }
        for (int i=0;i<m;i++)
        {
            for (int j=0;j<n;j++)
            {
                if (board[i][j] == '*')
                {
                    board[i][j] = 'O';
                }
                else if (board[i][j] == 'O')
                {
                    board[i][j] = 'X';
                }
            }
        }
    }
};
