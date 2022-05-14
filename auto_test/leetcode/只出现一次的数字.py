"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
链接：https://leetcode.cn/leetbook/read/top-interview-questions-easy/x21ib6/

思路：
001先排序，遍历数组，若temp列表为空，添加当前元素；否则对比但钱元素和temp最后一个元素，相等则删除最后一个元素。返回temp最后一个元素。

002异或运算：a^a=0,o^a=a,a^b^a=b;依次异或数组，结果为出现一次的值
"""


def func001(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if len(res) == 0:
            res.append(nums[i])
        elif nums[i] == res[-1]:
            res.pop()
        else:
            res.append(nums[i])
    return res[-1]


def func002(nums):
    res = 0
    for i in nums:
        res ^= i
    return res


s = [1, 2, 2]
print(func001(s))
