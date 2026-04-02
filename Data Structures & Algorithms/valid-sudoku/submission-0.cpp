class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0;i<9;i++)
        {
            vector<int> check_row(9,0);
            for(int j=0;j<9;j++)
            {
                if(board[i][j]=='.')
                {
                    continue;
                }
                else
                {
                    if(check_row[board[i][j]-'1']==1)
                    {
                        cout << "error in row" << i;
                        return false;
                    }
                    check_row[board[i][j]-'1']=1;
                }
            }
            vector<int> check_col(9,0);
            for(int j=0;j<9;j++)
            {
                if(board[j][i]=='.')
                {
                    continue;
                }
                else
                {
                    if(check_col[board[j][i]-'1']==1)
                    {
                        return false;
                    }
                    check_col[board[j][i]-'1']=1;
                }
            }
        }
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                vector<int> check_box(9,0);
                for(int k=0;k<3;k++)
                {
                    for(int l=0;l<3;l++)
                    {
                        if(board[3*i+k][3*j+l]=='.')
                        {
                            continue;
                        }
                        else
                        {
                            if(check_box[board[3*i+k][3*j+l]-'1']==1)
                            {
                                cout << "error in box";
                                return false;
                            }
                            check_box[board[3*i+k][3*j+l]-'1']=1;
                        }
                    }
                }

            }
        }
        return true;
    }
};
