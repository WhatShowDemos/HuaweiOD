import sys
import heapq
 
f = open("in");

lines = [line.strip() for line in f.readlines()]
 
array1 = [int(n) for n in lines[0].split()][1:]
array2 = [int(n) for n in lines[1].split()][1:]
k = int(lines[2])
array = []
 
total = 0
i, j = 0, 0
 
heapq.heappush(array, (array1[i] + array2[j], i, j))
visited = set()
while k > 0 and array:
    value, i, j = heapq.heappop(array)
    if (value, i, j) in visited:
        continue
    visited.add((value, i, j))
    total += value
    if i + 1 < len(array1):
        heapq.heappush(array, (array1[i + 1] + array2[j], i + 1, j))
    if j + 1 < len(array2):
        heapq.heappush(array, (array1[i] + array2[j + 1], i, j + 1))
    
    
    k -= 1
print(total)

f.close();