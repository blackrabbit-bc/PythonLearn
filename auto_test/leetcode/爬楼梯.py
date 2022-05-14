"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

思路：
可使用递归；但是递归重复，耗时较高，使用数组存储对应阶梯的值，减少次数
"""


def func(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        dp = [0] * (num + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, num + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    return dp[num]

print(func(3))
