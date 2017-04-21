#-*-encoding:utf-8-*-
import numpy as np

# 1차원 배열
x1 = np.array([1, 2, 3])
print (x1)

# n차원 배열
x2 = np.array([[1, 2], [3, 4]])
print (x2)

# 브로드캐스트
# 넘파이 배열간 연산을 하기 위해선 행렬 크기가 같아야하지만
# 스칼라값(단일값)으로 연산을 하면 스스로 크기에 맞게 확장하여 계산된다.
print (x2 * 100)

# 스칼라값이 아니더라도 행 또는 열 길이가 같으면 아래로 브로드캐스트 된다.
print (x2 * np.array([10, 20]))
print(x2 * np.array([[10], [20]]))

# 원소 접근
x3 = np.array([[51,55],[14,19],[0,4]])
print(x3)
print(x3[1])
print(x3[1][1])

# 1차원 배열로 변환(평탄화)
X3 = x3.flatten()
print(X3)

# 인덱스가 0,2,4인 원소 얻기
# 인덱스로 탐색
print(X3[np.array([0,2,4])])

# 특정 조건을 만족하는 원소만 얻기
print(X3 > 15)
print(X3[X3 > 15])

