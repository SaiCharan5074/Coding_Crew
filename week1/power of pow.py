#Problem Statement:
Given a single integer N, your task is to find the sum of the square of the first N even natural Numbers.

#Python Code:
import math
class Solution:
	def sum_of_square_evenNumbers(self, n):
		# Code here
		return 4*(n*(n+1)*(2*n+1)//6)
