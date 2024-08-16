f = open("in")

gardens = list(map(int, f.readline().split()))

dicts = {};
for garden in gardens:
    if garden+1 in dicts:
        dicts[garden+1] += 1
    else:
        dicts[garden+1] = 1

child_num = 0;
for data in dicts:
    g_vol = data
    g_num = dicts[data]
    if g_num <= g_vol:
        child_num += g_vol;
    else:
        
        x = g_num // g_vol;
        if g_num % g_vol == 0:
            child_num += x*g_vol;
        else:
            child_num += (x+1)*g_vol;
print(child_num);

f.close();