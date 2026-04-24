# Day08 - 字典（Dictionary）数据结构

## 📚 学习目标
1. 理解字典的概念和特点
2. 掌握字典的创建、访问和修改
3. 学习字典的常用方法
4. 了解字典的应用场景
5. 完成字典基础练习

## 🎯 为什么学习字典？

字典是Python中**最强大、最常用的数据结构**之一，它使用**键值对（key-value pairs）** 来存储数据。

### 字典 vs 列表 vs 元组

| 特性 | 列表（List） | 元组（Tuple） | 字典（Dictionary） |
|------|-------------|--------------|------------------|
| 存储方式 | 有序序列 | 有序序列 | **键值对映射** |
| 访问方式 | 数字索引 | 数字索引 | **键（key）** |
| 可变性 | ✅ 可变 | ❌ 不可变 | ✅ 可变 |
| 语法 | 方括号 `[]` | 圆括号 `()` | 花括号 `{}` |
| 使用场景 | 有序数据集合 | 固定数据集合 | **关联数据映射** |

### 字典的实际应用场景
- **用户信息**：`{"name": "张三", "age": 25, "city": "北京"}`
- **配置设置**：`{"theme": "dark", "language": "zh", "font_size": 14}`
- **单词翻译**：`{"apple": "苹果", "banana": "香蕉"}`
- **学生成绩**：`{"张三": 95, "李四": 88, "王五": 92}`
- **商品信息**：`{"name": "iPhone", "price": 6999, "color": "黑色"}`

## 📝 核心知识点

### 1. 创建字典

```python
# 空字典
empty_dict = {}
print(empty_dict)  # {}

# 使用花括号创建
student = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "score": 95.5
}
print(student)

# 使用dict()函数创建
person = dict(name="李四", age=25, city="上海")
print(person)  # {'name': '李四', 'age': 25, 'city': '上海'}

# 从键值对列表创建
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# 字典可以嵌套
company = {
    "name": "腾讯",
    "employees": 100000,
    "departments": {
        "tech": 50000,
        "product": 30000,
        "sales": 20000
    }
}
```

### 2. 访问字典元素

```python
user = {
    "username": "coder123",
    "email": "coder@example.com",
    "age": 30,
    "is_active": True
}

# 使用键访问值
print(user["username"])  # "coder123"
print(user["email"])     # "coder@example.com"

# 使用get()方法（更安全，不会报错）
print(user.get("age"))        # 30
print(user.get("city"))       # None（键不存在时返回None）
print(user.get("city", "未知"))  # "未知"（指定默认值）

# 访问嵌套字典
company = {
    "name": "阿里巴巴",
    "info": {
        "founded": 1999,
        "founder": "马云"
    }
}
print(company["info"]["founder"])  # "马云"
```

### 3. 修改字典

```python
# 创建字典
book = {
    "title": "Python编程",
    "author": "Guido",
    "price": 99.9
}

# 添加新键值对
book["pages"] = 500
book["publisher"] = "人民邮电出版社"
print(book)

# 修改现有值
book["price"] = 89.9  # 修改价格
print(book)

# 删除键值对
del book["publisher"]  # 删除出版社信息
print(book)

# 使用pop()删除并返回值
author = book.pop("author")
print(f"作者: {author}")
print(f"删除后: {book}")

# 清空字典
book.clear()
print(book)  # {}
```

### 4. 字典常用方法

```python
inventory = {
    "apple": 10,
    "banana": 20,
    "orange": 15,
    "grape": 8
}

# keys() - 获取所有键
print(inventory.keys())    # dict_keys(['apple', 'banana', 'orange', 'grape'])

# values() - 获取所有值
print(inventory.values())  # dict_values([10, 20, 15, 8])

# items() - 获取所有键值对
print(inventory.items())   # dict_items([('apple', 10), ('banana', 20), ...])

# in 操作符 - 检查键是否存在
print("apple" in inventory)   # True
print("watermelon" in inventory)  # False

# len() - 获取字典长度（键值对数量）
print(len(inventory))  # 4

# update() - 合并字典
new_items = {"pear": 12, "kiwi": 5}
inventory.update(new_items)
print(inventory)

# copy() - 复制字典
inventory_copy = inventory.copy()
print(inventory_copy)
```

### 5. 遍历字典

```python
student = {
    "name": "王五",
    "age": 20,
    "major": "计算机科学",
    "gpa": 3.8
}

# 遍历所有键
print("学生信息键:")
for key in student:
    print(f"  {key}")

# 遍历所有值
print("学生信息值:")
for value in student.values():
    print(f"  {value}")

# 遍历所有键值对
print("完整学生信息:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 遍历嵌套字典
school = {
    "student1": {"name": "张三", "score": 95},
    "student2": {"name": "李四", "score": 88},
    "student3": {"name": "王五", "score": 92}
}

print("所有学生成绩:")
for student_id, info in school.items():
    name = info["name"]
    score = info["score"]
    print(f"  {student_id}: {name} - {score}分")
```

### 6. 字典推导式

```python
# 创建数字平方字典
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 过滤字典
inventory = {"apple": 10, "banana": 0, "orange": 15, "grape": 8}
available = {item: qty for item, qty in inventory.items() if qty > 0}
print(available)  # {'apple': 10, 'orange': 15, 'grape': 8}

# 转换字典
prices = {"apple": 5, "banana": 3, "orange": 4}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)  # {'apple': 4.5, 'banana': 2.7, 'orange': 3.6}
```

### 7. 字典的排序

```python
scores = {"张三": 95, "李四": 88, "王五": 92, "赵六": 78}

# 按键排序
sorted_by_name = dict(sorted(scores.items()))
print("按姓名排序:", sorted_by_name)

# 按值排序（从高到低）
sorted_by_score = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print("按成绩排序:", sorted_by_score)

# 获取最高分和最低分
highest = max(scores, key=scores.get)
lowest = min(scores, key=scores.get)
print(f"最高分: {highest}({scores[highest]}分)")
print(f"最低分: {lowest}({scores[lowest]}分)")
```

## 🎯 练习项目

### 项目1：学生成绩管理系统
创建一个学生成绩管理系统，使用字典存储学生信息。

### 项目2：单词翻译器
创建一个简单的英汉词典，实现单词查询和添加功能。

### 项目3：用户信息管理系统
管理用户信息，支持添加、删除、修改和查询用户。

## 💡 学习建议

1. **理解键值对概念**：这是字典的核心思想
2. **掌握常用方法**：keys()、values()、items()、get()等
3. **学会安全访问**：使用get()方法避免KeyError
4. **熟练遍历字典**：掌握多种遍历方式
5. **理解字典推导式**：这是Python的优雅特性

## 🚀 下一步学习

掌握了字典后，你将学习：
- **Day09**: 集合（Set） - 无序不重复元素集合
- **Day10**: 字符串（String）高级操作
- **Day11**: 函数进阶
- **Day12**: 文件操作

字典是Python编程中**使用频率最高的数据结构**，掌握了它，你的Python编程能力将大幅提升！