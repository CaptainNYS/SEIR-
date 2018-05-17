# -*- coding: utf-8 -*-
# Captain_N
import numpy as np
import matplotlib .pyplot as plt
def Figure(M,mean_i_negG1,mean_i_posG1,mean_i_negG2,mean_i_posG2,mean_i_negG3,mean_i_posG3):
    x_zhou=np.array(range (M))
    plt.figure()
    plt.plot(x_zhou, mean_i_negG1,'g-o')
    plt.plot(x_zhou, mean_i_posG1,'r-o')
    plt.plot(x_zhou, mean_i_negG2, 'g-s')
    plt.plot(x_zhou, mean_i_posG2, 'r-s')
    plt.plot(x_zhou, mean_i_negG3, 'g->')
    plt.plot(x_zhou, mean_i_posG3, 'r->')
    plt.ylim((0,1))
    plt.xlim((0,M))
    plt.xticks(np.linspace(0, M, M+1))#构建等差数列
    plt.yticks(np.linspace(0, 1, 11))
    plt.legend(labels = ['I_{neg}G1','I_{pos}G1','I_{neg}G2','I_{pos}G2','I_{neg}G3','I_{pos}G3'], loc = 'best')
    plt.xlabel('Time/step')
    plt.ylabel('Node density')

    plt .show()