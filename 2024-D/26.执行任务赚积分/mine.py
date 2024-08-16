files = ["in1", "in2"]
#files = ["in1"]

for file in files:
    f = open(file)
    
    task_num = int(f.readline())
    task_time = int(f.readline())
    tasks = {};
    for i in range(task_num):
        data = list(map(int, f.readline().split()))
        if data[0] in tasks:
            tasks[data[0]].append(data[1])
        else:
            tasks[data[0]] = [data[1]]
    
    score = 0;
    for task_id in tasks:
        #tasks[task_id].sort(reverse=True);
        score += max(tasks[task_id]);
    
    print(score)
    
    f.close()