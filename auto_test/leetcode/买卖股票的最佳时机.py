"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn8fsh/

思路：
遍历数组，取首个值为买入价，取当前值作比较，如果当前值较小，作为卖出价幷取差值作为收入记录；如当期值较大，则取当前值为买入价继续往后比较；取所有记录的最大值。

"""


def func001(prices):
    buy = prices[0]
    price = 0
    for i in prices:
        if buy >= i:
            buy = i
        else:
            price = max(price, i - buy)
    return price


ss = [7, 1, 5, 3, 6, 4]
print(func001(ss))
