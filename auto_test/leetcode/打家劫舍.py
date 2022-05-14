"""

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnq4km/

思路：
如果房屋数量大于两间，应该如何计算能够偷窃到的最高总金额呢？对于第 k~(k>2)k (k>2) 间房屋，有两个选项：

偷窃第 k 间房屋，那么就不能偷窃第 k-1 间房屋，偷窃总金额为前 k-2 间房屋的最高总金额与第 k 间房屋的金额之和。

不偷窃第 k 间房屋，偷窃总金额为前 k-1k−1 间房屋的最高总金额。


简化空间复杂度：
我们发现 dp[n] 只与 dp[n−1] 和 dp[n−2] 有关系，因此我们可以设两个变量 cur和 pre 交替记录，将空间复杂度降到 O(1)。

"""


def func001(nums):
    length = len(nums)
    res = []
    for i in range(length):
        if i == 0:
            res.append(nums[0])
        elif i == 1:
            res.append(max(nums[0], nums[1]))
        else:
            res.append(max(res[i - 1], res[i - 2] + nums[i]))
    return res[-1]


def func002(nums):
    res = 0
    pre = 0
    cur = 0
    for i in range(len(nums)):
        if i == 0:
            pre = nums[0]
            res = pre
        elif i == 1:
            cur = max(nums[0], nums[1])
            res = cur
        elif i == len(nums) - 1:
            res = max(pre + nums[i], cur)
        else:
            temp = pre
            pre = cur
            cur = max(temp + nums[i], cur)
    return res


s = [2, 7, 9, 3, 1]
print(func002(s))
