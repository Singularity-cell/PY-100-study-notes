# Day06 列表综合练习：学生成绩分析系统
# 请按照注释完成代码

# 成绩列表
grades = [85, 92, 78, 90, 88, 76, 95, 89, 62, 73]

print("原始成绩列表：", grades)
print("=" * 50)

# 1. 计算平均分
total = 0
# 请在此处添加代码计算总分
average = 0  # 请修改这里
print(f"1. 平均分：{average:.1f}")  # :.1f保留一位小数

# 2. 找出最高分和最低分
# 方法1：使用max()和min()函数
highest = 0  # 请修改这里
lowest = 0   # 请修改这里

# 方法2：使用循环自己找（可选挑战）
# 请在此处添加循环代码

print(f"2. 最高分：{highest}，最低分：{lowest}")

# 3. 成绩分段统计
# 优秀(≥90)、良好(≥80)、及格(≥60)、不及格(<60)
excellent = 0  # 优秀人数
good = 0       # 良好人数
passing = 0    # 及格人数
failed = 0     # 不及格人数

# 请在此处添加循环统计代码

print("3. 成绩分段统计：")
print(f"   优秀(≥90)：{excellent}人")
print(f"   良好(≥80)：{good}人")
print(f"   及格(≥60)：{passing}人")
print(f"   不及格(<60)：{failed}人")

# 4. 找出所有不及格的成绩
fail_grades = []  # 存储不及格的成绩
# 请在此处添加代码

print("4. 不及格的成绩：", fail_grades)

# 5. 成绩排名（挑战：排序）
# 使用sort()方法对成绩排序（默认升序）
sorted_grades = []  # 请修改这里
print("5. 成绩排名（升序）：", sorted_grades)

# 6. 成绩提升计划
# 将所有成绩低于80分的增加5分（但不能超过100分）
improved_grades = []  # 存储提升后的成绩
# 请在此处添加代码

print("6. 成绩提升后的列表：", improved_grades)

# 7. 统计信息汇总
print("=" * 50)
print("成绩分析报告：")
print(f"  学生总数：{len(grades)}人")
print(f"  平均分：{average:.1f}")
print(f"  最高分：{highest}")
print(f"  最低分：{lowest}")
print(f"  优秀率：{excellent/len(grades)*100:.1f}%")
print(f"  及格率：{(excellent+good+passing)/len(grades)*100:.1f}%")

print("\n=== 分析完成 ===")
print("提示：")
print("1. 使用for循环遍历grades列表")
print("2. 使用if判断成绩属于哪个分段")
print("3. 使用append()方法向列表添加元素")
print("4. 使用max()和min()函数快速找到极值")