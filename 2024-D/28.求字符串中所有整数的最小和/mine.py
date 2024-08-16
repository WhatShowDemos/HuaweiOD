import re

reg_exp_neg = re.compile(r"-(\d)*")
reg_exp_pos = re.compile(r"(\d)")


files = ["in1", "in2"]

for file in files:
    f = open(file)
    
    str_in = f.readline().strip();
    sum_all = 0;
    # find neg
    reg_matches = reg_exp_neg.finditer(str_in)
    for match1 in reg_matches:
        str_g = match1.group();
        sum_all += eval(str_g)
    # remove neg
    str_in_res = re.sub(reg_exp_neg, '', str_in);
    reg_matches = reg_exp_pos.finditer(str_in_res)
    for match1 in reg_matches:
        str_g = match1.group();
        sum_all += eval(str_g)
    print(sum_all)
    
    f.close()