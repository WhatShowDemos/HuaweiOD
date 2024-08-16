import re
files = ["in1", "in2"]

for file in files:
    f = open(file)
    
    data = f.readline().strip().replace(",","")
    
    data = re.sub(r"111", "x", data);
    data = re.sub(r"11", "x", data);
    data = re.sub(r"1", "x", data);
    car = data.count("x");
    print(car)
    
    f.close()