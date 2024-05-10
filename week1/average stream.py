#Problem Statement:
Given a stream of incoming numbers, find average or mean of the stream at every point.

#Python Code:
class Solution:
	def streamAvg(self, arr, n):
	    def getavg(x,n,sum):
            sum+=x
            return float(sum)/n
	    l1=[]
		# code here
		avg=0
		sum=0
		for i in range(n):
		    avg=getavg(arr[i],i+1,sum)
		    sum=avg*(i+1)
		    l1.append(avg)
		    
		return l1
