import tkinter as tk
import pandas as pd
import math
import numpy as np
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

df = pd.read_csv('model_data.csv')
df.drop(columns='Unnamed: 0',inplace=True)
cos_matrix = np.load("cosine_similarity_matrix.npy")
#查看美食详细信息
def food_of_info():   #相似美食推荐
    food = dropdown1.get()  # 获取用户输入的美食名称
    if food in df["name"].values:
        target_index = df[df["name"] == food].index[0]
        food_diet = df['diet'][target_index]
        if food_diet=='vegetarian':
            food_diet = '素食'
        else:
            food_diet = '非素食'
        food_prep_time = df['prep_time'][target_index]
        if math.isnan(food_prep_time):
            food_prep_time = '未知'
        food_cook_time = df['cook_time'][target_index]
        if math.isnan(food_cook_time):
            food_cook_time = '未知'
        food_time = df['total_time'][target_index]
        if math.isnan(food_time):
            food_time = '未知'
        food_flavor_profile = df['flavor_profile'][target_index]
        if food_flavor_profile=='spicy':
            food_flavor_profile='辛辣'
        elif food_flavor_profile=='sweet':
            food_flavor_profile='甜味'
        elif food_flavor_profile == 'other':
            food_flavor_profile='其他口味'
        elif food_flavor_profile == 'bitter':
            food_flavor_profile='苦味'
        else:
            food_flavor_profile='酸味'
        food_course = df['course'][target_index]
        if food_course=='main course':
            food_course='主菜'
        elif food_course=='dessert':
            food_course='甜点'
        elif food_course == 'snack':
            food_course='小吃'
        else:
            food_course='开胃菜'
        food_state = df['state'][target_index]
        food_region = df['region'][target_index]
        if food_region=='East':
            food_region='东部地区'
        elif food_region=='West':
            food_region='西部地区'
        elif food_region == 'North':
            food_region='北部地区'
        elif food_region == 'Other region':
            food_region='其他地区'
        elif food_region == 'North East':
            food_region='东北地区'
        elif food_region == 'South':
            food_region='东北地区'
        else:
            food_region='中部地区'
        food_ingredients = df['ingredients'][target_index]
        result_text.insert(tk.END, f"美食名称：{food}\n成分配料：{food_ingredients}\n类型：{food_diet}，{food_course}\n风味：{food_flavor_profile}\n所在地区：{food_region}\n\
所在州：{food_state}\n制作所花费时间：{food_time}分钟\n准备所需时间：{food_prep_time}分钟\n烹饪所需时间：{food_cook_time}分钟\n")
    elif food=="请输入或选择美食" or food=="":
        result_text.insert(tk.END, f"请输入内容!\n")
    else:
        result_text.insert(tk.END, f"查找不到 {food} 这种美食,请检查您是否拼写有误,名称首字母需大写!\n")
#由城市推荐风味
def state_to_flavor():
    state = dropdown2.get()
    if state in df["state"].values:
        df_flavor_state = pd.pivot_table(data=df,index='state',columns='flavor_profile',values='name',aggfunc='count').reset_index()
        df_flavor_state.fillna(0,inplace=True)
        df_flavor_state.set_index('state',inplace=True)
        df_flavo_sort = df_flavor_state.loc[state].reset_index()
        df_flavo_sort = df_flavo_sort.sort_values(state,ascending=False)
        name1 = df_flavo_sort.iloc[0]["flavor_profile"]
        score1 = df_flavo_sort.iloc[0][state]
        name2 = df_flavo_sort.iloc[1]["flavor_profile"]
        score2 = df_flavo_sort.iloc[1][state]
        if score1 < 5 or score2 == 0:
            result_text.insert(tk.END, f"该州美食风味并不多,推荐以下美食风味：{name1}，美食种数：{score1};\n")
        else:
            result_text.insert(tk.END, f"该州中,推荐以下美食风味：{name1}，美食种数：{score1};\n{name2}，美食种数：{score2}\n")
    elif state=="请输入或选择州" or state=="":
        result_text.insert(tk.END, f"请输入内容!\n")
    else:
        result_text.insert(tk.END, f"查找不到 {state} 这个州,请检查您是否拼写有误,名称首字母需大写!\n")
