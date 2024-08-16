import sys
from collections import namedtuple
 
#for line in sys.stdin:
f = open("out");
out_std = f.readline();
f.close();
    


if __name__ == "__main__":
    f = open("in");
    # ist line
    line = f.readline();
    line_in = line.split();
    h = int(line_in[0]);
    n = int(line_in[1]);
    
    # 2nd line
    s = f.readline();
    ss = s.split();
    ss_int = [];
    for ss1 in ss:
        ss1 = int(ss1)
        ss_int.append([abs(ss1 - h), ss1]);
    ss_int.sort();
    out_arr = [];
    for ss_int1 in ss_int:
        out_arr.append(str(ss_int1[1]));
    
    out = " ".join(out_arr);
    print(out);
    
    assert(out == out_std)

    f.close();
    