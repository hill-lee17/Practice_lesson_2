import jieba,math
import jieba.analyse
# ’analyse.extract.tags‘
import re

from flask import jsonify


def remove_content_between_angle_brackets(input_file, output_file):
    try:
        # 打开输入文件
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式替换尖括号之间的内容
        cleaned_content = re.sub(r'<.*?>', '', content)

        # 将清理后的内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_content)

        print(f"Content between angle brackets has been removed and saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


# 使用示例
input_filename = '../spider_data/data/data.txt'  # 替换为你的输入文件名
output_filename = 'output1.txt'  # 替换为你想要保存的输出文件名
remove_content_between_angle_brackets(input_filename, output_filename)




def extract_content_between_tags(input_file, output_file):
    try:
        # 打开输入文件
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式匹配“微博内容”到“点赞数”之间的内容
        pattern = r'微博内容(.*?)点赞数'
        matches = re.findall(pattern, content, re.DOTALL)

        # 将所有匹配到的内容合并为一个字符串
        extracted_content = '\n'.join(matches)

        # 将合并后的内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(extracted_content)

        print(f"Content between '微博内容' and '点赞数' has been extracted and saved to {output_file}")

    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_keywords():
    remove_content_between_angle_brackets('../spider_data/data/data.txt', 'output1.txt')
    extract_content_between_tags('output1.txt', 'output2.txt')
    with open('output2.txt', 'r', encoding='utf-8') as file:
        str_text = file.read()
    keywords1 = jieba.analyse.extract_tags(str_text)
    keywords_top = jieba.analyse.extract_tags(str_text, topK=3)
    total = len(list(jieba.cut(str_text)))
    get_cnt = math.ceil(total * 0.02)  # 向上取整
    keywords_top1 = jieba.analyse.extract_tags(str_text, topK=get_cnt)
    result = {
        'keywords1': keywords1,
        'keywords_top': keywords_top,
        'total': total,
        'get_cnt': get_cnt,
        'keywords_top1': keywords_top1
    }
    return jsonify(result)

