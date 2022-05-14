'''
给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。
示例 1：
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。

思路：
本质上是取所有上升时的区间的值。
'''

def test_func001(prices):
    buy = [ prices[0], 0]
    sale = [ prices[0], 0]
    price = 0
    for i in range(len(prices)):
        if (buy[0] > prices[i] or buy[0]==prices[i]) and buy[1] == 0:
            buy[0] = prices[i]
            sale[0]=buy[0]
        elif buy[1] == 0:
            buy[1] = 1
            sale[0] = prices[i]
        elif sale[0] < prices[i]:
            sale[0] = prices[i]
        else:
            sale[1] = 1
        if buy[1] == 1 and sale[1] == 1:
            price += sale[0] - buy[0]
            buy = [prices[i], 0]
            sale = [prices[i], 0]
        if i == len(prices) - 1:
            price += sale[0] - buy[0]
    return price

def test_func002(prices):
    price = 0
    for i in range(len(prices)-1):
        if prices[i+1]-prices[i]>0:
            price+=prices[i+1]-prices[i]
    return price

test_list =[7,1,5,3,6,4]
print(test_func002(test_list))