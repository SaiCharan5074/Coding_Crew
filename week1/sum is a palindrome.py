#problem statement:
Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.
#Python Code:
class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        sum1=0
        while n>0:
            dig=n%10
            sum1+=dig
            n=n//10
            
        s1=str(sum1)
        if s1==s1[::-1]:
            return 1
        else:
            return 0