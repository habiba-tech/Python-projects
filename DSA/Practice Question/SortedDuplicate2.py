num = [2,2,2,5,5,4,4,3,3,8,8,9]

# First sort the array
num.sort()
n = len(num)
if n <= 2:
    print(n)
else:
    start = 1
    for i in range(2, n):
        if num[i] != num[start - 1]:
            start += 1
            num[start] = num[i]
    print("Length:", start + 1)
    print("Array:", num[:start + 1])
