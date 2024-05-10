#Problem Statement:
Given a number, reverse it and add it to itself unless it becomes a palindrome or number of iterations becomes more than 5.

#Python Code:
class Solution:
    def isSumPalindrome (self, n):
        it=0
        # code here 
        def ispalindrome(num):
            s1=str(num)
            s2=s1[::-1]
            if s1==s2:
                return True
            return False
            
        while True:
            if ispalindrome(n):
                return n
            st1=str(n)
            st2=st1[::-1]
            if ispalindrome(int(st1)+int(st2)):
                return int(st1)+int(st2)
                
            it+=1
            k=int(st1)+int(st2)
            if it>4:
                return -1
            if ispalindrome(k):
                return k
                break
            n=k