from itertools import *
from math import factorial
import fractions
#n, m, k = list(map(int, input().split()))
#n - total dimensions



#BIG_COLUMNS
#ROWS
#COLS
test = [
    [
        [
            [1, 1, -5],
            [2, -3, 2],
            [-4, -6, -5],
        ],
        [
            [5, 0, 4],
            [6, 1, 4],
            [-3, -4, -4]
        ],
        [
            [-4, -2, 2],
            [3, 4, -6],
            [-6, 4, -1]
        ]
    ]
]
test2 = [
    [
        [
            [1, 1, -5], 
            [2, -3, 2], 
            [-4, -6, -5]
        ],
        [
            [5, 0, 4], 
            [6, 1, 4], 
            [-3, -4, -4]
        ], 
        [
            [-4, -2, 2], 
            [3, 4, -6], 
            [-6, 4, -1]
        ]
    ], 
    [
        [
            [-3, 3, 3], [2, -5, -4], [-2, -2, -5]], [[-4, 0, 0], [2, -1, -2], [0, 4, -3]], [[4, -4, 0], [-4, -4, 2], [-4, 5, 4]]], [[[3, -2, 1], [1, 4, 3], [-5, 4, 5]], [[4, -2, 0], [5, -2, -1], [3, -4, 3]], [[0, 
-1, -2], [-3, 0, -1], [-5, 6, 2]]]]
def make4dim(BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    res = []
    for i in range(BIG_ROWS):
        res.append([])
        for j in range(BIG_COLUMNS):
            res[i].append([])
            for f in range(ROWS):
                res[i][j].append([])
                for k in range(COLS):
                    res[i][j][f].append(0)
    return res
def to4dim(arr, BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    res = make4dim(BIG_ROWS, BIG_COLUMNS, ROWS, COLS)
    for i in range(BIG_ROWS):
        for k in range(ROWS):
            for j in range(BIG_COLUMNS):
                for f in range(COLS):
                    indh = j * BIG_COLUMNS + f
                    indv = i * BIG_ROWS + k
                    res[i][j][k][f] = arr[indv][indh]
    return res
def cnt_inversion(A):
    c = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                c += 1
    return c
def sym(arr, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, fixed):
    cntFixed = sum(fixed)
    res = []
    DIM = 4
    SAMPLE_DIM = [i for i in range(DIM)]
    for bc in range(BIG_ROWS):
        res.append([])
        for br in range(BIG_COLUMNS):
            res[bc].append([])
            for r in range(ROWS):
                res[bc][br].append([])
                for c in range(COLS):
                    perm = [bc, br, r, c]
                    ans = 0
                    for _ in permutations(SAMPLE_DIM):
                        _ = list(_)
                        curp = []
                        bad = False
                        for i in range(DIM): 
                            if fixed[i] and i != _[i]: 
                                bad = True
                            curp.append(perm[_[i]])
                        if bad: continue
                        ans += arr[curp[0]][curp[1]][curp[2]][curp[3]]
                    #ans /= factorial(DIM - cntFixed)
                    res[bc][br][r].append(fractions.Fraction(ans, factorial(DIM - cntFixed)))
    return res
def pretty_ans(arr):
    res = ""
    for i in arr:
        res += i + ', '
    return res
def to_ans2(arr):
    res = []
    for f in arr:
        if f.denominator == 1:
            res.append(str(f.numerator))
        else:
            res.append(str(f.numerator) + "/" + str(f.denominator))
    return pretty_ans(res)
def to_ans(arr, BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    ans = []
    for f in range(BIG_ROWS):
        for j in range(ROWS):
            for i in range(BIG_COLUMNS):
                for k in range(COLS):
                    ans.append(arr[f][i][j][k])
    return to_ans2(ans)
    
test1 = [[1, 1, -5, 5, 0, 4, -4, -2, 2], [2, -3, 2, 6, 1, 4, 3, 4, -6], [-4, -6, -5, -3, -4, -4, -6, 4, -1], [-3, 3, 3, -4, 0, 0, 4, -4, 0], [2, -5, -4, 2, -1, -2, -4, -4, 2], [-2, -2, -5, 0, 4, -3, -4, 5, 4], [3, -2, 1, 4, -2, 0, 0, -1, -2], [1, 4, 3, 5, -2, -1, -3, 0, -1], [-5, 4, 5, 3, -4, 3, -5, 6, 2]]
#print(to4dim(test1, 3, 3, 3, 3))    
print(to_ans(sym(test2, 3, 3, 3, 3, [False, False, True, False]), 3, 3, 3, 3))

'''
0 0 2 [0, 1, 2] False
0 0 2 [2, 1, 0] False

'''

            
                    

            