files = ["in1", "in2"];

for file in files:
    f = open(file)
    
    task_vol = int(f.readline());
    f.readline();
    tasks = list(map(int, f.readline().split()))
    
    left = 0;
    time = 0;
    for task in tasks:
        left += task;
        
        # pass 1 sec
        left -= task_vol;
        if left < 0:
            left = 0;
        time += 1;
    while left > 0:
        left -= task_vol;
        time += 1;
    
    print(time)
        
            
    f.close()