files = ["in1", "in2"]
out_accs = ["700", "1100"];

for file in files:
    f = open(file)
    
    N = int(f.readline())
    forts = list(map(int, f.readline().split()))
    
    fam = [];
    for i in range(N):
        fam.append([forts[i], forts[i]]);
        
    for i in range(N-1):
        data = list(map(int, f.readline().split()));
        fathe = data[0] - 1;
        child = data[1] - 1;
        
        fam[fathe][0] += fam[child][1];
    
    fam.sort(reverse=True)
    print(fam[0][0])
    
    f.close()