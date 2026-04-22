#Remove Duplicate from sorted Array
num=[2,2,2,5,5,4,4,3,3,8,8,9]
n= len(num)
start=0
for i in range (1,n):
	#unique element
	if num [i] != num[start]:
		start +=1 
		num [start] = num[i]
print (start+1)
print ( "duplicate values ",num[:start+1])
