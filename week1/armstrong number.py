#Problem Statement:
For a given 3 digit number, find whether it is armstrong number or not. An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. Return "Yes" if it is a armstrong number else return "No".

#Python code:
class Solution:
    def armstrongNumber (self, n):
        # code here 
        num1=n
        res=0
        s1=str(n)
        k=len(s1)
        while num1>0:
            dig=num1%10
            res+=pow(dig,k)
            num1=num1//10
            
        if res==n:
            return "Yes"
        else:
            return "No"
            