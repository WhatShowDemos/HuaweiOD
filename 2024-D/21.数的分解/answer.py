def solve():
    sum = int(input())  # 从标准输入读取一个整数n
    f = False  # 设置一个标志变量f，用于表示是否找到了有效的分解
    ans = []  # 初始化一个列表，用于存储找到的连续整数序列
    m = 1  # 初始化m，表示连续整数的个数，从1开始，实际循环中会先自增
 
    while True:
        m += 1  # 将m增加1，因为分解至少需要2个数
        if (2 * sum) % m != 0:  # 如果2*sum不是m的倍数，跳过当前m
            continue
        y = 2 * sum // m - m + 1  # 计算可能的连续序列的第一个数
        if y <= 0:  # 如果y小于等于0，说明不可能再找到有效的序列，终止循环
            break
        if y % 2 == 0:  # y必须是偶数，以确保可以从正整数开始
            f = True  # 设置找到分解的标志为True
            for x in range(y // 2, y // 2 + m):  # 计算并存储连续的整数序列
                ans.append(x)
            break  # 找到了最小的m，退出循环
 
    if f:  # 如果找到了至少一个有效的分解
        print(sum, end='=')  # 输出原始的整数和等号
        print(ans[0], end='')  # 输出序列的第一个整数
        for i in range(1, len(ans)):  # 遍历序列，输出剩余的加号和数字
            print('+', end='')
            print(ans[i], end='')
        print()  # 输出换行符
    else:
        print('N')  # 如果没有找到任何有效的分解，输出"N"
 
if __name__ == '__main__':
    solve()