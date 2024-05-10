#Problem Statement:
Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.

#Python Code:
class Solution:
    def get(self, a, b):
        a=a+b
        b=a-b
        a=a-b
        return (a,b)
        #code here
