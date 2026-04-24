# Day08 字典基础练习
# 完成以下12个练习，掌握字典的基本操作

def main():
    print("=== Day08 字典基础练习 ===")
    print("请完成以下练习，取消注释并运行测试\n")
    
    # 练习1：创建字典
    print("1. 创建字典")
    # 创建一个学生字典，包含以下信息：
    # 姓名：张三，年龄：18，性别：男，成绩：95.5
    student = {"name": "张三", "age": 18, "gender": "男", "score": 95.5}
    print(student)
    
    # 练习2：访问字典元素
    print("\n2. 访问字典元素")
    # 使用字典student，打印学生的姓名和成绩
    print(f"姓名: {student['name']}")
    print(f"成绩: {student['score']}")
    
    # 练习3：使用get()方法
    print("\n3. 使用get()方法")
    # 使用get()方法获取学生的城市信息，如果不存在则返回"未知"
    city = student.get("city", "未知")
    print(f"城市: {city}")
    
    # 练习4：添加新键值对
    print("\n4. 添加新键值对")
    # 向student字典添加"班级"信息，值为"高三(1)班"
    student["class"] = "高三(1)班"
    print(student)
    
    # 练习5：修改字典值
    print("\n5. 修改字典值")
    # 将学生的成绩修改为97.0
    student["score"] = 97.0
    print(f"修改后成绩: {student['score']}")
    
    # 练习6：删除键值对
    print("\n6. 删除键值对")
    # 删除学生的性别信息
    del student["gender"]
    print(student)
    
    # 练习7：获取所有键
    print("\n7. 获取所有键")
    # 获取student字典的所有键并打印
    keys = student.keys()
    print(f"所有键: {keys}")
    
    # 练习8：获取所有值
    print("\n8. 获取所有值")
    # 获取student字典的所有值并打印
    values = student.values()
    print(f"所有值: {values}")
    
    # 练习9：遍历字典
    print("\n9. 遍历字典")
    # 使用items()方法遍历student字典，打印所有键值对
    for key, value in student.items():
        print(f"{key}: {value}")
    
    # 练习10：嵌套字典
    print("\n10. 嵌套字典")
    # 创建一个学校字典，包含多个学生信息
    school = {
        "student1": {"name": "张三", "score": 95},
        "student2": {"name": "李四", "score": 88},
        "student3": {"name": "王五", "score": 92}
    }
    # 打印李四的成绩
    print(f"李四的成绩: {school['student2']['score']}")
    
    # 练习11：字典推导式
    print("\n11. 字典推导式")
    # 使用字典推导式创建1-5的数字平方字典
    squares = {x: x**2 for x in range(1, 6)}
    print(f"数字平方: {squares}")
    
    # 练习12：字典排序
    print("\n12. 字典排序")
    # 有一个成绩字典，按分数从高到低排序
    scores = {"张三": 95, "李四": 88, "王五": 92, "赵六": 78}
    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    print(f"按成绩排序: {sorted_scores}")

if __name__ == "__main__":
    main()