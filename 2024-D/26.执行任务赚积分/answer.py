import heapq  # 引入heapq模块，用于操作堆结构
 
def solve():
    n = int(input())  # 读取任务数量N
    T = int(input())  # 读取可用于处理任务的时间T
    # 创建一个列表，索引表示任务的最晚处理时间，每个位置存储一个积分列表
    cod = [[] for i in range(105)]
    for i in range(n):
        # 读取每个任务的最晚完成时间和对应的积分值
        lastday, val = map(int, input().split())
        # 将积分值添加到对应的最晚完成时间的列表中
        cod[lastday].append(val)
    q = []  # 初始化一个小顶堆，用来存储当前可能处理的任务积分
    # 从1到T迭代，模拟每个时间单元处理任务
    for d in range(1, 101):
        # 将所有在当前时间点或之前需要完成的任务的积分加入堆中
        for x in cod[d]:
            heapq.heappush(q, x)  # 将积分压入小顶堆中
        # 如果堆的大小超过当前时间点，说明有超出处理时间的任务
        while len(q) > min(d, T):
            heapq.heappop(q)  # 弹出堆中最小的元素，优先保留高积分任务
    # 计算堆中剩余所有任务的积分总和
    ans = sum(q)
    # 输出最终可以获得的最大积分
    print(ans)
    
if __name__ == '__main__':
    solve()  # 执行solve函数