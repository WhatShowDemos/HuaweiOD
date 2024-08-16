import sys
from collections import namedtuple
 
#for line in sys.stdin:
f = open("out");
out_std = f.readline();
f.close();
    
def cord_reg(line):
    cord = [];
    cord_str = line.split();
    cord_str_len = int(len(cord_str)/2);
    for i in range(cord_str_len):
        cord.append([int(cord_str[2*i]), int(cord_str[2*i+1])])
    return cord;

def qi_count(cord1, cord2):
    cord_all = cord1 + cord2;
    cord_qi = [];
    for cord in cord1:
        if cord[0] > 0:
            new_cord = [cord[0]-1, cord[1]];
            if new_cord not in cord_all and new_cord not in cord_qi:
                cord_qi.append(new_cord);
        if cord[0] < 18:
            new_cord = [cord[0]+1, cord[1]];
            if new_cord not in cord_all and new_cord not in cord_qi:
                cord_qi.append(new_cord);
        if cord[1] > 0:
            new_cord = [cord[0], cord[1]-1];
            if new_cord not in cord_all and new_cord not in cord_qi:
                cord_qi.append(new_cord);
        if cord[1] < 18:
            new_cord = [cord[0], cord[1]+1];
            if new_cord not in cord_all and new_cord not in cord_qi:
                cord_qi.append(new_cord);
    return len(cord_qi);
            
    
f = open("in");

# ist line
line = f.readline();
b_cord = cord_reg(line);

# 2nd line
line = f.readline();
w_cord = cord_reg(line);


w_qi = qi_count(w_cord, b_cord);
b_qi = qi_count(b_cord, w_cord);

out = str(b_qi) + " " + str(w_qi)
# print(COs)
# out = " ".join(COs_out);
print(out);

assert(out == out_std)

f.close();
    