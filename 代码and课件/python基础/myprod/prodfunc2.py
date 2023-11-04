# -*- coding: UTF8 -*-

import sys
def prods(x):
    """
    :param x: 一个整数
    :returns: 无返回值，直接打印结果
    """
    for i in range(1,int(x)+1):
        a = ''
        for j in range(1,i+1):
            a = a+' '+f'{i}*{j}={i*j}'
        print(a)

# 调用.py文件时执行以下代码
if __name__=='__main__':
    try:
        x = sys.argv[1]
        y = sys.argv[2]
        prods(x)
        print(y)
    except:
        pass
    
    prods(5)