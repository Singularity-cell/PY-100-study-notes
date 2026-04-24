# Day07 - 元组（Tuple）数据结构

## 📚 学习目标
1. 理解元组的概念和特点
2. 掌握元组与列表的区别
3. 学习元组的基本操作（创建、访问、遍历）
4. 了解元组的应用场景
5. 完成元组基础练习

## 🎯 为什么学习元组？

元组是Python中**另一个重要的数据结构**，与列表相似但有一个关键区别：**元组是不可变的**。

### 列表 vs 元组
| 特性 | 列表（List） | 元组（Tuple） |
|------|-------------|--------------|
| 可变性 | ✅ 可变（可修改） | ❌ 不可变（创建后不能修改） |
| 语法 | 方括号 `[]` | 圆括号 `()` |
| 性能 | 相对较慢 | 相对较快 |
| 内存占用 | 较大 | 较小 |
| 使用场景 | 需要修改的数据 | 不需要修改的数据 |

### 元组的实际应用场景
- **坐标点**：`(x, y)` 坐标不应该被单独修改
- **RGB颜色**：`(255, 0, 0)` 红色值固定
- **数据库记录**：一条记录的各字段不应该被修改
- **函数返回值**：函数可以返回多个值（实际上是一个元组）
- **配置参数**：固定的配置项

## 📝 核心知识点

### 1. 创建元组

```python
# 空元组
empty_tuple = ()
print(empty_tuple)  # ()

# 单元素元组（注意：必须有逗号！）
single_tuple = (5,)  # ✅ 正确
not_a_tuple = (5)    # ❌ 错误，这是整数5

# 多元素元组
coordinates = (10, 20)
colors = ("红色", "绿色", "蓝色")
mixed = ("苹果", 5, True, 3.14)  # 可以混合类型

# 不加括号也可以（但建议加上）
simple_tuple = 1, 2, 3  # Python会自动识别为元组
print(simple_tuple)  # (1, 2, 3)

# 从列表转换为元组
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # (1, 2, 3)
```

### 2. 访问元组元素

```python
student = ("张三", 18, "男", 95.5)

# 正向索引（从0开始）
print(student[0])   # "张三"
print(student[1])   # 18
print(student[2])   # "男"

# 负向索引（从-1开始）
print(student[-1])  # 95.5（最后一个）
print(student[-2])  # "男"（倒数第二个）

# 切片操作（获取子元组）
print(student[1:3])   # (18, "男")（索引1到2）
print(student[:2])    # ("张三", 18)（从开始到索引1）
print(student[2:])    # ("男", 95.5)（从索引2到结束）
```

### 3. 元组操作（不可变性是关键！）

```python
# 创建元组
numbers = (1, 2, 3, 4, 5)

# ✅ 可以访问
print(numbers[0])  # 1
print(numbers[1])  # 2

# ❌ 不能修改
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# ❌ 不能添加
# numbers.append(6)  # AttributeError: 'tuple' object has no attribute 'append'

# ❌ 不能删除
# del numbers[0]  # TypeError: 'tuple' object doesn't support item deletion

# ✅ 但可以重新赋值（创建新元组）
numbers = (10, 20, 30)  # 这是创建新的元组，不是修改原来的

# ✅ 可以连接元组（创建新元组）
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)
```

### 4. 元组解包（重要功能！）

```python
# 基本解包
coordinates = (10, 20)
x, y = coordinates  # x=10, y=20
print(f"x坐标: {x}, y坐标: {y}")

# 交换两个变量的值（经典用法）
a = 5
b = 10
a, b = b, a  # a=10, b=5
print(f"a={a}, b={b}")

# 多值解包
student = ("李四", 20, "计算机科学")
name, age, major = student
print(f"姓名: {name}, 年龄: {age}, 专业: {major}")

# 使用*收集剩余元素
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
# first=1, middle=[2, 3, 4], last=5
```

### 5. 常用元组方法

```python
my_tuple = (1, 2, 3, 2, 4, 2)

# count(x) - 统计元素x出现的次数
print(my_tuple.count(2))  # 3

# index(x) - 返回元素x第一次出现的索引
print(my_tuple.index(3))  # 2

# len(tuple) - 获取元组长度
print(len(my_tuple))  # 6

# in 操作符 - 检查元素是否存在
print(3 in my_tuple)  # True
print(10 in my_tuple) # False
```

### 6. 元组与for循环

```python
# 遍历元组元素
colors = ("红色", "绿色", "蓝色", "黄色")
for color in colors:
    print(f"颜色: {color}")

# 遍历元组索引和元素
for i, color in enumerate(colors):
    print(f"颜色{i+1}: {color}")

# 遍历元组解包
students = [("张三", 18), ("李四", 20), ("王五", 19)]
for name, age in students:
    print(f"{name}的年龄是{age}岁")
```

### 7. 元组与函数的配合

```python
# 函数返回多个值（实际上是返回一个元组）
def get_student_info():
    name = "张三"
    age = 18
    score = 95.5
    return name, age, score  # 实际上是返回 (name, age, score)

# 接收函数返回的多个值
student_name, student_age, student_score = get_student_info()
print(f"学生: {student_name}, 年龄: {student_age}, 成绩: {student_score}")

# 如果只需要部分返回值
name, _, score = get_student_info()  # 用_忽略不需要的值
print(f"姓名: {name}, 成绩: {score}")
```

## 🎯 练习项目

### 项目1：坐标系统
创建一个坐标系统，练习元组的基本操作。

### 项目2：学生成绩统计
使用元组存储学生信息，练习元组解包和遍历。

### 项目3：颜色转换
使用元组表示RGB颜色，练习元组的应用。

## 💡 学习建议

1. **理解不可变性**：这是元组与列表的核心区别
2. **掌握元组解包**：这是Python中非常实用的功能
3. **选择合适的场景**：不需要修改的数据用元组，需要修改的数据用列表
4. **注意单元素元组**：别忘了逗号！

## 🚀 下一步学习

掌握了元组后，你将学习：
- **Day08**: 字典（Dictionary） - 键值对数据结构
- **Day09**: 集合（Set） - 无序不重复元素集合
- **Day10**: 字符串（String）高级操作

元组是Python数据结构的基石之一，理解了它，你就能更好地理解Python的数据处理方式！