files = ["in1", "in2"]


for file in files:
    f = open(file)
    
    data = list(map(int, f.readline().split()));
    n = data[0];
    m = data[1];
    subjs = f.readline().strip().split();
    studs = [];
    for i in range(n):
        data = list(f.readline().strip().split());
        name = data[0];
        marks = list(map(int, data[1:]));
        marks_all = sum(marks);
        marks.insert(0, name);
        marks.append(marks_all)
        studs.append(marks)
    subj_need = f.readline().strip();
    
    if subj_need in subjs:
        subj_need_idx = subjs.index(subj_need) + 1;
        
        studs.sort(key=lambda x:(-x[subj_need_idx], x[0]))
    else:
        studs.sort(key=lambda x:(-x[-1], x[0]))
    
    names = [];
    for stud in studs:
        names.append(stud[0]);
    print(" ".join(names))
    
    f.close();