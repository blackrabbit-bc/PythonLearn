"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组 是数组中的一个连续部分。
https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn3cg3/

思路：
遍历数组：取首个元素为子集，取子集和当前值之和，大于当前值则往后取，否则重新取值；取所有子集和最大值

"""


def func001(nums):
    temp = []
    res = nums[0]
    for i in nums:
        if not temp:
            temp.append(i)
            res = max(res, sum(temp))
        elif sum(temp) + i > 0:
            if sum(temp) <= 0:
                temp = [i]
            else:
                temp.append(i)
            res = max(res, sum(temp))
        else:
            temp = [i]
            res = max(res, sum(temp))
        print(temp)
        print(res)
    return res


def func002(nums):
    temp = 0
    res = nums[0]
    for i in nums:
        temp = max(temp + i, i)
        res=max(res,temp)
        print("i:{}".format(i))
        print("temp:{}".format(temp))
        print("res:{}".format(res))
    return res


# s =[1,2,3,4,-11,8]
s=[-1,-2,-3]
print(func002(s))
