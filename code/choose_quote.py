import random
import re


def choose_quote(file_path):
    try:
        # 读取文件中所有的行
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        # 移除每行末尾的换行符，并使用正则表达式移除行首的数字和点
        lines = [re.sub(r'^\d+\.', '', line.strip()) for line in lines if line.strip()]
        # 从列表中随机选择一行
        selected_line = random.choice(lines)
        # 打印选中的行
        # print(selected_line)
        return selected_line

    except Exception as e:
        print(f"发生错误：{e}")


file_path = 'quotes.txt'
choose_quote(file_path)
