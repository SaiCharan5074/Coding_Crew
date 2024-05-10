#Problem statement:
Given two positive integers a and b, find GCD of a and b.

#Python Code:
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        def gcd1(a,b):
            if a==0:
                return b
            else:
                return gcd1(b%a,a)
                
        return(gcd1(a,b))
