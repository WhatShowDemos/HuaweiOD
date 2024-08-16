files = ["in1", "in2"];


for file in files:
    f = open(file)
    
    aver_min = int(f.readline())
    fails = list(map(int, f.readline().split()))

    i = 0;
    has = False;
    res = [];
    while i < len(fails):
        next_id = i + 1;
        if next_id >= len(fails):
            break;
        
        fail_all = fails[i];
        num = 1;
        end = i;
        for j in range(next_id, len(fails)):
            fail_all += fails[j];
            num += 1;
            if fail_all/num > aver_min:
                end = j - 1;
                num -= 1;
                break;
            end = j;
        if num > 1:
            has = True;
            res.append("{}-{}".format(i, end))
        
        
        i = end + 1;
    print(" ".join(res))
        
    
    f.close()