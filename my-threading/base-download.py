#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
这里是一个没开启线程的下载20个文件的py程序
"""


import urllib.request
import time


def download_image(url, filename):
    print("从{}下载文件...".format(url))
    urllib.request.urlretrieve(url, filename)


def main():
    for i in range(20):
        textName = 'temp/jiari-{}.rar'.format(i)
        download_image('http://www.yftxt.com/uploads/soft/1706/%B3%C7%C3%C5%BF%AA_%D3%EA%B7%E3%D0%F9Rain8.com.txt.rar',
                       textName)


if __name__ == '__main__':
    t0 = time.time()
    main()
    t1 = time.time()
    print("耗时：", t1-t0)

