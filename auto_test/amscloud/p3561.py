'''
http://www.amoscloud.com/?p=3561
  给定一个射击比赛成绩单
  包含多个选手若干次射击的成绩分数
  请对每个选手按其最高三个分数之和进行降序排名
  输出降序排名后的选手id序列
  条件如下
    1. 一个选手可以有多个射击成绩的分数，且次序不固定
    2. 如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手
    3. 如果选手的成绩之和相等，则相等的选手按照其id降序排列
   输入描述:
     输入第一行
         一个整数N
         表示该场比赛总共进行了N次射击
         产生N个成绩分数
         2<=N<=100
     输入第二行
       一个长度为N整数序列
       表示参与每次射击的选手id
       0<=id<=99
     输入第三行
        一个长度为N整数序列
        表示参与每次射击选手对应的成绩
        0<=成绩<=100
   输出描述:
      符合题设条件的降序排名后的选手ID序列
    输入:
        13
        3,3,7,4,4,4,4,7,7,3,5,5,5
        53,80,68,24,39,76,66,16,100,55,53,80,55
    输出:
        5,3,7,4
13
3,3,7,4,4,4,4,7,7,3,5,5,5
53,80,68,24,39,76,66,16,100,55,53,80,55
'''


def func():
    n = int(input())
    ids = list(map(int, input().strip().split(',')))
    scores = list(map(int, input().strip().split(',')))
    result = {}
    for i in range(len(ids)):
        if ids[i] not in result.keys():
            result[ids[i]] = [scores[i]]
        else:
            result[ids[i]].append(scores[i])
    print(result)
    for i in result.keys():
        sum = 0
        if len(result[i]) < 3:
            result.pop(i)
        else:
            for j in range(3):
                sum += max(result[i])
                result[i].remove(max(result[i]))
        result[i] = sum
    print(result)
    list1=[]
    list2=result.keys()
    for i in range(len(list2)):
        if




    #     print(id_list)
    #     count_list[id_list.index(ids[i])] += 1
    #     score_list[id_list.index(ids[i])] += scores[i]
    # print(id_list)
    # print(count_list)
    # print(score_list)


func()
