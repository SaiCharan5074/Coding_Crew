#Problem Statement:
Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

#Python Code:
class Solution:
    def nPr(self, n, r):
        # code here
        def fact(n):
            if n==1 or n==0:
                return 1
            else:
                return n*fact(n-1)
                
        def nPr1(n,r):
            return fact(n)/fact(n-r)
            
        return int(nPr1(n,r))