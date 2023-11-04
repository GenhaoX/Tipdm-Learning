# -*- coding: UTF8 -*-

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

prods(9)

if __name__=='__main__':
    prods(5)