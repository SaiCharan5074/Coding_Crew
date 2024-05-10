#Problem statement:
Given an integer N, find the number of divisors of N that are divisible by 3.
 
#Python code:
import math
class Solution:
    def count_divisors(self, N):
        if N==1:
            return 0
        count1=0
        # code here
        for i in range(1,int(math.sqrt(N))+1):
            if N%i==0:
                if i%3==0:
                    count1+=1
                if (int(N/i))%3==0 and i!=int(N/i):
                    count1+=1
                    
        return count1
