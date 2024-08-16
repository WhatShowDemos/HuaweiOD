#files = ["in2"];

files = ["in1", "in2"];
out_accs = ["0", "1"];


def is_strange(command_num, luck, commands):
    if command_num < 1 or command_num > 100:
        return True;
    if luck < -100 or luck > 100:
        return True;
    if command_num != len(commands):
        return True;
    for command in commands:
        if command < -100 or command > 100:
            return True;
    return False;
    

for file in files:
    f = open(file);
    command_num = int(f.readline());
    luck = int(f.readline());
    commands = list(map(int, f.readline().split()));
    
    if is_strange(command_num, luck, commands):
        print("12345")
    else:
        pos = [0];
        for command in commands:
            step = command;
            if command == luck:
                if step > 0:
                    step += 1;
                elif step < 0:
                    step -= 1;
            pos.append(pos[-1] + step);
        print(max(pos))
    
    f.close();
print("accurate output");
for out_acc in out_accs:
    print(out_acc) 