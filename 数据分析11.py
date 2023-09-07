import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
# 中文字体的导入方式（两种）
# 第一种
font = {
    'family': 'Microsoft Yahei',
    'weight': 'bold',
}
matplotlib.rc('font', **font)
# 第二种
# myfont = font_manager.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")


# 图片大小
plt.figure(figsize=(20, 8), dpi=80)

# x、y轴数据
a = input("请输入要查询的蔬菜：")
with open("xfd8-18.csv", "r", encoding="utf-8") as f:
    str1 = f.readlines()
    # print(str1, type(str1))
# 获取输入值的索引
for j in str1:
    if a in j:
        b = str1.index(j)

i = str1[b]
li1 = i.split(",")
# print(i)

with open("xfd8-21.csv", "r", encoding="utf-8") as f:
    str2 = f.readlines()

# 获取输入值的索引
for j in str2:
    if a in j:
        c = str2.index(j)

i2 = str2[c]
li2 = i2.split(",")

with open("xfd8-22.csv", "r", encoding="utf-8") as f:
    str3 = f.readlines()

# 获取输入值的索引
for j in str3:
    if a in j:
        d = str3.index(j)

i3 = str3[d]
li3 = i3.split(",")

with open("xfd8-29.csv", "r", encoding="utf-8") as f:
    str4 = f.readlines()

# 获取输入值的索引
for j in str4:
    if a in j:
        e = str4.index(j)

i4 = str4[e]
li4 = i4.split(",")

with open("xfd8-30.csv", "r", encoding="utf-8") as f:
    str5 = f.readlines()

# 获取输入值的索引
for j in str5:
    if a in j:
        f = str5.index(j)

i5 = str5[f]
li5 = i5.split(",")

x = [i for i in range(5)]
y = [0, float(li1[2]), float(li1[3]), float(li1[4]), 1]
y2 = [0, float(li2[2]), float(li2[3]), float(li2[4]), 1]
y3 = [0, float(li3[2]), float(li3[3]), float(li3[4]), 1]
y4 = [0, float(li4[2]), float(li4[3]), float(li4[4]), 1]
y5 = [0, float(li5[2]), float(li5[3]), float(li5[4]), 1]

# 绘图
plt.plot(x, y, color="cyan", linestyle=":", label="8.18")
plt.plot(x, y2, color="magenta", label="8.21")
plt.plot(x, y3, color="blue", label="8.22")
plt.plot(x, y4, color="red", label="8.29")
plt.plot(x, y5, color="green", label="8.30")


# x轴刻度线
# x_ticks = [i for i in range(5)]
x_ticks = [8.18, 8.21, 8.22, 8.19, 8.30]
# plt.xticks(x, x_ticks, rotation=90, fontproperties=myfont)
plt.xticks(x, x_ticks)

# y轴刻度线
y_ticks = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.yticks(y_ticks)

# 设置网格线
plt.grid(alpha=0.3)

# 添加标题
plt.title("新发地五日蔬菜价格统计图")

# 添加图例(A、B两条线)
plt.legend()

# 显示
plt.show()











