
import requests
from datetime import datetime
from urllib.parse import quote
import csv


def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['排名', '标题', '标签', '链接']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow({
                '排名': item['排名'],
                '标题': item['标题'],
                '标签': item['标签'],
                '链接': item['链接']
            })


def spider_main(num):
    data = hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return

    print(datetime.now().strftime('微博热搜榜 %Y年%m月%d日 %H:%M'))
    hot_search_data = []
    for i, rs in enumerate(data['realtime'][:num], 1):
        title = rs['word']
        try:
            label = rs['label_name']
            if label in ['新', '爆', '沸']:
                label = label
            else:
                label = ''
        except:
            label = ''
        # print(f"{i}. {title} {label} 链接：https://s.weibo.com/weibo?q={quote(title)}&Refer=top")
        hot_search_data.append({
            'rank': i,
            'title': title,
            'label': label,
            'link': f"https://s.weibo.com/weibo?q={quote(title)}&Refer=top"
        })
    print(hot_search_data)
    return hot_search_data
    # save_to_csv(hot_search_data, 'hot_search.csv')


# if __name__ == '__main__':
#     num = 20  # 获取热搜的数量
# spider_main(20)