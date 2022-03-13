# 地下城堡3 自动刷
import uiautomator2
import time


class DiXiaChenBao:
    def __init__(self):
        pass

    @staticmethod
    def auto_clear(stage: str):
        d = uiautomator2.connect('127.0.0.1:7555')
        # 蛮牛谷军营
        while stage == '1':
            d.click(917, 1287)
            time.sleep(3)
            d.click(714, 1687)
            time.sleep(3)
            d.click(740, 2237)
            time.sleep(3)

            d.click(714, 1287)
            time.sleep(3)
            d.click(730, 985)
            time.sleep(3)
            d.click(711, 1587)
            time.sleep(10)
            d.click(724, 2163)
            time.sleep(3)

            d.click(714, 995)
            time.sleep(3)
            d.click(717, 1579)
            time.sleep(10)
            d.click(727, 2170)
            time.sleep(3)

            d.click(721, 998)
            time.sleep(3)
            d.click(727, 1584)
            time.sleep(10)
            d.click(730, 2155)
            time.sleep(3)

            d.click(711, 998)
            time.sleep(3)
            d.click(714, 983)
            time.sleep(3)
            d.click(708, 1587)
            time.sleep(3)
            d.click(708, 2265)
            time.sleep(3)

        # 废弃岗哨
        while stage == '2':
            d.click(724, 1213)
            time.sleep(3)
            d.click(724, 1587)
            time.sleep(3)
            d.click(717, 2257)
            time.sleep(3)

            d.click(717, 1282)
            time.sleep(3)
            d.click(420, 983)
            time.sleep(8)
            d.click(721, 2165)
            time.sleep(3)

            d.click(1002, 975)
            time.sleep(8)
            d.click(711, 2155)
            time.sleep(3)

            d.click(1029, 975)
            time.sleep(8)
            d.click(695, 2158)
            time.sleep(3)

            d.click(702, 988)
            time.sleep(3)
            d.click(724, 1584)
            time.sleep(3)
            d.click(708, 1285)
            time.sleep(3)

            d.click(724, 967)
            time.sleep(8)
            d.click(721, 2165)
            time.sleep(3)

            d.click(708, 691)
            time.sleep(3)
            d.click(721, 1582)
            time.sleep(13)
            d.click(721, 2165)
            time.sleep(3)

            d.click(724, 983)
            time.sleep(3)
            d.click(721, 1587)
            time.sleep(3)
            d.click(705, 2263)
            time.sleep(3)

        while stage == '9':
            d.click(858, 872)
            time.sleep(3)
            d.click(740, 1510)
            time.sleep(3)
            d.click(973, 1681)
            time.sleep(30)
            d.click(692, 2170)
            time.sleep(3)
