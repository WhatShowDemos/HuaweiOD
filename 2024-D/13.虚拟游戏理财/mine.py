f = open("in")

data = list(map(int, f.readline().split()))
N = data[0];
invest_max = data[1]
risk_max = data[2]

retns = list(map(int, f.readline().split()));
risks = list(map(int, f.readline().split()));
invests = list(map(int, f.readline().split()));





def calc_reward(invest_max, a_lim, a_rtn, b_lim,b_rtn):
    if invest_max <= a_lim:
        return invest_max*a_rtn, invest_max, 0;
    else:
        rtn = a_lim*a_rtn;
        left = invest_max - a_lim;
        if left > b_lim:
            left = b_lim
        rtn += left*b_rtn;
        return rtn, a_lim, left;

# double
combs = [];
for i in range(N - 1):
    if i + 1 >= N:
        break;
    for j in range(i+1, N):
        if risks[j] + risks[i] <= risk_max:
            if retns[i] > retns[j]:
                reward = calc_reward(invest_max, invests[i], retns[i], invests[j], retns[j]);
                reward = list(reward);
                reward.append(i)
                reward.append(j)
            else:
                reward = calc_reward(invest_max, invests[j], retns[j], invests[i], retns[i]);
                reward = list(reward);
                reward.append(j)
                reward.append(i)
            
            combs.append(reward);
combs.sort(reverse=True)


singles = [];
for i in range(N):
    if risks[i] <= risk_max:
        buy = invests[i] if invest_max > invests[i] else invest_max
        singles.append([buy*retns[i], buy,i])
singles.sort(reverse=True);


buy_num = [];
if combs[0][0] > singles[0][0]:
    for i in range(N):
        if i == combs[0][3]:
            buy_num.append(str(combs[0][1]))
        elif i == combs[0][4]:
            buy_num.append(str(combs[0][2]))
        else:
            buy_num.append(str(0))
else:
    for i in range(N):
        if i == singles[0][2]:
            buy_num.append(str(singles[0][1]))
        else:
            buy_num.append(str(0))

print(" ".join(buy_num))
f.close()