'''
@Author: your name
@Date: 2020-04-07 08:44:23
@LastEditTime: 2020-04-07 08:52:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \刷题人生\python学习\词向量.py
'''
from gensim.models import word2vec
import logging

raw_sentences =['I love eat meat','I like you very much']
sentences =[s.split() for s in raw_sentences]
print(sentences)
model = word2vec.Word2Vec(sentences,min_count=1)
#model.similarity()