'''
https://sites.google.com/googleapps.wrdsb.ca/fryer-davis-classes/math-club

https://www.cemc.uwaterloo.ca/contests/past_contests.html
'''


## https://cemc2.math.uwaterloo.ca/contest/PSG/school/print.php?f=web&h=y&t=&ids=p855-p1560-p905-p381-p1563-p995-p620-p889-p1590-p369-p1872-p300-p871-p2077-p1424

DEBUG = True
## Puzzle
## Yann writes down the first n consecutive positive integers, 1,2,3,...,n. 
## He removes four different integers p,q,r,s from the list.
## At least three of p,q,r,s are consecutive and 100<p<q<r<s.
## The average of the integers remaining in the list is 89.5625.
## What is the number of possible values of s?
def p14_01_10_2023():
    # sum of [1..n] is n(n+1)//2, avg is (n+1)/2, the closest for 89.5625 is n=179.
    # as the four integers are bigger than 100, so removing them will decrease average,
    # so the original avg cannot be less than 89, n = 177
    # also avg of [1..n-4] cannot be bigger than 90, n <183.
    DEBUG = False
    if DEBUG: print('\n>>p14_01_10_2023')
    res = 0
    for n in range(177, 183):
        sm = n *(n + 1) // 2
        for p in range(101, n - 2):
            for s in list(range(101, p)) + list(range(p+3, n)):
                # q = p + 1, s = p + 2
                if (n - 4) * 89.5625 == sm - (p + p + 1 + p + 2 + s):
                    if DEBUG:
                        if s > p + 2:
                            A = [p,p+1,p+2,s]
                        else:
                            A = [s,p,p+1,p+2]
                        print(n, res, A)
                    res += 1
                    break
    return res
def p14_01_10_2023_2():
    DEBUG = False
    # sum of [1..n] is n(n+1)//2, avg is (n+1)/2, the closest for 89.5625 is n=179.
    # as the four integers are bigger than 100, so removing them will decrease average,
    # so the original avg cannot be less than 89, n = 177
    # also avg of [1..n-4] cannot be bigger than 90, n <183.
    if DEBUG: print('\n>>p14_01_10_2023_2')
    from itertools import combinations
    res = 0
    for n in range(177, 183):
        sm = n *(n + 1) // 2
        A = list(range(n + 1))
        for p,q,r,s in combinations(A, 4):
                if 101<p+1==q==r-1 or 101<p+1<q+1==r==s-1:
                    if (n - 4) * 89.5625 == sm - (p + q + r + s):
                        if DEBUG:
                            print(n, res, [p,q,r,s])
                        res += 1
    return res

## For any real number x, f(x) denotes the largest integer less than or equal to x.
## For example, f(4.2) = 4 and f(0.9) = 0.
## If S is the sum of all integers k with 1<=k<=999,999
## and for which k is divisible by f(sqrt(k)). What is the value of S?
## A. 999500000 B. 999000000 C. 999999000 D. 998999500 E. 998500500
def p15_01_10_2023():
    # if k is a perfect square number, it is valid
    from math import sqrt
    if DEBUG: print('\n>>p15_01_10_2023')
    res = 0
    for k in range(1, 1000000):
        # x = sqrt(k) - b, b < 1
        # for k in [i^2, (i+1)^2], x = i 
        x = int(sqrt(k))
        if k % x == 0:
            res += k
    return res
def p15_01_10_2023_2():
    if DEBUG: print('\n>>p15_01_10_2023_2')
    res = cnt = 0
    # x = sqrt(k) - b, b < 1
    # for k in [i^2, (i+1)^2], x = i 
    for i in range(1, 1000):
        for k in range(i*i, (i+1)*(i+1)):
            if k % i == 0:
                res += k
                cnt += 1
    return res, cnt
def p15_01_10_2023_3():
    if DEBUG: print('\n>>p15_01_10_2023_3')
    res = 0
    # for k in [i^2, (i+1)^2], only 3 numbers are able to be divided by i
    # i^2, i^2 + i, i^2 + 2i
    # so counter of this kind of numbers is 3*999 = 2997
    # sum = 3(1**2+2**2+...+n**2) + 3(1+2+...+n) = n(n+1)(2n+1)/2 + 3n(n+1)/2
    i = 999
    return i*(i+1)*(2*i+1)//2+3*i*(i+1)//2



def main():
    print(p14_01_10_2023())
    # print(p14_01_10_2023_2())
    print(p15_01_10_2023())
    print(p15_01_10_2023_2())
    print(p15_01_10_2023_3())

main()