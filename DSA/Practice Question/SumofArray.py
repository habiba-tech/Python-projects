#Running sum of 1d array also called perfix sum

nums=[1,2,5,6,9,7]
n = len(nums)
ans=[ ]
ans.append(nums[0])
for i in range (1,n):
	x=ans[i-1] + nums[i]
	ans.append(x)
	
print (ans) 
