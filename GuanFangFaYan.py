# -*- coding: utf-8 -*-
# Captain_N
import numpy as np
from Figure import Figure
from HanShu import HanShu

# lambda1 = 0.3
# lambda2 = 0.3
# u1 =  0.3
# u2 =  0.3
# u=0.5
# seta1 = 0.01
# index=0.1
# N = 769
# pos_start = 562
# neg_start = 331
# K=10#循环次数
# M=10#每一循环的遍历次数

#HanShu(K,M,N,lambda1,lambda2,u1,u2,u,seta1,pos_start,neg_start,index)
a=HanShu(50,10,769,0.3,0.3,0.3,0.3,0.5,0.01,562,331,0)
b=HanShu(50,10,769,0.3,0.3,0.3,0.3,0.5,0.01,562,331,0.1)
c=HanShu(50,10,769,0.3,0.3,0.3,0.3,0.5,0.01,562,331,0.2)


Figure(10,a[0],a[1],b[0],b[1],c[0],c[1])










