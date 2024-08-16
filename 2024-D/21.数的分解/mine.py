f = open("in1")
number = int(f.readline());

m = 1;
res = [];

while True:
    m += 1;
    # has residual
    if 2*number % m != 0:
        continue;
    else:    
        start2 = 2*number // m - m + 1;
        if start2 < 1:
            break;
        elif start2 % 2 == 0:
            for seq_data in range(start2//2, start2//2 + m):
                res.append(str(seq_data))
            break;

if len(res) > 0:
    print(str(number)+"="+"+".join(res))
else:
    print("N")

f.close();