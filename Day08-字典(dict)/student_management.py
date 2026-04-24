# Day08 字典项目：学生成绩管理系统
# 综合运用字典知识，实现一个简单的学生成绩管理系统

def main():
    print("=== 学生成绩管理系统 ===")
    print("本程序演示字典在学生成绩管理中的应用")
    print()
    
    # 1. 创建学生字典
    print("1. 创建学生字典")
    students = {
        "S001": {"name": "张三", "age": 18, "scores": {"语文": 95, "数学": 88, "英语": 92}},
        "S002": {"name": "李四", "age": 19, "scores": {"语文": 88, "数学": 92, "英语": 85}},
        "S003": {"name": "王五", "age": 20, "scores": {"语文": 90, "数学": 95, "英语": 88}}
    }
    
    print("   学生列表:")
    for student_id, info in students.items():
        print(f"     {student_id}: {info['name']} ({info['age']}岁)")
    print()
    
    # 2. 添加新学生
    print("2. 添加新学生")
    students["S004"] = {"name": "赵六", "age": 19, "scores": {"语文": 85, "数学": 90, "英语": 87}}
    print("   添加赵六后的学生列表:")
    for student_id, info in students.items():
        print(f"     {student_id}: {info['name']}")
    print()
    
    # 3. 查询学生信息
    print("3. 查询学生信息")
    student_id = "S002"
    if student_id in students:
        student = students[student_id]
        print(f"   学号 {student_id} 的信息:")
        print(f"     姓名: {student['name']}")
        print(f"     年龄: {student['age']}")
        print(f"     成绩: {student['scores']}")
    else:
        print(f"   学号 {student_id} 不存在")
    print()
    
    # 4. 修改学生成绩
    print("4. 修改学生成绩")
    student_id = "S001"
    subject = "数学"
    new_score = 95
    if student_id in students:
        students[student_id]["scores"][subject] = new_score
        print(f"   修改 {students[student_id]['name']} 的{subject}成绩为: {new_score}")
    print()
    
    # 5. 删除学生
    print("5. 删除学生")
    student_id = "S003"
    if student_id in students:
        removed_student = students.pop(student_id)
        print(f"   删除学生: {removed_student['name']}")
        print(f"   剩余学生数: {len(students)}")
    print()
    
    # 6. 计算平均分
    print("6. 计算平均分")
    for student_id, info in students.items():
        scores = info["scores"]
        average = sum(scores.values()) / len(scores)
        print(f"   {info['name']} 的平均分: {average:.2f}")
    print()
    
    # 7. 按科目统计
    print("7. 按科目统计")
    subjects = ["语文", "数学", "英语"]
    for subject in subjects:
        subject_scores = []
        for student_id, info in students.items():
            if subject in info["scores"]:
                subject_scores.append(info["scores"][subject])
        if subject_scores:
            avg_score = sum(subject_scores) / len(subject_scores)
            max_score = max(subject_scores)
            min_score = min(subject_scores)
            print(f"   {subject}: 平均{avg_score:.1f}分, 最高{max_score}分, 最低{min_score}分")
    print()
    
    # 8. 查找最高分学生
    print("8. 查找最高分学生")
    highest_score = -1
    highest_student = None
    
    for student_id, info in students.items():
        total_score = sum(info["scores"].values())
        if total_score > highest_score:
            highest_score = total_score
            highest_student = info["name"]
    
    print(f"   总分最高的学生: {highest_student} ({highest_score}分)")
    print()
    
    # 9. 使用字典推导式生成成绩报告
    print("9. 成绩报告（字典推导式）")
    # 生成学生总分字典
    total_scores = {info["name"]: sum(info["scores"].values()) for info in students.values()}
    print(f"   学生总分: {total_scores}")
    
    # 按总分排序
    sorted_scores = dict(sorted(total_scores.items(), key=lambda x: x[1], reverse=True))
    print(f"   按总分排名: {sorted_scores}")
    print()
    
    # 10. 复杂嵌套：班级字典
    print("10. 班级管理")
    classes = {
        "高三(1)班": {
            "teacher": "王老师",
            "students": students
        },
        "高三(2)班": {
            "teacher": "李老师",
            "students": {
                "S201": {"name": "孙七", "age": 18, "scores": {"语文": 92, "数学": 88, "英语": 90}},
                "S202": {"name": "周八", "age": 19, "scores": {"语文": 85, "数学": 90, "英语": 87}}
            }
        }
    }
    
    print("   班级信息:")
    for class_name, class_info in classes.items():
        print(f"     {class_name}:")
        print(f"       班主任: {class_info['teacher']}")
        print(f"       学生数: {len(class_info['students'])}")
        for student_id, info in class_info["students"].items():
            print(f"         {info['name']}", end=" ")
        print()
    print()
    
    # 11. 字典的update()方法
    print("11. 合并学生字典")
    new_students = {
        "S005": {"name": "吴九", "age": 18, "scores": {"语文": 88, "数学": 92, "英语": 90}},
        "S006": {"name": "郑十", "age": 19, "scores": {"语文": 90, "数学": 87, "英语": 92}}
    }
    
    # 备份原字典
    students_backup = students.copy()
    students.update(new_students)
    print(f"   合并后学生数: {len(students)}")
    print(f"   新添加学生: {list(new_students.keys())}")
    print()
    
    # 12. 字典的setdefault()方法
    print("12. setdefault()方法示例")
    # 统计每个年龄段的学生数
    age_count = {}
    for student_id, info in students.items():
        age = info["age"]
        age_count.setdefault(age, 0)
        age_count[age] += 1
    
    print(f"   年龄段分布: {age_count}")
    
    print()
    print("=== 项目完成 ===")
    print("字典在学生成绩管理、数据统计等场景中非常实用！")
    print("记住：字典适合存储关联性数据，键值对结构让数据组织更清晰。")

if __name__ == "__main__":
    main()