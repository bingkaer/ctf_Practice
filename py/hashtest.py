#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/8/26 19:01
# @Author  : tushanfirm
# @File    : hashtest.py
# @Software: PyCharm
import hashlib

filename = input("Enter file name: \n")
md5_filename = hashlib.md5(filename.encode('utf-8')).hexdigest()
print(md5_filename)

cookie_secret = '859efc33-3d48-4658-ab24-620b559e033e'
new_field = cookie_secret + md5_filename
new_md5 = hashlib.md5(new_field.encode('utf-8')).hexdigest()
print(new_md5)