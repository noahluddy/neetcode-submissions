# O(1) ST, since all sudokus will be 9x9
# O(nm) T, O(n) S where board is n x m

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        for row in board:
            valid &= self.validateGroup(row)
        # for col in list(zip(*board)):
        #     valid &= validateGroup(col)
        for i in range(0, 9):
            col = [board[j][i] for j in range(0, 9)]
            valid &= self.validateGroup(col)
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = [board[i1][j1] for i1 in range(i, i+3) for j1 in range(j, j+3)]
                valid &= self.validateGroup(box)
        return valid

    def validateGroup(self, chars: List[str]) -> bool:
        # chars is a list of exactly nine chars
        # we expect 0 or 1 instances of each number 1-9 and unlimited num of .
        seen = set()
        valid = True
        for c in chars:
            if c == '.':
                continue
            elif c in seen:
                valid &= False
            seen.add(c)
        return valid
        
    # def validateGroup(self, chars: List[str]) -> bool:
    #     # chars is a list of exactly nine chars
    #     # we expect 0 or 1 instances of each number 1-9 and unlimited num of .
    #     seen = {str(i) : False for i in range(1, 10)}
    #     valid = True
    #     for c in chars:
    #         if c == '.':
    #             continue
    #         # some non-digit char
    #         elif c not in seen:
    #             valid &= False
    #         elif seen[c]:
    #             valid &= False
    #         seen[c] = True
    #     return valid
