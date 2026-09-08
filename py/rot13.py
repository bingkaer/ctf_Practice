#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/8/22 15:43
# @Author  : tushanfirm
# @File    : rot13.py
# @Software: PyCharm
import codecs

encrypted = "afZ_r9VYfScOeO_UL^RWUc"
decrypted = codecs.decode(encrypted, "rot13")
print(decrypted)
# 输出: flag{5pq1004q-86n5-46q8-o720-oro5on0417r1}
