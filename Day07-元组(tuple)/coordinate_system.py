# Day07 元组项目：坐标系统
# 综合运用元组知识，实现一个简单的坐标系统

def main():
    print("=== 坐标系统 ===")
    print("本程序演示元组在坐标系统中的应用")
    print()
    
    # 1. 创建坐标点
    print("1. 创建坐标点")
    point_a = (3, 4)
    point_b = (7, 2)
    point_c = (1, 9)
    
    print(f"  点A: {point_a}")
    print(f"  点B: {point_b}")
    print(f"  点C: {point_c}")
    print()
    
    # 2. 访问坐标分量
    print("2. 访问坐标分量")
    x_a, y_a = point_a
    print(f"  点A的x坐标: {x_a}")
    print(f"  点A的y坐标: {y_a}")
    print()
    
    # 3. 计算两点之间的距离
    print("3. 计算两点之间的距离")
    # 距离公式：√((x2-x1)² + (y2-y1)²)
    x1, y1 = point_a
    x2, y2 = point_b
    
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(f"  点A{point_a}到点B{point_b}的距离: {distance:.2f}")
    print()
    
    # 4. 坐标点列表
    print("4. 坐标点列表")
    points = [point_a, point_b, point_c]
    print("  所有坐标点:")
    for i, (x, y) in enumerate(points):
        print(f"    点{i+1}: ({x}, {y})")
    print()
    
    # 5. 查找最远的点（离原点(0,0)）
    print("5. 查找离原点最远的点")
    origin = (0, 0)
    farthest_point = None
    farthest_distance = 0
    
    for point in points:
        x, y = point
        distance_to_origin = (x ** 2 + y ** 2) ** 0.5
        if distance_to_origin > farthest_distance:
            farthest_distance = distance_to_origin
            farthest_point = point
    
    print(f"  离原点最远的点: {farthest_point}")
    print(f"  距离: {farthest_distance:.2f}")
    print()
    
    # 6. 计算中心点（所有点的平均值）
    print("6. 计算中心点")
    total_x = 0
    total_y = 0
    
    for x, y in points:
        total_x += x
        total_y += y
    
    center_x = total_x / len(points)
    center_y = total_y / len(points)
    center_point = (center_x, center_y)
    
    print(f"  所有点的中心点: ({center_x:.2f}, {center_y:.2f})")
    print()
    
    # 7. 坐标变换（平移）
    print("7. 坐标平移")
    dx = 5  # x方向平移量
    dy = -3  # y方向平移量
    
    print(f"  平移向量: ({dx}, {dy})")
    print("  平移后的坐标:")
    
    for i, (x, y) in enumerate(points):
        new_x = x + dx
        new_y = y + dy
        print(f"    点{i+1}: ({x}, {y}) → ({new_x}, {new_y})")
    print()
    
    # 8. RGB颜色元组示例
    print("8. RGB颜色元组")
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    
    colors = [red, green, blue, yellow]
    color_names = ["红色", "绿色", "蓝色", "黄色"]
    
    for i, color in enumerate(colors):
        r, g, b = color
        print(f"  {color_names[i]}: RGB{r, g, b}")
    print()
    
    # 9. 学生信息元组
    print("9. 学生信息元组")
    students = [
        ("张三", 18, 95.5),
        ("李四", 19, 88.0),
        ("王五", 20, 92.5)
    ]
    
    print("  学生信息:")
    for name, age, score in students:
        print(f"    姓名: {name}, 年龄: {age}, 成绩: {score}")
    print()
    
    # 10. 元组解包的高级用法
    print("10. 元组解包高级用法")
    data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
    # 获取第一个、最后一个和中间部分
    first, *middle, last = data
    print(f"  第一个元素: {first}")
    print(f"  中间元素: {middle}")
    print(f"  最后一个元素: {last}")
    print()
    
    print("=== 项目完成 ===")
    print("元组在坐标系统、颜色表示、学生信息等场景中非常实用！")
    print("记住：元组不可变，适合存储不需要修改的数据。")

if __name__ == "__main__":
    main()