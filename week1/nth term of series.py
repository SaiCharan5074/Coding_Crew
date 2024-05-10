#Problem Statement:
Given a number N, find the Nth term in the series 1, 3, 6, 10, 15, 21…

#Python code:
class Solution:
    def findNthTerm(self, N):
        # code here 
        return N*(N+1)//2

