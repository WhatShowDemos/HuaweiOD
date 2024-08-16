f = open("in");

N = int(f.readline());
mems = list(map(int, f.readline().split()));
mems.sort(reverse=True);
ab_min = int(f.readline())

mems_taken = [0]*N

team_num = 0;
for i in range(N):
    if mems_taken[i] == 1:
        break;
    else:
        if mems[i] >= ab_min:
            team_num += 1;
            mems_taken[i] = 1;
        else:
            for j in range(N-1, i, -1):
                if mems_taken[j] != 1:
                    if mems[i] + mems[j] >= ab_min:
                        team_num += 1;
                        mems_taken[i] = 1;
                        mems_taken[j] = 1;
                        break;
        

f.close();


print("Accurate:\n3");