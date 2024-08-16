files = ["in1", "in2", "in3", "in4"];

for file in files:
    f = open(file);
    
    line = f.readline();
    data = line.split();
    a_num = int(data[0]);
    b_num = int(data[1]);
    
    line = f.readline();
    data = line.split();
    a = list(map(int, data));
    a.sort();
    
    line = f.readline();
    data = line.split();
    b = list(map(int, data));
    b.sort();
    
    
    for i in range(a_num):
        is_end = False;
        for j in range(b_num):
            a_sum_swap = sum(a) - a[i] + b[j];
            b_sum_swap = sum(b) - b[j] + a[i];
            
            if a_sum_swap == b_sum_swap:
                print("%d %d"%(a[i], b[j]))
                is_end = True;
                break;
        if is_end:
            break;
                
    
    f.close();
    
print("accurate output:");
print("1 2\n1 2\n2 3\n5 4");