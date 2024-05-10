#Problem Statement:
Create the multiplication table of a given number N and return the table as an array.

#Python code:
class Solution:
    def getTable(self,N):
        l1=[]
        # code here
        for i in range(1,11):
            l1.append(N*i)
            
        return l1
        