#由风味推荐城市
def flavor_to_state():
    flavor = dropdown3.get()
    if flavor in df["flavor_profile"].values:
        df_state_flavor = pd.pivot_table(data=df,index='flavor_profile',columns='state',values='name',aggfunc='count').reset_index()
        df_state_flavor.fillna(0,inplace=True)
        df_state_flavor.set_index('flavor_profile',inplace=True)
        df_state_sort = df_state_flavor.loc[flavor].reset_index()
        df_state_sort = df_state_sort.sort_values(flavor,ascending=False)
        name1 = df_state_sort.iloc[0]["state"]
        score1 = df_state_sort.iloc[0][flavor]
        name2 = df_state_sort.iloc[1]["state"]
        score2 = df_state_sort.iloc[1][flavor]
        name3 = df_state_sort.iloc[2]["state"]
        score3 = df_state_sort.iloc[2][flavor]
        if score1 < 5 or score2 == 0:
            result_text.insert(tk.END, f"该美食风味较少,只推荐去这个州：{name1}，美食种数：{score1};\n")
        else:
            result_text.insert(tk.END, f"对于该美食风味,推荐去这三个州：\n{name1}，美食种数：{score1};\n{name2}，美食种数：{score2};\n{name3}，美食种数：{score3}\n")
#由城市推荐类型
def state_to_crouse():
    state = dropdown2.get()
    if state in df["state"].values:
        df_state_course = pd.pivot_table(data=df,index='state',columns='course',values='name',aggfunc='count').reset_index()
        df_state_course.fillna(0,inplace=True)
        df_state_course.set_index('state',inplace=True)
        df_state_sort = df_state_course.loc[state].reset_index()
        df_state_sort = df_state_sort.sort_values(state,ascending=False)
        name1 = df_state_sort.iloc[0]["course"]
        score1 = df_state_sort.iloc[0][state]
        name2 = df_state_sort.iloc[1]["course"]
        score2 = df_state_sort.iloc[1][state]
        if score1 < 5 or score2 == 0:
            result_text.insert(tk.END, f"该州美食类型并不多,推荐以下美食类型：{name1}，美食种数：{score1};\n")
        else:
            result_text.insert(tk.END, f"对于该城市,推荐两种美食类型：\n{name1}，美食种数：{score1};\n{name2}，美食种数：{score2};\n")
    elif state=="请输入或选择州" or state=="":
        result_text.insert(tk.END, f"请输入内容!\n")
    else:
        result_text.insert(tk.END, f"查找不到 {state} 这个城市,请检查您是否拼写有误,名称首字母需大写!\n")
#由类型推荐城市
def course_to_state():
    course = dropdown3.get()
    if course in df["course"].values:
        df_course_state = pd.pivot_table(data=df,index='course',columns='state',values='name',aggfunc='count').reset_index()
        df_course_state.fillna(0,inplace=True)
        df_course_state.set_index('course',inplace=True)
        df_course_sort = df_course_state.loc[course].reset_index()
        df_course_sort = df_course_sort.sort_values(course,ascending=False)
        name1 = df_course_sort.iloc[0]["state"]
        score1 = df_course_sort.iloc[0][course]
        name2 = df_course_sort.iloc[1]["state"]
        score2 = df_course_sort.iloc[1][course]
        name3 = df_course_sort.iloc[2]["state"]
        score3 = df_course_sort.iloc[2][course]
        # result_text.delete(1.0, tk.END)  # 清空结果文本框
        if score1 < 5 or score2 == 0:
            result_text.insert(tk.END, f"该美食类型较少,只推荐去这个州：{name1}，美食种数：{score1};\n")
        else:
            result_text.insert(tk.END, f"对于该美食类型,推荐去这三个州：\n{name1}，美食种数：{score1};\n{name2}，美食种数：{score2};\n{name3}，美食种数：{score3}\n")
