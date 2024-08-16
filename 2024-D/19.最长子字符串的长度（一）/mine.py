# 计算 o出现次数，基数次就丢失一个o，偶数次全保留


f = open("in")

for i in range(3):
    data = f.readline().strip();
    o_num = data.count('o');
    if o_num % 2 == 0:
        print(len(data));
    else:
        print(len(data) - 1)

print("Accurate:\n6\n7\n6")

f.close();