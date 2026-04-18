# -*- coding: utf-8 -*-  # 解决编码问题

print("=== Day02 变量与数据类型演示 ===")

# 1. 变量赋值
name = "S"
age = 25
height = 1.75
is_student = True

print(f"姓名：{name}")
print(f"年龄：{age}岁")
print(f"身高：{height}米")
print(f"是学生吗？{is_student}")

# 2. 查看数据类型
print(f"\n--- 数据类型检查 ---")
print(f"name 的类型：{type(name)}")
print(f"age 的类型：{type(age)}")
print(f"height 的类型：{type(height)}")
print(f"is_student 的类型：{type(is_student)}")

# 3. 用户输入
print(f"\n--- 与程序对话 ---")
user_name = input("你叫什么名字？ ")
user_age = input("你多大了？ ")

print(f"你好，{user_name}！你{user_age}岁了。")

# 4. 类型转换
print(f"\n--- 类型转换 ---")
# 字符串转数字
age_number = int(user_age)  # 把文字年龄变成数字
next_year = age_number + 1
print(f"明年你就{next_year}岁了！")

# 数字转字符串
age_str = str(age_number)  # 把数字年龄变回文字
print(f"你的年龄作为文字是：'{age_str}'")
