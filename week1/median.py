#problem statement:
Given an array arr[] of N integers, calculate the median.

NOTE: Return the floor value of the median.
#Python code:
import math
class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		if len(v)%2!=0:
		    return v[((len(v)+1)//2)-1]
		else:
		    return math.floor((v[(len(v)//2)-1]+v[(len(v)//2)])//2)
		