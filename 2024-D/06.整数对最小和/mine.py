f = open("in");

line = f.readline();
data = line.split();
in1 = list(map(int, data[1:]));

line = f.readline();
data = line.split();
in2 = list(map(int, data[1:]));

k = int(f.readline());


sum_all = [];


for i in range(len(in1)):
    for j in range(len(in2)):
        sum_all.append(in1[i]+in2[j]);

sum_all.sort();        
    



print(sum(sum_all[:k]));


f.close();