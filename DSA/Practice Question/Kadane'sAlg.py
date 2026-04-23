# maximum sum subarray 
num = [-2, 4, 5, 2, 7, 3, -6, -4, 7, 8, 6]
curr_sum = 0
max_sum = num[0]

for i in range(len(num)):
    curr_sum += num[i]    
    if curr_sum > max_sum:
        max_sum = curr_sum        
    if curr_sum < 0:
        curr_sum = 0
        
print(max_sum)
