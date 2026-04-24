# Day07 元组基础练习
# 请按照注释完成代码

# 1. 创建元组
# 创建一个包含3个颜色的元组：红色、绿色、蓝色
colors = ("红色", "绿色", "蓝色")  # 请修改这里

print("1. 颜色元组：", colors)

# 2. 访问元组元素
# 打印第二个颜色（索引从0开始）
second_color = colors[1]  # 请修改这里
print("2. 第二个颜色：", second_color)

# 3. 尝试修改元组元素（理解不可变性）
# 下面的代码会报错，请注释掉它，然后运行程序看看错误信息
# colors[0] = "黄色"  # 这行会报错，请注释掉
print("3. 尝试修改后（应该无变化）：", colors)

# 4. 元组长度
# 使用len()函数获取元组长度
tuple_length = len(colors)  # 请修改这里
print("4. 元组长度：", tuple_length)

# 5. 遍历元组（使用for循环）
print("5. 遍历颜色元组：")
# 请在此处添加for循环代码
for color in colors:
    print(color)

# 6. 使用enumerate()遍历（带索引）
print("6. 带索引遍历：")
# 请在此处添加enumerate()代码
for i, color in enumerate(colors):
    print(f"索引{i}: {color}")

# 7. 元组解包练习
# 创建一个坐标元组 (10, 20)
coordinates = (10, 20)  # 请修改这里

# 使用元组解包获取x和y坐标
x, y = coordinates  # 请修改这里
print("7. 坐标解包：")
print(f"  x坐标: {x}")
print(f"  y坐标: {y}")

# 8. 交换两个变量的值（使用元组解包）
a = 5
b = 10
print("8. 交换前：", f"a={a}, b={b}")

# 使用元组解包交换a和b的值
a, b = b, a  # 请修改这里
print("8. 交换后：", f"a={a}, b={b}")

# 9. 元组连接（创建新元组）
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # 请修改这里
print("9. 连接后的元组：", combined_tuple)

# 10. 元组方法练习
numbers = (1, 2, 3, 2, 4, 2, 5)

# 使用count()方法统计数字2出现的次数
count_2 = numbers.count(2)  # 请修改这里
print("10. 数字2出现的次数：", count_2)

# 使用index()方法查找数字4第一次出现的索引
index_4 = numbers.index(4)  # 请修改这里
print("10. 数字4的索引：", index_4)

# 11. 检查元素是否存在
# 检查数字3是否在元组中
has_3 = 3 in numbers  # 请修改这里
print("11. 元组中是否有数字3：", has_3)

# 12. 从列表创建元组
my_list = ["苹果", "香蕉", "橙子"]
my_tuple = tuple(my_list)  # 请修改这里
print("12. 从列表创建的元组：", my_tuple)

print("\n=== 练习完成 ===")
print("请对照README.md检查你的答案是否正确！")