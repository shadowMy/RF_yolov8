# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties
#支持中文
config = {
            "font.family": 'serif',
            "font.size": 15,
            "mathtext.fontset": 'stix',
            "font.serif": ['SimSun'],
         }
rcParams.update(config)
# mpl.rcParams['font.sans-serif'] = ['SimHei']

if __name__ == '__main__':
    # 列出待获取数据内容的文件位置
    # v5、v8都是csv格式的，v7是txt格式的
    result_dict = {
        'RF-YOLOv8s': r'D:\workspace\PycharmProjects\yolov8\runs\train\RF-YOLOv8\results.csv',
        'YOLOv8s': r'D:\workspace\PycharmProjects\yolov8\runs\train\yolov8s\results.csv',
    }

    # 绘制map50
    i = 0
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            data = pd.read_csv(res_path, usecols=[6]).values.ravel()  # 6是指map50的下标（每行从0开始向右数）
        else:  # 文件后缀是txt
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[10]))  # 10是指map50的下标（每行从0开始向右数）
                data = np.array(data)
        x = range(len(data))
        if i == 0:
            plt.plot(x, data, label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1
            i += 1
        else:
            plt.plot(x, data, '--', label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1

    # 添加x轴和y轴标签
    plt.xlabel('迭代次数')
    plt.ylabel('mAP@0.5')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("mAP50.png", dpi=600)  # dpi可设为300/600/900，表示存为更高清的矢量图
    plt.show()

    # 绘制map50-95
    i = 0
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            data = pd.read_csv(res_path, usecols=[7]).values.ravel()  # 7是指map50-95的下标（每行从0开始向右数）
        else:
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[11]))  # 11是指map50-95的下标（每行从0开始向右数）
                data = np.array(data)
        x = range(len(data))
        if i == 0:
            plt.plot(x, data, label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1
            i += 1
        else:
            plt.plot(x, data, '--', label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1

    # 添加x轴和y轴标签
    plt.xlabel('迭代次数')
    plt.ylabel('mAP@0.5:0.95')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("mAP50-95.png", dpi=600)
    plt.show()

    # 绘制训练的总loss
    i = 0
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            box_loss = pd.read_csv(res_path, usecols=[1]).values.ravel()
            obj_loss = pd.read_csv(res_path, usecols=[2]).values.ravel()
            cls_loss = pd.read_csv(res_path, usecols=[3]).values.ravel()
            data = np.round(box_loss + obj_loss + cls_loss, 5)  # 3个loss相加并且保留小数点后5位（与v7一致）

        else:
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[5]))
                data = np.array(data)
        x = range(len(data))
        if i == 0:
            plt.plot(x, data, label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1
            i += 1
        else:
            plt.plot(x, data, '--', label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1


    # 添加x轴和y轴标签
    plt.xlabel('迭代次数')
    plt.ylabel('训练总损失')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("loss_train.png", dpi=600)
    plt.show()

    # 绘制验证的总loss
    i = 0
    for modelname in result_dict:
        res_path = result_dict[modelname]
        ext = res_path.split('.')[-1]
        if ext == 'csv':
            box_loss = pd.read_csv(res_path, usecols=[8]).values.ravel()
            obj_loss = pd.read_csv(res_path, usecols=[9]).values.ravel()
            cls_loss = pd.read_csv(res_path, usecols=[10]).values.ravel()
            data = np.round(box_loss + obj_loss + cls_loss, 5)  # 3个loss相加并且保留小数点后5位（与v7一致）

        else:
            with open(res_path, 'r') as f:
                datalist = f.readlines()
                data = []
                for d in datalist:
                    data.append(float(d.strip().split()[5]))
                data = np.array(data)
        x = range(len(data))
        if i == 0:
            plt.plot(x, data, label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1
            i += 1
        else:
            plt.plot(x, data, '--', label=modelname, color='black', linewidth='1.2')  # 线条粗细设为1


    # 添加x轴和y轴标签
    plt.xlabel('迭代次数')
    plt.ylabel('验证总损失')
    plt.legend()
    plt.grid()
    # 显示图像
    plt.savefig("loss_val.png", dpi=600)
    plt.show()
