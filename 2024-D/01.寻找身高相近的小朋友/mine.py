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
    a = line.split()
    xmh = int(a[0])
    n = int(a[1])
    # 2nd line
    s = f.readline();
    COs = list(map(lambda x: int(x), s.split()))
    CO = namedtuple("CO", ["diff", "h"])
    COs = list(map(lambda x: CO(abs(xmh - x), x), COs))
    COs.sort()
    COs_out = list(map(lambda x: str(x[1]), COs))
    # print(COs)
    out = " ".join(COs_out);
    print(out);
    
    assert(out == out_std)

    f.close();
    