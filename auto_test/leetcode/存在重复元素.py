"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。

思路：
使用set()将列表转换为元祖，自动去重，对比长度即可
"""
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
nums_set = set(nums)
if len(nums) == len(nums_set):
    print(True)
else:
    print(False)
