from matplotlib import pyplot as plt
from matplotlib import font_manager

# 在绘制直方图时：1.数据必须是未经统计的原始数据  2.如果是已经统计后的数据，可用条形图达到直方图的效果

# 在美国2004年人口普查发现有124 million的人在离家相对较远的地方工作。
# 根据他们从家到上班地点所需要的时间,通过抽样统计(最后一列)出了下表的数据,这些数据能够绘制成直方图么?
# 显然不能，只能使用条形图达到直方图的效果

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

# 中文显示
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# 图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 因为数据是经统计后的，不适用于直方图，因而使用条形图 达到 直方图的效果
plt.bar(range(len(interval)),quantity,width=1)  # 在条形图中，注意图形与x轴刻度的对应关系，图形在刻度的正中，width默认0.8

_x = [ i - 0.5 for i in range(len(interval)+1)]  # 要显示的刻度
_x_label = interval + [150]
# _x_label = interval.append(150)  # 错误，此时 _x_label = None,是.append()的返回结果，并非变量 a的引用
plt.xticks(_x,_x_label)

# 显示绘图
plt.show()
