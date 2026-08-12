class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<bool> base = vector<bool>(9, 0);
        for (size_t i = 0; i < 9; ++i) {
            vector<bool> column(base);
            for (size_t j = 0; j < 9; ++j) {
                int val = board[i][j]-'0';
                if (val > 0 && val < 10) {
                    if (column[val-1]) return false;
                    column[val-1] = true;
                }
            }
        }
        for (size_t i = 0; i < 9; ++i) {
            vector<bool> column(base);
            for (size_t j = 0; j < 9; ++j) {
                int val = board[j][i]-'0';
                if (val > 0 && val < 10) {
                    if (column[val-1]) return false;
                    column[val-1] = true;
                }
            }
        }
        for (int square = 0; square < 9; square++) {
            unordered_set<char> seen;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }

        return true;
    }
};
