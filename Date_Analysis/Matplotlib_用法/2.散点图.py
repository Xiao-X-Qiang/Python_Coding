
from matplotlib import pyplot as plt

from matplotlib import font_manager

# 绘制北京3月和10月的天气温度散点图
# 使用scatter()方法绘制散点图

a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

plt.figure(figsize=(20,8),dpi=80)

# 显示中文字体
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# x坐标
x = range(len(a))
x_1 = range(40,40+len(b))

# 刻度标注
_x = list(x) + list(x_1)
_x_label = ["3月{}日".format(i) for i in x]
_x_label += ["10月{}日".format(i-40) for i in x_1]
plt.xticks(_x[::2],_x_label[::2],fontproperties=my_font,rotation=45)

# 使用scatter方法绘散点图图例
plt.scatter(x,a,label="3月")
plt.scatter(x_1,b,label="10月")

plt.legend(loc="upper left",prop=my_font)

# 图形展示
plt.show()