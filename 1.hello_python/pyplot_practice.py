# -*-encoding:utf-8-*-
import numpy as np
import matplotlib as mil
mil.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.image import imread


# 데이터 준비
x = np.arange(0, 6, 0.1)    #0부터 6까지 0.1간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")        # x축 라벨
plt.ylabel("y")        # y축 라벨
plt.title('sin & cos')  # 제목
plt.legend()
plt.show()

#이미지 표시하기
img = imread('back.png')

plt.imshow(img)
plt.show()
