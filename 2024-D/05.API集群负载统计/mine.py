files = ["in1", "in2"]


for file in files:
    f = open(file)
    rec_num = int(f.readline());
    recs = [];
    for i in range(rec_num):
        rec = f.readline();
        rec = rec.split("/");
        rec = rec[1:];
        recs.append(rec);
    line = f.readline();
    line = line.split();
    layer = int(line[0]);
    strin = line[1];

    num_count = 0;
    for i in range(rec_num):
        if len(recs[i]) < layer:
            continue;
        tmp = recs[i][layer-1].replace('\n', '')
        if tmp == strin:
            num_count=num_count+1;
    print(num_count);
    f.close();