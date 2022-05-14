import random
from mahjong import mahjong_base

mahjong = mahjong_base.MahjongBase()

# for _ in range(10):
#     hand_group=mahjong.get_hand_group()
#     print(hand_group)
#     result = mahjong.flag_win(hand_group)
#     print(result)


for _ in range(1):
    hand_group = ['1万', '1万', '1万', '2万', '3万', '4万', '5万', '6万', '7万', '8万', '9万', '9万', '9万', '{}万'.format(random.randint(1, 9))]
    hand_group = ['1万', '2万', '3万', '2万', '3万', '4万', '2万', '3万', '4万', '8万', '9万', '9万', '9万', '8万']
    print(hand_group)
    result = mahjong.flag_win(hand_group)
    print(result)
