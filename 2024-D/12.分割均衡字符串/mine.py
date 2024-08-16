files = ["in1"];


for file in files:
    f = open(file);
    
    string = f.readline();
    
    num = 0;
    xnum = 0;
    ynum = 0;
    for i in range(len(string)):
        if string[i] == 'X':
            xnum +=1;
        else:
            ynum +=1
        if xnum == ynum and xnum > 0:
            num += 1;
            xnum = 0;
            ynum = 0;
    print(num)
    
    f.close();