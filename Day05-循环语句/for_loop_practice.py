# 简单购物车
cart_list = ["苹果", "香蕉", "橙子", "葡萄", "草莓"]
price_list = [12, 5, 3, 33, 15]
quantities = [2, 1, 3, 1, 2]
total_price = 0
for i in range(len(cart_list)):
    total_price += price_list[i] * quantities[i]

print("=" * 30)
print("        购物车清单")
print("=" * 30)

print(f"您的购物车总金额为：{total_price}")
# 计算总商品数量
total_items = sum(quantities)  # sum()函数计算列表总和

# 计算平均价格
average_price = total_price / total_items if total_items > 0 else 0

# 找出最贵商品
max_price = max(price_list)
max_index = price_list.index(max_price)  # 找到最贵商品的索引
most_expensive = cart_list[max_index]
print("购物清单详情：")
print("商品        单价  数量  小计")
print("-" * 30)
for index, item in enumerate(cart_list):
    price = price_list[index]
    quantity = quantities[index]
    subtotal = price * quantity
    # 使用字符串格式化对齐列
    print(f"{item:6}    {price:3}元  {quantity:3}   {subtotal:4}元")
print("-" * 30)
print(f"总数量：{total_items}件")
print(f"总金额：{total_price}元")
print(f"平均每件：{average_price:.2f}元")  # :.2f 保留两位小数
print(f"最贵商品：{most_expensive}（{max_price}元）")
