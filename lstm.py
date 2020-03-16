# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:17:43 2019

@author: liusiyan
"""
# 手动编写一个lstm 前向传播

import numpy as np

timesteps = 10
input_features = 16
output_features = 32

inputs = np.random.random((timesteps, input_features)) # (10, 32)

c_state = np.zeros(shape=(output_features,)) # init state c  # 长期记忆单元
h_state = c_state # 初始化 都等于 0

def generate_parames_for_lstm_cell(x_size, h_size, bias_size):
    '''
    随机生成单元内部参数
    :param x_size: 输入数据 参数
    :param h_size: 上一层输出数据 参数
    :param bias_size: 偏置
    :return:
    '''
    w = np.random.random(x_size)
    u = np.random.random(h_size)
    b = np.random.random(bias_size)
    return w, u, b

def sigmoid(x):
    # 定义 sigmoid函数
    s=1.0/(1.0+np.exp(-x))
    return s
# 遗忘门参数
forget_gate_w, forget_gate_u, forget_gate_b = \
    generate_parames_for_lstm_cell((input_features, output_features),
                                   (output_features, output_features),
                                   (1, output_features)
                                   )
# 输入门参数
input_gate_w, input_gate_u, input_gate_b = \
    generate_parames_for_lstm_cell((input_features, output_features),
                                   (output_features, output_features),
                                   (1, output_features)
                                   )
# 输出门参数
output_gate_w, output_gate_u, output_gate_b = \
    generate_parames_for_lstm_cell((input_features, output_features),
                                   (output_features, output_features),
                                   (1, output_features)
                                   )
# tanh层参数
tanh_w, tanh_u, tanh_b = \
    generate_parames_for_lstm_cell((input_features, output_features),
                                   (output_features, output_features),
                                   (1, output_features)
                                   )

h_list = []
for i in range(timesteps):

    # 遗忘门(控制上一时刻记忆的遗忘程度)
    forget_gate = sigmoid(np.dot(h_state, forget_gate_u) + np.dot(inputs[i], forget_gate_w) + forget_gate_b)
    # 输入门(控制新记忆写入长期记忆的程度)
    input_gate = sigmoid(np.dot(h_state, input_gate_u) + np.dot(inputs[i], input_gate_w) + input_gate_b)
    # 输出门(控制着短期记忆如何受长期记忆影响)
    output_gate = sigmoid(np.dot(h_state, output_gate_u) + np.dot(inputs[i], output_gate_w) + output_gate_b)
    # tanh
    tanh_gate = np.tanh(np.dot(h_state, tanh_u) + np.dot(inputs[i], tanh_w) + tanh_b)

    c_state = c_state * forget_gate + input_gate * tanh_gate # shape (1, 64)  # 长期记忆

    h_state = np.tanh(c_state) * output_gate # (1, 64)  #短期记忆

    h_list.append(h_state)

h_list = np.vstack(h_list)


print('最后一个cell的输出：')
print(h_state)

print('每一层cell的输出：')
print(h_list)
