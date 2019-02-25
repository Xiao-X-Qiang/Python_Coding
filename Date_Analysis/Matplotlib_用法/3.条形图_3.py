from matplotlib import pyplot as plt
from matplotlib import font_manager

# 多次bar()横条形图绘制票房

# 假设你知道了列表a中电影分别在2017-09-14(b_14), 2017-09-15(b_15), 2017-09-16(b_16)三天的票房,为了展示列表中电影本身的票房以及同其他电影的数据对比情况

a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

# 中文显示
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# 图形大小
plt.figure(figsize=(20, 8), dpi=80)

bar_width = 0.3  # bar_width*3 <=1 ，否则会有重叠

# 刻度显示及中文显示
x_1 = list(range(len(a)))
x_2 = [x + bar_width for x in x_1]
x_3 = [x + bar_width * 2 for x in x_1]

# 绘图
plt.bar(x_1, b_14, width=bar_width, label="9月14日")
plt.bar(x_2, b_15, width=bar_width, label="9月15日")
plt.bar(x_3, b_16, width=bar_width, label="9月16日")

# 刻度标注
plt.xticks(x_2, a, fontproperties=my_font)

# 图例
plt.legend(loc="upper left", prop=my_font)

# 显示绘图
plt.show()
