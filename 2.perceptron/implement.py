#-*-encoding: utf-8 -*-
import numpy as np


class Perceptron:
    def __init__(self, _w1, _w2, _theta):
        self.w = np.array([_w1, _w2])
        self.theta = _theta

    def passing_x(self, _x1, _x2):
        x = np.array([_x1, _x2])
        np_sum = np.sum(self.w * x)
        if np_sum - self.theta >= 0:
            return 1
        else:
            return 0

# AND 게이트
p_and = Perceptron(1.5, 1.5, 2.0)
print p_and.passing_x(1, 1)

# NAND 게이트
p_nand = Perceptron(-1.5, -1.5, -2.0)
print p_nand.passing_x(1, 1)

# OR 게이트
p_or = Perceptron(1.0, 1.0, 0.5)
print p_or.passing_x(0, 0)

# XOR 게이트
# 다중 퍼셉트론
def xor(_x1,_x2):
    return p_and.passing_x(p_nand.passing_x(_x1, _x2), p_or.passing_x(_x1, _x2))

print xor(0,0)
print xor(0,1)
print xor(1,0)
print xor(1,1)


