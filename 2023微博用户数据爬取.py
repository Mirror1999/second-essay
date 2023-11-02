# -*- coding:utf-8 -*-
# @time: 2023/10/31 10:00
# @Author: Mirror1999
# @Environment: Python 3.7
import json
import requests
import csv
import time
import chardet # 数据乱码


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Referer": "https://weibo.com"
    }
    cookies = {
    	"cookie": '在次数输入自己的cookies' }
    response = requests.get(url, headers=headers, cookies=cookies)
    time.sleep(3)   # 加上3s 的延时防止被反爬
    return response.text


# def save_data(data):
    
    # data为dict类型
    # 有的值有'description', 'followers_count', 'friends_count', 'statuses_count', 'location', 'gender', 
    # 'verified', 'verified_reason', 'birthday', 'created_at', 'sunshine_credit', 'company', 'school','name'
    
    
    
    
#     title = [ 'description', 'followers_count', 'friends_count', 'statuses_count', 'location', 'gender', 'verified', 'verified_reason', 'birthday', 'created_at', 'sunshine_credit', 'company', 'school','name']
#     with open("G:\\论文\\毕业论文\\数据\\爬虫_data.txt", "a", encoding='utf-8-sig', newline="")as fi:
#         fi = csv.writer(fi)
#         fi.writerow([data[k] for k in title])

def save_data1(data):
    with open('G:\\论文\\毕业论文\\数据\\爬虫_data.txt','a',encoding = 'utf-8-sig') as f1:
        f1.write(str(data))
        f1.write('\n')
    
    


def get_data(id):
    url1 = "https://weibo.com/ajax/profile/info?uid={}".format(id)
    url2 = "https://weibo.com/ajax/profile/detail?uid={}".format(id)
    
    html1 = get_html(url1)
    responses1 = json.loads(html1)
#     response = requests.get(url1)
    data1 = responses1['data']['user']

    html2 = get_html(url2)
    responses2 = json.loads(html2)
    data2 = responses2['data']

    data = {}   # 新建个字典用来存数据
#     data['name'] = data1['name']  # 名字
#     data['description'] = data1['description']  # 个人简介
    
    try:
        data['description'] = data2['description']  # 个人简介
    except KeyError:
        data['description'] = ""

        
    data['verified'] = data1['verified']  # 是否认证
    
    try:
        data['verified_reason'] = data2['verified_reason']  # 认证信息
    except KeyError:
        data['verified_reason'] = ""
    data['followers_count'] = data1['followers_count']  # 粉丝数量
    data['friends_count'] = data1['friends_count']  # 关注数量
    data['statuses_count'] = data1['statuses_count']  # 博文数量
    data['location'] = data1['location']  # 所在地区
    data['gender'] = data1['gender']  # 性别：f:女, m:男


    try:
        data['birthday'] = data2['birthday']  # 生日
    except KeyError:
        data['birthday'] = ""
    try:
        data['created_at'] = data2['created_at']  # 注册时间
    except KeyError:
        data['created_at'] = ""
    try:
        data['sunshine_credit'] = data2['sunshine_credit']['level']  # 阳光信用
    except KeyError:
        data['sunshine_credit'] = ""
    try:
        data['company'] = data2['career']['company']  # 公司
    except KeyError:
        data['company'] = ""
    try:
        data['school'] = data2['education']['school']  # 学校
    except KeyError:
        data['school'] = ""
    
    try:
        data['name'] = data2['name'] # 真实姓名
    except KeyError:
        data['name'] = ""
    try:
        data['label_desc'] = data2['label_desc'] # 互动信息，互动得多，可以相信是开放的，否则是不开放的
    except KeyError:
        data['label_desc'] = ""     
    
    
    save_data1(data)
#     print(data)
    


if __name__ == '__main__':
    uid = df_Weibo100
    for id in uid:
        try:        
            get_data(id)
        except:
            pass
print('finished')
