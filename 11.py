'''
Created on Feb 27, 2021

@author: zahar
'''
from collections import deque


class Solution:

    def solve(self, A):
        row = len(A)
        col = len(A[0])
        B = [[1 for _ in range(col)] for _ in range(row)]
        seen = set()

        def nei(i, j):
            if i + 1 < row and A[i + 1][j] == 0:
                yield (i + 1, j)
            if j + 1 < col and A[i][j + 1] == 0:
                yield (i, j + 1)
            if i - 1 >= 0 and A[i - 1][j] == 0:
                yield (i - 1, j)
            if j - 1 >= 0 and A[i][j - 1] == 0:
                yield (i, j - 1)

        for i in range(row):
            for j in range(col):
                if i not in (0, row - 1) and j not in (0, col - 1):
                    continue
                if (i, j) in seen:
                    continue
                if A[i][j] == 1:
                    continue
                d = deque([(i, j)])
                while d:
                    x, y = d.popleft()
                    B[x][y] = 0
                    for x2, y2 in nei(x, y):
                        if (x2, y2) not in seen:
                            d.append((x2, y2))
                            seen.add((x2, y2))
        return B


mat = [[1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 1, 0, 1, 1, 1, 1],
       [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
       [1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
       [1, 1, 1, 0, 1, 0, 1, 0, 0, 1],
       [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]

n = len(mat)
m = len(mat[0])

# print(ob.solve(mat))

ob1 = Solution()
aux = ob1.solve(mat)

for i in range(0, len(aux)):
    for j in range(0, len(aux[0])):
        print(str(aux[i][j]) + " ", end="")
    print()
