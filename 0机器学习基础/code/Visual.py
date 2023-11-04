
import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd 


def plot_surface(model, x, y, plt_step=0.02, alpha=1):
    plt.style.use('default')
    plt.rcParams['font.family'] = 'SimHei'   # 设置字体为仿宋
    plt.rcParams['axes.unicode_minus'] = False   # 显示正、负的问题
    fig = plt.figure(figsize=(8,6))
    fig.subplots_adjust(wspace=0.3,hspace=0.3)
    n_classes = len(np.unique(y)) # 类别数
    markers = ('s','x','o','^','v','*','-') # 点样式
    plot_colors = "rybcgkm"[:n_classes] # 颜色数和类别数相等

    if x.shape[1]<=2:  # 只有两列的情况
        col = [[0, 1], [0, 0],[1, 0], [1, 1]]
    elif x.shape[1]==3: # 3列的情况
        col = [[0, 0], [0, 1], [0, 2],[1, 1], [1, 2], [2, 2]]
    else: # 3列以上的情况
        col = [[0, 1], [0, 2], [0, 3],[1, 2], [1, 3], [2, 3]]
    for pairidx, pair in enumerate(col):
        # 选出两列数据用于建模和绘图
        X = np.array(x)[:, pair]  # array([[6.1, 3. ],[7.7, 3. ])
        model.fit(X,y)
        # 找出特征的最大最小值，防止范围溢出
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        # # 生成网格点坐标矩阵
        xx, yy = np.meshgrid(np.arange(x_min, x_max, plt_step),
                             np.arange(y_min, y_max, plt_step))
        # 分子图绘制
        plt.subplot(2, 3, pairidx + 1)
        # xy轴标签
        if type(x)==pd.core.frame.DataFrame:
            plt.xlabel(x.columns[pair[0]], size=12)
            plt.ylabel(x.columns[pair[1]], size=12)
        else:
            plt.xlabel(pair[0], size=12)
            plt.ylabel(pair[1], size=12)          
        # 预测
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) # array([[6.1, 1 ],[6.12, 1 ])
        # 绘制轮廓等高线  alpha参数为透明度
        Z = Z.reshape(xx.shape)
        cs = plt.contourf(xx, yy, Z, alpha=alpha, cmap=plt.cm.RdYlBu) # 绘制曲面

        # 按分类点绘图
        for i, color in zip(range(n_classes), plot_colors):
            idx = np.where(y == i)
            plt.scatter(X[idx, 0], X[idx, 1], c=color, label=np.unique(y)[i],marker = markers[i],
                        cmap=plt.cm.RdYlBu, edgecolor='black', s=15)
            plt.legend(loc='lower right')
    plt.show()


def randa_plot(model_center=None,label=None):
    '''
    :param: model_center,聚类中心
    :param: label,特征名称
    '''
    plt.rcParams['font.sans-serif'] = 'SimHei'  #设置正常显示中文
    label = list(label)
    n = len(label)  # 特征个数
    angles = np.linspace(0,2*np.pi,n,endpoint=False)  # 间隔采样，设置雷达图的角度，用于平分切开一个圆面,endpoint设置为False表示随机采样不包括stop的值
    angles = np.concatenate((angles,[angles[0]]))  # 拼接多个数组，使雷达图一圈封闭起来
    fig = plt.figure(figsize=(5,5))  # 创建一个空白画布
    ax = fig.add_subplot(1,1,1,polar=True)  # 创建子图，设置极坐标格式，绘制圆形
    ax.set_thetagrids(angles*180/np.pi, label+[label[0]])  #  添加每个特征的标签
    ax.set_ylim(model_center.min(),model_center.max())  # 设置y轴范围
    ax.grid(True)  # 添加网格线
    sam = ['r-', 'o-', 'g-', 'b-', 'p-','m-','k-','y-']  # 设置折线样式
    labels = []
    for i in range(len(model_center)):
        values = np.concatenate((model_center[i],[model_center[i][0]]))
        ax.plot(angles,values,sam[i])
        labels.append('群' + str(i+1))
    plt.legend(labels)