#由已知美食推荐相似美食
def recommend_similar_food():   #相似美食推荐
    food = dropdown1.get()  # 获取用户输入的美食名称
    if food in df["name"].values:
        target_index = df[df["name"] == food].index[0]
        cos_matrix[target_index][target_index] = 0      # 将与自身余弦相似值设为0，避免干扰
        # result_text.delete(1.0, tk.END)  # 清空结果文本框
        result_text.insert(tk.END, f"为 {food} 推荐10种相似美食：\n")
        target_vector = cos_matrix[target_index]
        top_indices = target_vector.argsort()[-10:][::-1]
        for i, index in enumerate(top_indices):
            similarity_value = round(cos_matrix[target_index][index],3)
            result_text.insert(
                tk.END, f"NO.{i+1}：索引值:{index}  名称:{df.loc[index]['name']}  \t推荐系数:{similarity_value}\n")
    elif food=="请输入或选择美食" or food=="":
        result_text.insert(tk.END, f"请输入内容!\n")
    else:
        # result_text.delete(1.0, tk.END)  # 清空结果文本框
        result_text.insert(tk.END, f"查找不到 {food} 这种美食,请检查您是否拼写有误,名称首字母需大写!\n")
#对比两美食之间的差异和相似性
def food_diff_and_similar():
    food1 = dropdown4.get()
    food2 = dropdown5.get()
    if food1 in df["name"].values and food2 in df["name"].values:
        target_index1 = df[df["name"] == food1].index[0]
        target_index2 = df[df["name"] == food2].index[0]
        cos_similar = round(cos_matrix[target_index1][target_index2],3)
        ingred1 = df['ingredients'][target_index1]
        diet1 = df['diet'][target_index1]
        flavor1 = df['flavor_profile'][target_index1]
        course1 = df['course'][target_index1]
        ingred2 = df['ingredients'][target_index2]
        diet2 = df['diet'][target_index2]
        flavor2 = df['flavor_profile'][target_index2]
        course2 = df['course'][target_index2]
        if cos_similar >= 0.8:
            result_text.insert(tk.END, f"这两种美食的相似性 较高,相似度为：{cos_similar}\n")
            result_text.insert(tk.END, f"两美食的配料及其他属性为:\n美食1 {food1}：\n    配料：{ingred1}\n    类型：{diet1}，{course1}\n    风味：{flavor1}\n\
美食2 {food2}：\n    配料:{ingred2}\n    类型：{diet2}，{course2}\n    风味：{flavor2}\n")
        elif cos_similar >= 0.5:
            result_text.insert(tk.END, f"这两种美食的相似性 一般,相似度为：{cos_similar}\n")
            result_text.insert(tk.END, f"两美食的配料及其他属性为:\n美食1 {food1}：\n    配料：{ingred1}\n    类型：{diet1}，{course1}\n    风味：{flavor1}\n\
美食2 {food2}：\n    配料:{ingred2}\n    类型：{diet2}，{course2}\n    风味：{flavor2}\n")
        else:
            result_text.insert(tk.END, f"这两种美食的相似性 较低,相似度为：{cos_similar}\n")
            result_text.insert(tk.END, f"两美食的配料及其他属性为:\n美食1 {food1}：\n    配料:{ingred1}\n    类型：{diet1}，{course1}\n    风味：{flavor1}\n\
美食2 {food2}：\n    配料:{ingred2}\n    类型：{diet2}，{course2}\n    风味：{flavor2}\n")
    elif food1 not in df["name"].values:
        # result_text.delete(1.0, tk.END)  # 清空结果文本框
        result_text.insert(tk.END, f"查找不到 {food1} 这种美食,请检查您是否拼写有误,名称首字母需大写!\n")
    elif food2 not in df["name"].values:
        result_text.insert(tk.END, f"查找不到 {food2} 这种美食,请检查您是否拼写有误,名称首字母需大写!\n")
    elif food1=="美食1" or food2=="美食2":
        result_text.insert(tk.END, f"请输入内容!\n")
#清空文本内容函数
def clear_text():
    result_text.delete(1.0, tk.END)
#退出程序函数
def quit_app():
    if messagebox.askokcancel("退出", "确定要退出应用程序吗？\n\t--GenhaoX"):
        window.destroy()
def course_and_flavor():
    name = dropdown3.get()
    if name in df["course"].values:
        return course_to_state()
    elif name in df["flavor_profile"].values:
        return flavor_to_state()
    elif name=="请输入或选择风味/类型" or name=="":
        return result_text.insert(tk.END, f"请输入内容!\n")
    else:
        return result_text.insert(tk.END, f"查找不到 {name} 这种美食风味或类型,请检查您是否拼写有误,名称首字母需大写!\n")
#*********************************************************************************************************************************************
##############################################################################################################################################

