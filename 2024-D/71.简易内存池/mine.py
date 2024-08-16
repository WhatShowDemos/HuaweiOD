files = ["in1", "in2"]

stack_max = 100;
stack_pre = 0;
stack_cur = 0;
stack_nex = 0

def stack_change(command):
    if "REQEUEST" in command:
        command = command.replace('REQEUEST=', "");
        return 1, int(command)
        
    if "RELEASE" in command:
        command = command.replace('RELEASE=', "");
        return 0, -int(command);


for file in files:
    f = open(file)
    
    N = int(f.readline().strip())
    for i in range(N):
        type_id, vol_change = stack_change(f.readline().strip())
        if type_id == 1 and vol_change == 0:
            print("ERROR")
            
        
    
    f.close()