#sort array by parity 
nums=[5,2,1,4,3,7,8,9]
n=len(nums) 
start =0
for i in range (n):
	if nums[i]%2==0:
		temp = nums[i]
		nums[i] =nums[start]
		nums[start]=temp
		start +=1
print( nums)
