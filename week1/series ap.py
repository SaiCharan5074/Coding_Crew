#Problem Statement:
Given the first 2 terms a1 and a2 of an Arithmetic Series.Find the nth term of the series. 
#Python code:
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        d=a2-a1
        return a1+(n-1)*d
        