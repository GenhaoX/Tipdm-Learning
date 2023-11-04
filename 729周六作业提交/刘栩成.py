#!/usr/bin/env python
# coding: utf-8

# # 1.通过input输入一个字符，并判断它的类型，然后输出它是什么类型。 可以无限次输入，直至自己输入‘退出’才会结束。 例如：
# [1,24] --->print('您输入的是列表') 
#     Csd --->print('您输入的是字符串')

# In[1]:


while True:
    user_input = input("请输入一个字符（输入'退出'结束）：")
    
    if user_input == '退出':
        print("程序已结束。")
        break
    
    if isinstance(eval(user_input), str):
        print("您输入的是字符串")
    elif isinstance(eval(user_input), list):
        print("您输入的是列表")
    elif isinstance(eval(user_input), dict):
        print("您输入的是字典")
    elif isinstance(eval(user_input), tuple):
        print("您输入的是元组")
    else:
        print("您输入的是其他类型")


# # 2.将字符串 去重并从小到大排序输出， 排序可用sorted()。                                         例如s = “ajldjlajfdljfddd”---->”adfjl”。

# In[6]:


s='ajldjlajfdljfddd'
set(s)
sorted(set(s))


# # 3.根据num.txt，设计函数，计算每个小列表里面的平均人数。 例如：
# 
# ['1000人以上'] ----> 1000
# ['50-150人'] ----> （150+50）/2 = 100,
# [''] ----> 0
# 最终结果保存在列表中，例如：[['50-150人'], [''],['1000人以上'] ] --> [100,0,1000,...]

# In[22]:


with open('C:/Users/84525/Desktop/python基础/data/num.txt') as f:
    data=f.readlines()
    print(data)


# In[18]:


num=data.replace('"','').split(',')
num


# In[ ]:





# In[20]:


path=('C:/Users/84525/Desktop/python基础/data/num.txt')
with open(path, 'r') as f:
    num=f.read()
num


# In[21]:


import re
num1=num
numbers=[]
for i in eval(num1):
    numbers.extend(eval(i))
    

number_detil=[]
for i in numbers:
    number_detil.append(re.findall(r'\d+', i)) 
    
    
avg_number = []
for i in number_detil:
    if len(i) > 0:
        avg = sum([int(x) for x in i]) / len(i)
        avg_number.append(avg)
    else:
        avg_number.append(0)  # 设置默认值为0

avg_number


# # 4.定义了一个 Car 类，它有 brand、model 和 year 属性，表示汽车的品牌、型号和制造年份。还有 speed 属性表示当前车速。
# 类中定义三个方法：accelerate（加速）、brake（刹车）和 get_speed（获取速度）。
# accelerate可以输入加速参数increment表示加速了多少，输出经过加速后汽车的速度
# brake可以输入参数decrement表示减速了多少，输出减速后的汽车速度
# get_speed可以获取当前汽车的速度

# In[49]:


class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        
    def accelerate(self,increment):
        self.speed1 = increment + self.speed
         
    def brake(self,decrement):
        self.speed2 = decrement - self.speed
        if self.speed < 0:
            self.speed = 0
    
    def get_speed(self):
        return self.speed


# In[32]:


mycar = Car(brand='tesla1', model='model S', year=2022)


# # 5.内容判断
# 
# a = [1,2,3] 与 b = [3,2,1]，两个列表中的内容是一样的，怎么判断出来？
# 
# 提示：集合

# In[50]:


a = [1, 2, 3]
b = [3, 2, 1]

set_a = set(a)
set_b = set(b)

if set_a == set_b:
    print("列表 a 和列表 b 的内容相同")
else:
    print("列表 a 和列表 b 的内容不同")


# #  6.（os、shutil模块的内容） 创建一个函数copy_directory，传入两个参数source_dir、destination_dir分别表示源文件夹和目标文件夹。 该函数作用是判断目标文件夹是否存在，如果不存在则新建，如果存在则把源文件夹下所有的内容复制到目标文件夹里面。

# In[54]:


import os
import shutil

def copy_directory(source_dir, destination_dir):
    # 判断目标文件夹是否存在，如果不存在则新建
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print("文件夹创建成功")

    # 复制操作
    for item in os.listdir(source_dir):
        # 文件路径的拼接
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)
        if os.path.isdir(source_item):
            # 如果是子文件夹，则递归方法来复制子文件夹
            copy_directory(source_item, destination_item)
        else:
            # 如果是文件，则使用 shutil.copy2 进行复制操作
            shutil.copy2(source_item, destination_item)
    print("复制成功")


    
    
    


# In[ ]:





# In[ ]:




