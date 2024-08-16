import sys
 
f = open("in")
data = f.readline().split(' ')
 
my_dict = {}
res = 0
for i in data:
    if int(i) in my_dict:
        my_dict[int(i)] += 1
    else:
        my_dict[int(i)] = 1
for i in my_dict:
    
    res += ( ( (my_dict[i] - 1) // (i + 1) ) + 1) * (i + 1)
   
print(res)

f.close()