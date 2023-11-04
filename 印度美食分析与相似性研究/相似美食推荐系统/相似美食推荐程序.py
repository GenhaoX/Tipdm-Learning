
#找到次.py文件路径,打开cmd使用python 相似美食推荐程序.py运行
import tkinter as tk
import pandas as pd
import numpy as np

df = pd.read_csv('clean_data.csv')
df.drop(columns='Unnamed: 0',inplace=True)
# df.head()
cos_matrix = np.load("cosine_similarity_matrix.npy")

def recommend_similar_food():
    food = entry.get()  # 获取用户输入的美食名称
    target_index = df[df["name"] == food].index[0]
    cos_matrix[target_index][target_index] = 0      # 将与自身余弦相似值设为0，避免干扰
    result_text.delete(1.0, tk.END)  # 清空结果文本框
    result_text.insert(tk.END, f"为 {food} 推荐相似美食：\n")
    target_vector = cos_matrix[target_index]
    top_indices = target_vector.argsort()[-10:][::-1]
    for i, index in enumerate(top_indices):
        similarity_value = cos_matrix[target_index][index]
        result_text.insert(
            tk.END, f"NO.{i+1}：索引值:{index}  名称:{df.loc[index]['name']}  推荐系数:{similarity_value}\n"
        )

# 创建主窗口
window = tk.Tk()
window.title("相似美食推荐")
window.geometry("400x300")

# 创建标签和输入框
label = tk.Label(window, text="请输入您喜欢的美食名称：")
label.pack()
entry = tk.Entry(window)
entry.pack()

# 创建按钮
button = tk.Button(window, text="推荐相似美食", command=recommend_similar_food)
button.pack()

# 创建结果文本框
result_text = tk.Text(window, height=10)
result_text.pack()

# 运行主循环
window.mainloop()