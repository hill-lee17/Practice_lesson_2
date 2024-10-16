import os
from datetime import datetime

import pymysql
from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from flask_cors import CORS
import time

import choose_quote
import data_deal
import hot_search_spider
import spider
import weibo_api
from pic_detec import Nude

app = Flask(__name__)
CORS(app)

app.secret_key = 'caw465zxc156e4a6w4e5dzxzvc1fdsdad'  # 设置一个密钥，用于 session

spider_finish = False


@app.route('/')
def home():
    if session.get('username') is None:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        admin_name = request.form.get('adminName')
        admin_pwd = request.form.get('adminPwd')
        sql = "select id from users where username= %s and password= %s"
        res = execute(sql, admin_name, admin_pwd)
        if res:
            session['username'] = admin_name
            return jsonify({'status': 'success', 'redirect_url': 'index'})
        else:
            return jsonify({'status': 'fail'})
    else:
        return render_template('login.html')


@app.route('/logout', methods=['POST'])
def logout():
    # 清除session中的用户信息
    if request.method == 'POST' and session.get('username'):
        session.pop('username', None)  # 假设您使用'user_id'来存储登录用户的ID
        # 如果需要完全删除session，可以使用session.clear()
        return '您已成功退出登录'


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET' and session.get('username'):
        return render_template('index.html')
    elif request.method == 'GET' and not session.get('username'):
        return redirect(url_for('login'))


@app.route('/hot_search', methods=['GET', 'POST'])
def hot_search():
    if request.method == 'GET' and session.get('username'):
        hot_search_data = hot_search_spider.spider_main(20)
        return render_template('table.html', hot_search_data=hot_search_data, current_time=datetime.now().strftime('%Y年%m月%d日 %H:%M'))
    elif request.method == 'GET' and not session.get('username'):
        return redirect(url_for('login'))


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'GET' and session.get('username'):
        return render_template('send.html')
    elif request.method == 'GET' and not session.get('username'):
        return redirect(url_for('login'))
    elif request.method == 'POST' and session.get('username'):
        topic = request.form.get('topic')
        content = request.form.get('content')
        print(topic)
        print(content)
        weibo_api.send(content+'#'+topic+'#')
        response = f"发送成功！<br>详见页面：https://m.weibo.cn/"
        return response


@app.route('/muti_send', methods=['POST'])
def muti_send():
    if request.method == 'POST' and session.get('username'):
        topic = request.form.get('topic')
        print(topic)
        for i in range(0, 5):
            weibo_api.send(choose_quote.choose_quote('quotes.txt') + '#'+topic+'#')
            time.sleep(1)
        response = f"发送成功！<br>详见页面：https://m.weibo.cn/"
        return response


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'GET' and session.get('username'):
        return render_template('comment.html')
    elif request.method == 'GET' and not session.get('username'):
        return redirect(url_for('login'))
    elif request.method == 'POST' and session.get('username'):
        id = request.form.get('id')
        content = request.form.get('content')
        print(id)
        print(content)
        weibo_api.comment(content, id)
        response = f"发送成功！<br>详见页面：https://m.weibo.cn/detail/{id}"
        return response


@app.route('/muti_comment', methods=['POST'])
def muti_comment():
    if request.method == 'POST' and session.get('username'):
        id = request.form.get('id')
        print(id)
        for i in range(0, 5):
            weibo_api.comment(choose_quote.choose_quote('quotes.txt'), id)
            time.sleep(1)
        response = f"发送成功！<br>详见页面：https://m.weibo.cn/detail/{id}"
        return response


@app.route('/get_username')
def get_username():
    if session.get('username'):
        username = session.get('username')
        return jsonify({'loggedInUsername': username})


@app.route('/get_keywords')
def get_keywords():
    return data_deal.get_keywords()


@app.route('/detect', methods=['POST'])
def detect_nudity():
    # 检查是否有文件在请求中
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']

    # 如果用户没有选择文件，浏览器可能会提交一个没有文件名的空部分
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # 将上传的文件保存到临时路径，或者直接传递文件流到Nude类
        with open('temp.jpg', 'wb') as f:
            f.write(file.read())

        # 创建Nude对象并进行检测
        n = Nude('temp.jpg')
        n.parse()
        result = n.result
        inspect = n.inspect()
        # 清理临时文件
        os.remove('temp.jpg')
        print(result)
        print(inspect)
        return jsonify({'result': result, 'inspect': inspect})


@app.route('/get_spider_info')
def get_spider_info():
    try:
        with open('../spider_data/data/data.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "文件未找到", 404




@app.route('/get_user_info', methods=['GET', 'POST'])
def get_user_info():
    global spider_finish
    if request.method == 'GET' and session.get('username'):
        # 仅在GET请求时渲染空表单页面
        return render_template('form.html', user_info={})
    elif request.method == 'GET' and not session.get('username'):
        return redirect(url_for('login'))
    elif request.method == 'POST':
        user_id = request.form.get('id')  # 从POST请求中获取用户ID
        if user_id:
            user_info = spider.get_userInfo(user_id)  # 使用user_id调用爬虫函数
            file = 'C:\\Users\\LENOVO\\Desktop\\lesson\\code\\spider_data\\' + 'data'+'\\' + 'data.txt'
            directory = os.path.dirname(file)
            if not os.path.exists(directory):
                os.makedirs(directory)
            spider.get_weibo(user_id, file)
            return jsonify(user_info)
        else:
            # 如果没有ID，返回页面并显示错误信息或保持空的用户信息
            return jsonify({})


def get_conn():
    # 建立与mysql连接
    conn = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="my_test", charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):  # 关闭连接
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def execute(sql, *args):  # 执行数据库语句函数
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    conn.commit()
    close_conn(conn, cursor)
    return res


if __name__ == '__main__':
    app.run(debug=True, port=5000)
