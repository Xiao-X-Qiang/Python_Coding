
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager  # 支持中文显示

# 如果列表a表示10点到12点的每一分钟的气温,如何绘制折线图观察每分钟气温的变化情况?
# a= [random.randint(20,35) for i in range(120)]

# 显示图片的大小及分辨率
plt.figure(figsize=(20,8),dpi=80)

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1,2,3,4,5]

y_1 = [1,2,2,1,3,4,1,3,2,1,0,2,3,1,1,1,1,1,1,1,1,1,1,1]

x = range(11,35)

# x轴刻度支持中文显示
my_font = font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")

# 绘图并调整其样式(color,linestyle,alpha)，并添加图例(1.添加label 2.调用legend()方法)
plt.plot(x,y,label="自个",color="orange",linestyle=":",alpha=0.8,linewidth=2)
plt.plot(x,y_1,label="同桌",color="#DB7093",linestyle="-")

# 添加图例
plt.legend(prop=my_font,loc="upper left")  # 添加图例并指定其位置loc，并显示中文字体，此处用的prop参数而非fontproperties,更多参数查看源码

# 设置x轴的刻度步长(即密集程度)及为刻度添标注信息
_x = x[::2]
x_label = ["{}岁".format(i) for i in _x]
plt.xticks(_x,x_label,rotation=45,fontproperties=my_font)  # 取步长，数字和字符串一一对应，两者的长度相等；rotation：逆时针旋转x轴刻度

# 对图形添加描述信息
plt.xlabel("年龄 ",fontproperties=my_font)
plt.ylabel("个数",fontproperties=my_font)
plt.title("随年龄交的朋友个数",fontproperties=my_font)

# 绘制网格及设置样式，类同plot()的样式，其中透明度 0:完全透明  1:实线
# 网络的密集程度与x、y的个数相关
plt.grid(alpha=0.7,linestyle="--")

plt.show()  # 显示图片

# 保存图片
plt.savefig("./h1.png")  # 保存图片，会根据文件名的后缀名判别保存的图片格式，支持png,svg,不支持jpg