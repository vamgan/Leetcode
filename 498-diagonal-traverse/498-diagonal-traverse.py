class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        self.ans = []
        def traverse(mat,i,j, up):
            if i >= len(mat) or j >= len(mat[0]):
                return
            self.ans.append(mat[i][j])
            if up:
                if i > 0 and j < len(mat[0]) - 1:
                    i -= 1
                    j += 1
                else:
                    if j < len(mat[0]) - 1:
                        j += 1
                    else:
                        i += 1
                    up = False
            else:
                if i < len(mat) - 1 and j > 0:
                    i  += 1
                    j -= 1
                else:
                    if i < len(mat) - 1:
                        i += 1
                    else:
                        j += 1
                    up = True
            traverse(mat, i, j, up)
        traverse(mat, 0, 0, True)
        return self.ans