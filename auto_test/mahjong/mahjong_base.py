import random


class MahjongBase:
    # 设置基础牌型和对应值
    def __init__(self):
        self.list_dot = ['1筒', '2筒', '3筒', '4筒', '5筒', '6筒', '7筒', '8筒', '9筒']
        self.list_dot_value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.list_bamboo = ['1条', '2条', '3条', '4条', '5条', '6条', '7条', '8条', '9条']
        self.list_bamboo_value = [11, 12, 13, 14, 15, 16, 17, 18, 19]
        self.list_character = ['1万', '2万', '3万', '4万', '5万', '6万', '7万', '8万', '9万']
        self.list_character_value = [21, 22, 23, 24, 25, 26, 27, 28, 29]
        self.list_honor = ['东', '南', '西', '北', '中', '白', '发']
        self.list_honor_value = [111, 222, 333, 444, 555, 666, 777]

        self.list_type = self.list_dot + self.list_bamboo + self.list_character + self.list_honor
        self.list_type_value = self.list_dot_value + self.list_bamboo_value + self.list_character_value + self.list_honor_value
        self.map = dict(zip(self.list_type, self.list_type_value))

    @staticmethod
    # 计算元素在list中的个数
    def count(ele, list_ele):
        count = 0
        for temp in list_ele:
            if ele == temp:
                count += 1
        return count

    # 获取手牌14张
    def get_hand_group(self):
        hand_group = []
        list_mahjiong = self.list_type * 4
        for _ in range(14):
            temp = random.choice(list_mahjiong)
            hand_group.append(temp)
            list_mahjiong.remove(temp)
        return hand_group

    # 判断手牌是否胡牌，只判断常规牌型;True：胡牌、False：未胡牌
    def flag_win(self, hand_group):
        hand_group_value = []
        for temp in hand_group:
            hand_group_value.append(self.map[temp])
        hand_group_value.sort()

        list_pair = []
        for temp in hand_group_value:
            if self.count(temp, hand_group_value) > 1:
                list_pair.append(temp)
        if len(list_pair) == 0:
            return False
        else:
            for temp_pair in list_pair:
                count_meld = 0
                hand_group_value_bak = list(hand_group_value)
                hand_group_value_bak.remove(temp_pair)
                hand_group_value_bak.remove(temp_pair)
                for temp in hand_group_value_bak:
                    while len(hand_group_value_bak) > 0 and self.count(temp, hand_group_value_bak) > 2:
                        hand_group_value_bak.remove(hand_group_value_bak[0])
                        hand_group_value_bak.remove(hand_group_value_bak[0])
                        hand_group_value_bak.remove(hand_group_value_bak[0])
                        count_meld += 1
                    while len(hand_group_value_bak) > 0 and hand_group_value_bak[0] + 1 in hand_group_value_bak and hand_group_value_bak[0] + 2 in hand_group_value_bak:
                        hand_group_value_bak.remove(hand_group_value_bak[0] + 2)
                        hand_group_value_bak.remove(hand_group_value_bak[0] + 1)
                        hand_group_value_bak.remove(hand_group_value_bak[0])
                        count_meld += 1
                if count_meld == 4:
                    return True
        return False