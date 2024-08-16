def calc_score(weight, data):
    score = 0;
    for i in range(len(data)):
        score += weight[i]*data[i];
    return -score;

f = open("in");
line = f.readline();
N = int(line);
line = f.readline();
w = list(map(int, line.split()));


proj = [];



for l in range(N):
    line = f.readline();
    data = line.split();
    data_name = data[0];
    
    data_name = data_name.lower();
    data_data = list(map(int, data[1:]));
    proj.append([calc_score(w,data_data), data_name])
    
proj.sort();
for i in range(len(proj)):
    print(proj[i][1]);

f.close();   
