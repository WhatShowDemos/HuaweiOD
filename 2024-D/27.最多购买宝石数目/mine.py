files = ["in1", "in2", "in3", "in4"]
out_accs = [3, 0, 4, 9]

for file in files:
    f = open(file)
    
    germ_num_max = int(f.readline())
    germs = [];
    for i in range(germ_num_max):
        germs.append(int(f.readline()));
    value_max = int(f.readline())
    
    value = 0;
    germ_num = 0
    for i in range(germ_num_max):
        value_tmp = 0;
        germ_tmp = 0
        for j in range(i, germ_num_max):    
            if value_tmp + germs[j] > value_max:
                break;
            else:
                value_tmp += germs[j];
                germ_tmp += 1
        if germ_tmp > germ_num:
            germ_num = germ_tmp
    print(germ_num);
                
    
    f.close()
    
print("accurate:")
for out_acc in out_accs:
    print(out_acc);