# 创建主窗口
window = tk.Tk()
window.title("印度美食推荐系统-------------------------------------------------------------------------------------------------GenhaoX")
window.geometry("800x600")
window.my_font_tip=font.Font(family="微软雅黑",size=10,slant=font.ITALIC)#提示词字体
window.my_font_input=font.Font(family="微软雅黑",size=10)#提示词字体

style = ttk.Style()
style.configure('TCombobox', foreground='gray', font=('Arial', 10, 'italic'))
style.map('TCombobox',
          fieldforeground=[('readonly', 'gray'), ('!disabled', 'black')],
          fieldbackground=[('readonly', 'white'), ('!disabled', 'white')])
# # 创建标签和输入框
label0 = tk.Label(window, text="面向旅游用户的美食推荐小程序",font=("华文行楷", 18), fg="green")
label0.place(x=205,y=2)
label1 = tk.Label(window, text="Food   name：",font=("Times New Roman", 15), fg="black")
label1.place(x=100,y=44)
dropdown1 = ttk.Combobox(window, width=18,values=list(set(df["name"])))
dropdown1.set("请输入或选择美食")
dropdown1.place(x=210,y=45)
#第二行********************
label2 = tk.Label(window, text="State   name：",font=("Times New Roman", 15), fg="black")
label2.place(x=100,y=85)
dropdown2 = ttk.Combobox(window, width=18,values=list(set(df["state"])))
dropdown2.set("请输入或选择州")
dropdown2.place(x=210,y=87)
#第三行********************
label3 = tk.Label(window, text="Flavor/Course：",font=("Times New Roman", 13), fg="black")
label3.place(x=100,y=123)
dropdown3 = ttk.Combobox(window, width=18,values=['bitter', 'other', 'sour', 'spicy', 'sweet','dessert', 'main course', 'snack', 'starter'])
dropdown3.set("请输入或选择风味/类型")
dropdown3.place(x=210,y=126)
#第四行
label4 = tk.Label(window, text="Food1&Food2：",font=("Times New Roman", 13), fg="black")
label4.place(x=100,y=171)
dropdown4 = ttk.Combobox(window, width=18,values=list(set(df["name"])))
dropdown4.set("请输入美食1")
dropdown4.place(x=210,y=162)
dropdown5 = ttk.Combobox(window, width=18,values=list(set(df["name"])))
dropdown5.set("请输入美食2")
dropdown5.place(x=210,y=185)
# 添加一个箭头
label4 = tk.Label(window, text="-->",font=("微软雅黑", 15), fg="black")
label4.place(x=365,y=39)
label5 = tk.Label(window, text="-->",font=("微软雅黑", 15), fg="black")
label5.place(x=365,y=78)
label6 = tk.Label(window, text="-->",font=("微软雅黑", 15), fg="black")
label6.place(x=365,y=118)
label7 = tk.Label(window, text="-->",font=("微软雅黑", 15), fg="black")
label7.place(x=365,y=168)
# # # 创建按钮
# 第一行******************************
button1 = tk.Button(window, text="美食详细信息", command=food_of_info,width=18)
button1.place(x=410,y=40)
button2 = tk.Button(window, text="推荐相似美食", command=recommend_similar_food,width=18)
button2.grid(row=1, column=1,sticky='w')
button2.place(x=555,y=40)
#第二行********************************
button3 = tk.Button(window, text="查找推荐美食风味", command=state_to_flavor,width=18)
button3.place(x=410,y=80)
button5 = tk.Button(window, text="查找推荐美食类型", command=state_to_crouse,width=18)
button5.place(x=555,y=80)
#第三行*********************
button4 = tk.Button(window, text="查找推荐的城市", command=course_and_flavor,width=39)
button4.place(x=410,y=120)
#第四行*********************
button6 = tk.Button(window, text="比较差异与相似性", command=food_diff_and_similar,width=39)
button6.place(x=410,y=168)
#添加输出文本框
result_text = tk.Text(window, font=("微软雅黑", 12),height=15,width=75)
result_text.place(x=58,y=210)#x加40,y加90

clear_button = tk.Button(window, text="清空文本", command=clear_text,width=12)
clear_button.place(x=100,y=535)#x加40,y加90
quit_button = tk.Button(window, text="退出程序", command=quit_app,width=12)
quit_button.place(x=600,y=535)#x加40,y加90

window.mainloop()