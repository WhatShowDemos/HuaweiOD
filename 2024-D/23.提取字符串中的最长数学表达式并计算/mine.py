import re

def find_exp(ss):
    #reexp=re.compile(r"(\d+)([+*-]\d+)*")
    reexp=re.compile(r'(\d+)([+*-]\d+)*')
    matches = reexp.finditer(ss);
    str_len_max = 0;
    eq = None;
    for match1 in matches:
        match_str = match1.group()
        match_str_len = len(match_str);
        if match_str_len > str_len_max:
            str_len_max = match_str_len;
            eq = match_str;
    if eq:
        return eval(eq);
    else:
        return 0;

f = open("in")

in_str = f.readline().strip()
print(find_exp(in_str))


f.close()