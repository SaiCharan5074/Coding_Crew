#Problem Statement:
You are given an integer N, reverse the digits of given number N, ensuring that the reversed number has no leading zeroes. Return the resulting reversed number.

#Python Code:
class Solution:
	def reverse_digit(self, n):
		# Code here
		rev=0
		while n>0:
		    dig=n%10
		    rev=(rev*10)+dig
		    n=n//10
		    
		return rev
