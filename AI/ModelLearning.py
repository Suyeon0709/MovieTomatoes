# Generate A.I Model
# >> Model: 긍부정 분석 모델(감성분석)
# >> Module: Tensorflow, Keras
# >> Dataset: Naver Sentiment Movie Corpus(https://github.com/e9t/nsmc/)

################
# Dataset Intro#
################

# 데이터셋 : Naver Sentiment Movie Corpus(https://github.com/e9t/nsmc/)
# >> 네이버 영화 리뷰 중 영화 당 100개의 리뷰를 모아
# >> 총 200,000개의 리뷰(훈련: 15만개, 테스트: 5만개)로
# >> 이루어져 있고, 1~10점 까지의 평저 중 중립적인 평점(5~8)은
# >> 제외하고 1~4점을 부정, 9~10점을 긍정으로 동일한 비율로
# >> 데이터에 포함시킴

# >> 데이터는 id, document, label 세개의 열로 이루어져있음
# >> id: 리뷰의 고유한 key 값
# >> document: 리뷰의 내용
# >> label: 긍정(1)인지 부정(0)인지 나타냄
#           평점이 긍정(9~10점), 부정(1~4점), 5~8점은 제거


import json
import os
import nltk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from pprint import pprint
from konlpy.tag import Okt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

#############
# File Open #
#############

# ~.txt 파일에서 데이터를 물러오는 method
def read_data(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
    return data

# nsmc 데이터를 불러와서 python 변수에 담기
train_data = read_data('ratings_train.txt') # 트레이닝 데이터 Open

'C:/cnu_workspace?MovieTomatoes/ai/dataset/rating_train.txt' #절대경로

# / => 하위폴더
# .. => 상위폴더
# . => 현재폴더

# nsmc 데이터를 불러와서 python 변수에 담기
train_data = read_data('./dataset/ratings_train.txt') # 트레이닝 데이터 Open
test_data = read_data('./dataset/ratings_text.txt')    # 테스트 데이터 Open

# 절대경로와 상대경로
# C:/cnu_workspace/MovieTomatoes
#                      ㄴ ai
#                          ㄴ dataset
#                                ㄴ ratings_text.txt
#                                ㄴ ratings_train.txt
#                          ㄴ ModelLearning.py
#                      ㄴ model
#                      ㄴ webcrawl
#                      ㄴ main.py
#                      ㄴ README.md



print(len(train_data))
print(train_data[0])
print(train_data[1])
print(train_data[-1])

################
# PreProcessing#
################
# 데이터를 학습하기에 알맞게 처리해보자. konlpy 라이브러리를 사용해서
# 형태소 분석 및 품사 태깅을 진행한다. 네이버 영화 데이터는
# 맞춤법이나 띄어쓰기가 제대로 되어있지 않은 경우가 있기 때문에
# 정확한 분류를 위해서 konlpy를 사용한다.
# konlpy에는 여러 클래스가 존재하지만 그중 okt(open korean text)를
# 사용하여 간단한 문장분석을 실행한다.

# JPype1은 반드시 1미만의 버전을 사용할 것!!
# pip uninstall JPpype1
# pip install "Jpype1
okt = Okt()

print(okt.pos('이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요'))