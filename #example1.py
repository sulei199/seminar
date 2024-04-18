#example
import matplotlib.pyplot as plt

# 示例数据
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]

# 创建柱状图
plt.bar(categories, values, color='skyblue')

# 添加标题和标签
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图形
plt.show()
