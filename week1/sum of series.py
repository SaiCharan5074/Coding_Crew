#Problem Statement:
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 

#Python Code:
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        return n*(n+1)//2
        