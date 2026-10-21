"""
实验二：基于流程控制的植物养护建议系统（不封装函数版本）
========================================================
全部逻辑以顺序结构与流程控制语句（while / if / elif / else）直接实现，不定义任何函数
"""
# 合法的叶片颜色取值
VALID_COLORS = ["绿色", "黄色", "褐色", "枯萎"]

# 各类状态计数，继续后添加
status_count = {"正常": 0, "浇水": 0, "排水": 0, "缺氮": 0, "缺水": 0, "紧急": 0}
total = 0  # 总诊断次数

print("=" * 42)
print("      植物养护建议系统（流程控制实验）")
print("=" * 42)

# while 循环：连续诊断
while True:
    name = input("\n请输入植物名称：").strip()
    if not name:                           # 名称非空校验
        print("  植物名称不能为空，请重新输入。")
        continue
# 叶片颜色输入校验
    while True:
        color = input("叶片颜色（绿色/黄色/褐色/枯萎）：").strip()
        if color in VALID_COLORS:
            break
        print("  输入无效，请重新输入（绿色/黄色/褐色/枯萎）。")

# 土壤湿度输入校验
    while True:
        raw = input("土壤湿度（0-100 整数）：").strip()
        if raw.lstrip("-").isdigit():          # 先确认是纯数字
            humidity = int(raw)
            if 0 <= humidity <= 100:           # 再确认范围
                break
        print("  输入无效，请输入 0-100 之间的整数。")

# 可选：虫害信息录入
    while True:
        pest = input("是否有虫害（有/无）：").strip()
        if pest in ("有", "无"):
            break
        print("  输入无效，请输入 有 或 无。")

# 条件判断：输出养护建议
    if color == "绿色":
        if humidity < 30:                      # 绿色 + 干旱
            tag, advice = "浇水", "土壤干旱，建议浇水"
        elif humidity > 70:                    # 绿色 + 过湿
            tag, advice = "排水", "土壤过湿，注意排水"
        else:                                  # 绿色 + 湿度适中(30-70)
            tag, advice = "正常", "状态良好，继续保持"
    elif color == "黄色":                       # 黄色：缺氮（任意湿度）
        tag, advice = "缺氮", "可能缺氮，建议施用氮肥"
    elif color == "褐色":                       # 褐色：缺水/日灼（任意湿度）
        tag, advice = "缺水", "可能缺水或日灼，建议增加浇水或遮阴"
    else:                                       # 枯萎：紧急（任意湿度）
        tag, advice = "紧急", "严重缺水或病害，建议紧急处理"

    status_count[tag] += 1      # 继续任务累计统计
    total += 1

# 有虫害时追加提示
    extra = "（注意防治虫害）" if pest == "有" else ""
    print(f"【{tag}】{name}{advice}{extra}")

# 是否继续诊断（内层 while 校验 y/n）
    while True:
        cont = input("是否继续？(y/n)：").strip().lower()
        if cont in ("y", "n"):
            break
        print("  输入无效，请输入 y 或 n")
    if cont == "n":
        break

# 退出时输出统计结果
print("\n" + "=" * 42)
print("               本次诊断统计")
print("=" * 42)
print(f"总诊断次数：{total}")
print("各类状态数量：")
for tag, cnt in status_count.items():
    if cnt:
        print(f"  {tag}：{cnt} 次")
print("感谢使用，再见！")
