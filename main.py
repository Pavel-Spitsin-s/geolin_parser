from itertools import *
from math import factorial
#n, m, k = list(map(int, input().split()))
#n - total dimensions



#BIG_COLUMNS
#ROWS
#COLS
test = [
    [
        [6, 4, -6],
        [6, -5, -4],
        [4, 0, -3]
    ],
    [
        [2, 4, -3],
        [6, -3, 1],
        [5, 5, 2]
    ],
    [
        [4, -1, 4],
        [4, 4, 1],
        [4, 0, 0]
    ]
]
def cnt_inversion(A):
    c = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                c += 1
    return c
def sym(arr, BIG_COLUMNS, ROWS, COLS, fixed):
    cntFixed = sum(fixed)
    #for br in range(BIG_ROWS):
    res = []
    for bc in range(BIG_COLUMNS):
        res.append([])
        for r in range(ROWS):
            res[bc].append([])
            for c in range(COLS):
                perm = [bc, r, c]
                ans = 0
                for _ in permutations([0, 1, 2]):
                    _ = list(_)
                    curp = []
                    bad = False
                    for i in range(3): 
                        if fixed[i] and i != _[i]: 
                            bad = True
                        curp.append(perm[_[i]])
                    if bad: continue
                    ans += arr[curp[0]][curp[1]][curp[2]]
                    if bc == 1 and r == 0: print(bc, r, c, _, curp, ans)
                ans /= factorial(3 - cntFixed)
                res[bc][r].append(ans)
    return res
def to_ans(arr, BIG_COLUMNS, ROWS, COLS):
    ans = []
    for j in range(ROWS):
        for i in range(BIG_COLUMNS):
            for k in range(COLS):
                ans.append(arr[i][j][k])
    return ans     
print(to_ans(sym(test, 3, 3, 3, [False, True, False]), 3, 3, 3))
'''
0 0 2 [0, 1, 2] False
0 0 2 [2, 1, 0] False

'''

            
                    

            