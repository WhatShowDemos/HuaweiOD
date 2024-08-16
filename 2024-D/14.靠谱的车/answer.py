import sys
 
f = open("in");
for li in range(3):
    N = f.readline().strip()
    index =0
 
    offset = 0
    before_offset = 0
    while index<len(N):
        cur_n = N[len(N)-1-index]
        if cur_n!="0":
            offset += int(cur_n)*before_offset
            if cur_n>"4":
                offset += 10**index-before_offset
        before_offset = before_offset*9+ 10**index
        index += 1
    print(int(N)-offset)
    
f.close();
 
 