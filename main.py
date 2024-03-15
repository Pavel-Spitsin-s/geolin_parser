from itertools import *
from math import factorial
import fractions


#BIG_N - типа COLUMNS
def make5dim(BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    res = []
    for l in range(BIG_N):
        res.append([])
        for i in range(BIG_ROWS):
            res[l].append([])
            for j in range(BIG_COLUMNS):
                res[l][i].append([])
                for f in range(ROWS):
                    res[l][i][j].append([])
                    for k in range(COLS):
                        res[l][i][j][f].append(0)
    return res
def to5dim(arr, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    res = make5dim(BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS)
    for l in range(BIG_N):
        for i in range(BIG_ROWS):
            for k in range(ROWS):
                for j in range(BIG_COLUMNS):
                    for f in range(COLS):
                        indh = l * BIG_N * BIG_COLUMNS + j * BIG_COLUMNS + f
                        indv = i * BIG_ROWS + k
                        res[l][i][j][k][f] = arr[indv][indh]
    return res
def cnt_inversion(A):
    c = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                c += 1
    return c
def sym(arr, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, fixed):
    DIM = 5
    cnt = factorial(DIM - sum(fixed))
    res = []
    SAMPLE_DIM = [i for i in range(DIM)]
    res = make5dim(BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS)
    for bn in range(BIG_N):
        for bc in range(BIG_ROWS):
            for br in range(BIG_COLUMNS):
                for r in range(ROWS):
                    for c in range(COLS):
                        perm = [bn, bc, br, r, c]
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
                            ans += arr[curp[0]][curp[1]][curp[2]][curp[3]][curp[4]]
                        res[bn][bc][br][r][c] = fractions.Fraction(ans, cnt)
    return res
def asym(arr, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, fixed):
    DIM = 5
    cnt = factorial(DIM - sum(fixed))
    res = []
    SAMPLE_DIM = [i for i in range(DIM)]
    res = make5dim(BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS)
    for bn in range(BIG_N):
        for bc in range(BIG_ROWS):
            for br in range(BIG_COLUMNS):
                for r in range(ROWS):
                    for c in range(COLS):
                        perm = [bn, bc, br, r, c]
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
                            if cnt_inversion(_) % 2 == 0:
                                ans += arr[curp[0]][curp[1]][curp[2]][curp[3]][curp[4]]
                            else:
                                ans -= arr[curp[0]][curp[1]][curp[2]][curp[3]][curp[4]]
                        
                        res[bn][bc][br][r][c] = fractions.Fraction(ans, cnt)
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
def to_ans(arr, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS):
    ans = []
    for f in range(BIG_ROWS):
        for j in range(ROWS):
            for l in range(BIG_N):
                for i in range(BIG_COLUMNS):
                    for k in range(COLS):
                        ans.append(arr[l][f][i][j][k])
    return to_ans2(ans)
def get_res(test, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, FIXED, isSym):
    if BIG_N == 1: 
        FIXED[0] = True
    if BIG_ROWS == 1:
        FIXED[1] = True
    if BIG_COLUMNS == 1:
        FIXED[2] = True
    if ROWS == 1:
        FIXED[3] = True
    if COLS == 1:
        FIXED[4] = True
    test = to5dim(test, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS) 
    if isSym:
        return to_ans(sym(test, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, FIXED), BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS)
    else:
        return to_ans(asym(test, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, FIXED), BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS)

test = [[4, 5, -4, -4, 3, 6, -1, 5, -1], [0, 1, -3, 0, -4, 0, 1, -4, -1], [6, 5, 5, 0, -5, -6, 5, 0, 5], [6, 6, 4, 5, -5, 1, 1, 1, 2], [4, 0, -4, -5, -3, 3, 3, -5, 3], [-5, -2, 1, -2, 1, 0, -4, -5, -4], [1, 3, -4, 3, -3, -2, 4, 2, -1], [0, 4, 1, 6, -5, 3, -4, 3, 1], [-4, -1, -5, 1, 4, -3, 3, -3, -1]]
BIG_N = 1
BIG_ROWS = 3
BIG_COLUMNS = 3
ROWS = 3
COLS = 3
FIXED = [True, False, False, False, True]
print(get_res(test, BIG_N, BIG_ROWS, BIG_COLUMNS, ROWS, COLS, FIXED, False))


'''
0 0 2 [0, 1, 2] False
0 0 2 [2, 1, 0] False

'''

            
                    

            