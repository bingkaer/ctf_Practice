#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/8/26 09:26
# @Author  : tushanfirm
# @File    : demo_base64.py
# @Software: PyCharm
class CustomBase64 :

    CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0!@#$%^&*()-"

    @classmethod
    def encode ( cls , s : str ) -> str :
        binary_str = '' . join ( format ( ord ( c ), '08b' ) for c in s ) # 转化为二进制字符串
        # print('binary_str:\n'+binary_str)
        padding = 3 - ( len ( s ) % 3 ) if len ( s ) % 3 else 0 # 计算需要的填充
        # print('padding:\n' + str(padding))
        binary_str += '0' * ( padding * 8 )
        # print('binary_str:\n' + binary_str)

        index_strs = [ binary_str [ i : i + 6 ] for i in range ( 0 , len ( binary_str ), 6 )]
        print('index_strs:\n' + str(index_strs))
        # 将每 6 位二进制串转换为十进制整数 int(index_str, 2)
        # 使用该整数作为索引去 CHAR_SET 中查找对应的字符
        encoded = '' . join ( cls . CHAR_SET [ int ( index_str , 2 )] for index_str in index_strs )
        print('encoded:\n' + str(encoded))
        # 之前补的二进制 '0' 也会被编码成字符，但这些字符是无意义的，需要替换为标准的 Base64 填充符 '='
        return encoded [: - padding ] + "=" * padding # 添加填充

    @classmethod
    def decode ( cls , s : str ) -> str :
        padding = s . count ( '=' )
        s = s . rstrip ( '=' )

        binary_str = '' . join ( format ( cls . CHAR_SET . index ( c ), '06b' ) for c in s ) # 转化为二进制字符串
        byte_strs = [ binary_str [ i : i + 8 ] for i in range ( 0 , len ( binary_str ), 8 )][: - padding ]

        decoded = '' . join ( chr ( int ( byte_str , 2 )) for byte_str in byte_strs )

        return decoded

if __name__ == '__main__':
    print(CustomBase64.encode ('hello world'))
