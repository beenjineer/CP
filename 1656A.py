# A good pair is a pair of indices (𝑖,𝑗) with 1≤𝑖,𝑗≤𝑛 such that, for all 1≤𝑘≤𝑛, the following equality holds:
# |𝑎𝑖−𝑎𝑘|+|𝑎𝑘−𝑎𝑗|=|𝑎𝑖−𝑎𝑗|

t = int(input()) 

# for _ in range(t): 
#     n = int(input())
#     arr = [int(i) for i in input().split()]
    
#     for i in range(n): 
#         for j in range(n): 
#             if all([abs(arr[i] - arr[k]) + abs(arr[k] - arr[j]) == abs(arr[i] - arr[j]) for k in range(n)]):
#                 print(i + 1, j + 1)  

# Optimized Solution
for _ in range(t): 
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    min_index = 0
    max_index = 0

    for i in range(n): 
        if arr[i] < arr[min_index]: 
            min_index = i 
        if arr[i] > arr[max_index]: 
            max_index = i 

    print(min_index+1, max_index+1)
    