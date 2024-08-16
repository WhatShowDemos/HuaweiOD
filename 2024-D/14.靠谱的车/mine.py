f = open("in");

for li in range(3):
    data = f.readline().strip();
    
    
    act = 0;
    for i in range(1, len(data)+1):
        digit = int(data[-i]);
        if digit > 4:
            digit -= 1;
        act += digit*(9**(i-1))
    
    print(act)
f.close();



