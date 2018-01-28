#!/usr/bin/env pyton
#__author:  CuiShuai
#date: 2018/1/10

import time
import csv
import  requests
import threading
from concurrent import futures
from collections import namedtuple

header = ["aid","view","danmaku","reply","favorite","coin","share"]
Video = namedtuple('Video',header)
headers = {
    'X-Requestd-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36'
    '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/573.36'
}

totle = 1
result = []
lock = threading.Lock()

def run(url):
    """load data
    """
    global totle
    req = requests.get(url,headers=headers,timeout=6).json()
    time.sleep(0.5)   #每个连接请求的时间间隔，避免ip被封
    try:
        data = req['data']
        video = Video(
            data['aid'],
            data['view'],
            data['danmaku'],
            data['reply'],
            data['favorite'],
            data['coin'],
            data['share']
        )
        with lock:
            result.append(video)
            print(totle)
            totle += 1
    except:
        pass

def save():
    """将数据保存到本地
    """
    with open('result.csv','w+',encoding='utf-8') as f:
        f_csv = csv.writer(f)        #创建一个csv文件
        f_csv.writerow(header)       #填写csv的表头
        f_csv.writerows(result)      #将数据存入csv、文件

if __name__ == '__main__':
    urls = ["http://api.bilibili.com/archive_stat/stat?aid={}".format(i) for i in range(1000)]  #取1000个
    with futures.ThreadPoolExecutor(32) as executor:
        executor.map(run,urls)  #多线程跑
    save()
