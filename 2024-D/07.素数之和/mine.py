import math

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False;
    return True;

files = ["in1", "in2"];


for file in files:
    f = open(file);
    
    num = int(f.readline());
    num_range = num;
    
    
    is_prime = False;
    res = [];
    for i in range(2, num_range):
        if isprime(i) and num % i == 0:
            num = num // i;
            res.append(str(i));
            
        if num == 1:
            is_prime = True
            break;
    if is_prime:
        res_str = " ".join(res);
        print(res_str);
    else:
        print("-1 -1")
            
    
    
    f.close();