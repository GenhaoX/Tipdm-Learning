import tkinter as tk
import pandas as pd
import numpy as np
from tkinter import ttk
from tkinter import font
from tkinter import messagebox

df = pd.read_csv('clean_data.csv')
df.drop(columns='Unnamed: 0',inplace=True)
cos_matrix = np.load("cosine_similarity_matrix.npy")
#由美食查找城市
def food_of_state():   #相似美食推荐
    food = dropdown1.get()  # 获取用户输入的美食名称
    if food in df["name"].values:
        target_index = df[df["name"] == food].index[0]
        food_state = df['state'][target_index]
        result_text.insert(tk.END, f"在{food_state}能找到这种美食\n")
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
#清空文本内容函数
def clear_text():
    result_text.delete(1.0, tk.END)
#退出程序函数
def quit_app():
    if messagebox.askokcancel("退出", "确定要退出应用程序吗？"):
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
window.title("印度美食推荐系统                                               \t\t\t\t\t            GenhaoX")
window.geometry("700x500")
window.my_font_tip=font.Font(family="微软雅黑",size=10,slant=font.ITALIC)#提示词字体
window.my_font_input=font.Font(family="微软雅黑",size=10)#提示词字体

style = ttk.Style()
style.configure('TCombobox', foreground='gray', font=('Arial', 10, 'italic'))
style.map('TCombobox',
          fieldforeground=[('readonly', 'gray'), ('!disabled', 'black')],
          fieldbackground=[('readonly', 'white'), ('!disabled', 'white')])
# # 创建标签和输入框
label0 = tk.Label(window, text="面向旅游用户的美食推荐小程序",font=("华文行楷", 18), fg="green")
label0.place(x=165,y=2)
label1 = tk.Label(window, text="Food   name：",font=("Times New Roman", 15), fg="black")
label1.place(x=50,y=44)
# entry2 = tk.Entry(window,width=20,font=window.my_font_tip,bd=1, fg='gray')
# entry2.insert(0, "请输入美食英文名称")  # 设置注释提示词
# entry2.place(x=160,y=45)
# def on_entry_click1(event):
#     if entry2.get() == "请输入美食英文名称":
#         entry2.delete(0, tk.END)
#         entry2.config(fg='black',font=window.my_font_input)
# entry2.bind('<FocusIn>', on_entry_click1)
dropdown1 = ttk.Combobox(window, width=18,values=list(set(df["name"])))
dropdown1.set("请输入或选择美食")
dropdown1.place(x=160,y=45)
#第二行********************
label2 = tk.Label(window, text="State   name：",font=("Times New Roman", 15), fg="black")
label2.place(x=50,y=95)
# entry1 = tk.Entry(window,width=20,font=window.my_font_tip,bd=1, fg='gray')
# entry1.insert(0, "请输入州英文名称")  # 设置注释提示词
# entry1.place(x=160,y=97)
# def on_entry_click2(event):
#     if entry1.get() == "请输入州英文名称":
#         entry1.delete(0, tk.END)
#         entry1.config(fg='black',font=window.my_font_input)
# entry1.bind('<FocusIn>', on_entry_click2)
dropdown2 = ttk.Combobox(window, width=18,values=list(set(df["state"])))
dropdown2.set("请输入或选择州")
dropdown2.place(x=160,y=97)
#第三行********************
label3 = tk.Label(window, text="Flavor/Course：",font=("Times New Roman", 13), fg="black")
label3.place(x=50,y=143)
# entry3 = tk.Entry(window,width=20,font=window.my_font_tip,bd=1, fg='gray')
# entry3.insert(0, "请输入美食的风味或类型")  # 设置注释提示词
# entry3.place(x=160,y=146)
# def on_entry_click3(event):
#     if entry3.get() == "请输入美食的风味或类型":
#         entry3.delete(0, tk.END)
#         entry3.config(fg='black',font=window.my_font_input)
# entry3.bind('<FocusIn>', on_entry_click3)
dropdown3 = ttk.Combobox(window, width=18,values=['bitter', 'other', 'sour', 'spicy', 'sweet','dessert', 'main course', 'snack', 'starter'])
dropdown3.set("请输入或选择风味/类型")
dropdown3.place(x=160,y=146)
# 添加一个箭头
label4 = tk.Label(window, text="--->",font=("微软雅黑", 15), fg="black")
label4.place(x=310,y=39)
label5 = tk.Label(window, text="--->",font=("微软雅黑", 15), fg="black")
label5.place(x=310,y=88)
label6 = tk.Label(window, text="--->",font=("微软雅黑", 15), fg="black")
label6.place(x=310,y=138)

# # # 创建按钮
# 第一行******************************
button1 = tk.Button(window, text="美食所在州", command=food_of_state,width=18)
button1.place(x=360,y=40)
button2 = tk.Button(window, text="推荐相似美食", command=recommend_similar_food,width=18)
button2.grid(row=1, column=1,sticky='w')
button2.place(x=505,y=40)
#第二行********************************
button3 = tk.Button(window, text="查找推荐美食风味", command=state_to_flavor,width=18)
button3.place(x=360,y=90)
button5 = tk.Button(window, text="查找推荐美食类型", command=state_to_crouse,width=18)
button5.place(x=505,y=90)
#第三行*********************
button4 = tk.Button(window, text="查找推荐的城市", command=course_and_flavor,width=39)
button4.place(x=360,y=140)
# button6 = tk.Button(window, text="查找该类型推荐的城市", command=course_to_state,width=18)
# button6.place(x=505,y=140)

result_text = tk.Text(window, font=("微软雅黑", 12),height=11,width=65)
result_text.place(x=50,y=200)#x加40,y加90

clear_button = tk.Button(window, text="清空文本", command=clear_text,width=12)
clear_button.place(x=60,y=450)#x加40,y加90
quit_button = tk.Button(window, text="退出程序", command=quit_app,width=12)
quit_button.place(x=535,y=450)#x加40,y加90

window.mainloop()