def solve():
    mem = [0] * 105  # 用于记录内存池中每个字节的使用状态
    len = [0] * 105  # 用于记录每个分配块的长度
    n = int(input())  # 输入操作命令的数量
    for _ in range(n):
        op, val = input().split('=')  # 读取操作命令和参数值
        val = int(val)
        if op == 'REQUEST':
            p = request(mem, len, val)
            if p == -1:
                print('error')  # 内存分配失败
            else:
                print(p)  # 内存分配成功，输出首地址
        elif op == 'RELEASE':
            if not release(mem, len, val):
                print('error')  # 内存释放失败
 
def release(mem, len, p):
    if len[p] == 0:
        return False  # 如果该首地址处没有分配内存，则返回错误
    for i in range(p, p + len[p]):
        mem[i] = 0  # 将从p开始的len[p]个字节的内存标记为未使用状态
    len[p] = 0  # 清空该首地址处的内存块长度记录
    return True
 
def request(mem, len, siz):
    if siz == 0:
        return -1  # 如果请求的内存大小为0，则返回错误
    l = 0
    while l < 100:
        if mem[l] != 0:
            l += 1
            continue
        r = l
        while r < 100 and mem[r] == 0:
            r += 1
        if r - l >= siz:
            for i in range(l, l + siz):
                mem[i] = 1  # 将该连续块标记为已使用
            len[l] = siz  # 记录该块的长度
            return l  # 返回分配到的内存首地址
        l = r + 1
    return -1  # 如果未找到合适的空闲块，则返回错误
 
if __name__ == '__main__':
    solve()