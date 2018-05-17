# -*- coding: utf-8 -*-
# Captain_N
import csv
import random
import numpy as np

def HanShu(K,M,N,lambda1,lambda2,u1,u2,u,seta1,pos_start,neg_start,index):

    #print("读取数据")
    with open('links.csv', encoding='utf-8') as f:
        data = csv.reader(f)
        network =np.zeros((33312,2),dtype=np.int64)#int64是numpy中引入的一个类，即 numpy.int64
        for i, line in enumerate(data):#enumerate 将对象转为索引序列，可以同时获得索引和值。
            #print(line[0])  matlab中节点标号1~769，python中节点标号0~768.
            network[i][0]=int(line[0])-1
            network[i][1]=int(line[1])-1
        #print(network)
    #存储为邻接矩阵
    new_network =np.zeros((N,N),dtype=np.int64)
    for i in range(33312):
        a= network[i][0]
        b= network[i][1]
        new_network[a][b]=1
    #定义初始状态
    #print("定义初始状态")
    state = np.zeros((N,5),dtype=np.int64)
    for i in range(N):
        state[i][0]=1
    #print(state.shape )
    state[pos_start][0] = 0
    state[pos_start][3] = 1
    state[neg_start][0] = 0
    state[neg_start][2] = 1
    #print(state)
    #定义情感值
    #print("情感初始化")
    #sentiment=np.zeros((N,))
    sentiment=np.random.normal(0,0.3875,769 )
    #print(sentiment .shape)
    #for i in range(len(new_network)):
    #    sentiment[i]=(random.normalvariate(0,0.3875))
    for i in range(len(sentiment)):
        if (sentiment[i]>1):
            sentiment [i]=0.99
        if((sentiment[i]<-1)):
            sentiment [i]=-0.99
    sentiment[pos_start]=0.99
    sentiment[neg_start]=-0.99
    #print(sentiment)
    c=np.zeros((K,M,N,5))
    #保留初始值
    old_state = state.copy()
    old_sentiment = sentiment.copy()
    #print(c.shape)

    for i in range(2):
            for i in range(K):
                c[i][0]=old_state.copy()
                #print(old_state)
                state= old_state.copy()
                new_state = state.copy()
                sentiment= old_sentiment.copy()
                for m in range(len(sentiment)):
                    if (sentiment[m]<=0.8):
                        sentiment[m]+=index
                progation= [neg_start,pos_start]
                for j in range(M-1):#29步后到达第30个状态
                    new_progation = []
                    #print(progation)
                    #print("第" + str(i) + "轮循环，第" + str(j) + "次遍历")

                    for m in range(len(progation)):
                        if (state[progation[m]][2]==1):
                            for n in range(N):
                                if (new_network [progation[m]][n]==1):
                                   # print("有连接")
                                    if(new_state[n][0]==1):
                                        sentiment[n]= sentiment[n]+u*(sentiment[progation[m]]-sentiment[n])
                                        if (sentiment[n]<=0):
                                            if(random.random()<lambda1 *(-sentiment[n])):
                                                new_state[n][0]=0
                                                new_state [n][2]=1
                                                new_progation.append(n)
                                            else:
                                                new_state[n][0] = 0
                                                new_state[n][1] = 1
                                                if (random.random() < seta1 * (1 + sentiment[n])):
                                                    new_state[n][1] = 0
                                                    new_state[n][4] = 1
                                                    sentiment[n] = 0

                                        else:
                                            if (random.random() < lambda2 * sentiment[n]):
                                                new_state[n][0] = 0
                                                new_state[n][3] = 1
                                                new_progation.append(n)
                                            else:
                                                new_state[n][0] = 0
                                                new_state[n][1] = 1
                                                if (random.random() < seta1 * (1 - sentiment[n])):
                                                    new_state[n][1] = 0
                                                    new_state[n][4] = 1
                                                    sentiment[n] = 0
                                    elif(new_state [n][1]==1):
                                        sentiment[n] = sentiment[n] + u * (sentiment[progation[m]] - sentiment[n])
                                        if (sentiment[n] <= 0):
                                            if (random.random() < u1 * (-sentiment[n])):
                                                new_state[n][1] = 0
                                                new_state[n][2] = 1
                                                new_progation.append(n)
                                        else:
                                            if (random.random() < u2 * sentiment[n]):
                                                new_state[n][1] = 0
                                                new_state[n][3] = 1
                                                new_progation.append(n)
                                    elif(new_state [n][2]==1):
                                        sentiment[n] = sentiment[n] + u * (sentiment[progation[m]] - sentiment[n])

                        elif (state[progation[m]][3] == 1):
                            for n in range(N):
                                if (new_network[progation[m]][n] == 1):
                                    #print("有连接")
                                    if (new_state[n][0] == 1):
                                        sentiment[n] = sentiment[n] + u * (sentiment[progation[m]] - sentiment[n])
                                        if (sentiment[n] <= 0):
                                            if (random.random() < lambda1 * (-sentiment[n])):
                                                new_state[n][0] = 0
                                                new_state[n][2] = 1
                                                new_progation.append(n)
                                            else:
                                                new_state[n][0] = 0
                                                new_state[n][1] = 1
                                                if (random.random() < seta1 * (1 + sentiment[n])):
                                                    new_state[n][1] = 0
                                                    new_state[n][4] = 1
                                                    sentiment[n] = 0

                                        else:
                                            if (random.random() < lambda2 * sentiment[n]):
                                                new_state[n][0] = 0
                                                new_state[n][3] = 1
                                                new_progation.append(n)
                                            else:
                                                new_state[n][0] = 0
                                                new_state[n][1] = 1
                                                if (random.random() < seta1 * (1 - sentiment[n])):
                                                    new_state[n][1] = 0
                                                    new_state[n][4] = 1
                                                    sentiment[n] = 0
                                    elif (new_state[n][1] == 1):
                                        sentiment[n] = sentiment[n] + u * (sentiment[progation[m]] - sentiment[n])
                                        if (sentiment[n] <= 0):
                                            if (random.random() < u1 * (-sentiment[n])):
                                                new_state[n][1] = 0
                                                new_state[n][2] = 1
                                                new_progation.append(n)
                                        else:
                                            if (random.random() < u2 * sentiment[n]):
                                                new_state[n][1] = 0
                                                new_state[n][3] = 1
                                                new_progation.append(n)
                                    elif (new_state[n][3] == 1):
                                        sentiment[n] = sentiment[n] + u * (sentiment[progation[m]] - sentiment[n])

                    #new_progation = sorted(new_progation)

                    c[i][j+1]=new_state.copy()
                    state =new_state.copy()
                    progation=new_progation.copy()

            column =10#统计20步
            i_posG= np.zeros((K,column))
            i_negG= np.zeros((K,column))
            #print(c[0][0])
            for i in range(K):#K=10
                #print(i)
                for j in range (column):#column=
                    #print(j)
                    state =c[i][j]

                    i_pos_numG =0
                    i_neg_numG =0
                    for m in range(len(state)):#len(state)=769
                        if (state[m][2] == 1):
                            i_neg_numG=i_neg_numG +1
                        if (state[m][3] == 1):
                            i_pos_numG =i_pos_numG +1
                    #print(s_num)
                    pdf_i_negG = i_neg_numG /N
                    pdf_i_posG = i_pos_numG /N
                    i_posG[i][j] = pdf_i_posG
                    i_negG[i][j]= pdf_i_negG
            mean_i_posG = np.mean(i_posG,0)
            mean_i_negG = np.mean(i_negG,0)
    return mean_i_negG,mean_i_posG
