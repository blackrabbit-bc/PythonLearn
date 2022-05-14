# ui2常用方法
import uiautomator2

# 链接设备:mumu模拟器
device = uiautomator2.connect('127.0.0.1:7555')

# 通过sourceId操作控件
device(resourceId='com.mumu.launcher:id/preview_background').click()

# 通过text操作控件
device(text='设置').click()

# 打开应用
device.app_start('com.android.browser')

# 滑动，可设置滑动时长
device.swipe(208, 1441, 433, 1461)

# 按住拖动，可设置拖动时长
device.drag(208, 1441, 433, 1461)
