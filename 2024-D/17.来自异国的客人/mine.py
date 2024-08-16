files = ["in1", "in2"]
out_accs = [2, 0]

for file in files:
    f = open(file);
    data = list(map(int, f.readline().split()));
    N = data[0];
    luck = str(data[1]);
    mod = data[2];
    
    left = N;
    N_mod = "";
    while left >= mod:
        res = left % mod;
        left = left // mod;
        N_mod = str(res) + N_mod;
    N_mod = str(left) + N_mod;
    
    print(N_mod.count(luck))
    
    f.close()








print("Accurate:")
for out_acc in out_accs:
    print(out_acc);