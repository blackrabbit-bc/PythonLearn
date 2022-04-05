# ui2常用方法
import uiautomator2

driver = uiautomator2.connect('127.0.0.1:7555')

# 滑动，可设置滑动时长
driver.swipe(208, 1441, 433, 1461)

# 按住拖动，可设置拖动时长
driver.drag(208, 1441, 433, 1461)

