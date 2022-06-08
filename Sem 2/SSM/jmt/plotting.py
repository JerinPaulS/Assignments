import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dp1 = [[0.1,0.5,0.05,0.1,0.05,0.53], [0.1,0.6,0.06,0.1,0.06,0.64], [0.1,.8,0.09,0.1,0.08,0.87], [0.1,0.9,0.1,0.1,0.09,0.99,], [0.1,1.0,0.11,0.1,0.1,1.11], [0.1,1.1,0.12,0.1,0.11,1.24], [0.1,1.2,0.14,0.1,0.12,1.36], [0.1,1.3,0.15,0.1,0.13,1.49], [0.1,1.4,0.16,0.1,0.14,1.63], [0.1,1.5,0.18,0.1,0.15,1.76]]
dp2 = [[0.5,1.5,3,0.5,0.75,6.0], [0.52,1.5,3.55,0.52,0.78,6.82], [0.54,1.5,4.26,0.54,0.81,7.89], [0.56,1.5,5.25,0.56,0.84,9.38], [0.58,1.5,6.69,0.58,0.87,11.54], [0.60,1.5,9.0,0.6,0.9,15], [0.62,1.5,13.29,0.62,0.93,21.43], [0.64,1.5,24,0.64,0.96,37.5], [0.66,1.5,99,0.66,0.99,150]]

ST = []
ACT = []
ATH = []
AU = []
AR = []

for i in range(len(dp1)):
    ST.append(dp1[i][1])
    ACT.append(dp1[i][2])
    ATH.append(dp1[i][3])
    AU.append(dp1[i][4])
    AR.append(dp1[i][5])

plt.plot(ST, ACT, color='r', label='Avg Customer')
plt.plot(ST, ATH, color='g', label='Avg Throughput')
plt.plot(ST, AU, color='b', label='Avg Utilization')
plt.plot(ST, AR, color='y', label='Avg Response')
plt.xlabel("Avg Serv Time")
plt.ylabel("Time (s)")
plt.title("M/M/1 Queue")
plt.legend()
plt.show()

AT = []
ACT = []
ATH = []
AU = []
AR = []

for i in range(len(dp2)):
    AT.append(dp2[i][0])
    ACT.append(dp2[i][2])
    ATH.append(dp2[i][3])
    AU.append(dp2[i][4])
    AR.append(dp2[i][5])

plt.plot(AT, ACT, color='r', label='Avg Customer')
plt.plot(AT, ATH, color='g', label='Avg Throughput')
plt.plot(AT, AU, color='b', label='Avg Utilization')
plt.plot(AT, AR, color='y', label='Avg Response')
plt.xlabel("Lambda")
plt.ylabel("Time (s)")
plt.title("M/M/1 Queue")
plt.legend()
plt.show()

data1 = pd.read_csv("/home/pict/JMT/log_JMCHt1.csv")
data2 = pd.read_csv("/home/pict/JMT/log_JMCHt2.csv")
data3 = pd.read_csv("/home/pict/JMT/log_JMCHt3.csv")
data4 = pd.read_csv("/home/pict/JMT/log_JMCHt4.csv")
data5 = pd.read_csv("/home/pict/JMT/log_JMCHt5.csv")
data6 = pd.read_csv("/home/pict/JMT/log_JMCHt6.csv")
data7 = pd.read_csv("/home/pict/JMT/log_JMCHt7.csv")
data8 = pd.read_csv("/home/pict/JMT/log_JMCHt8.csv")
data9 = pd.read_csv("/home/pict/JMT/log_JMCHt9.csv")
data10 = pd.read_csv("/home/pict/JMT/log_JMCHt10.csv")

fig = plt.figure()
ax = fig.add_subplot(111, label = "1")

#ax.plot(data1.loc[:, "Cust. ID"].values.tolist(), data1.loc[:, "Waiting Time"].values.tolist(), color = "C0", label = "0.5")
ax.set_xlabel("Cust ID", color = "C0")
ax.set_ylabel("Time (s)", color = "C0")
ax.tick_params(axis = 'x', colors = "C0")
ax.tick_params(axis = 'y', colors = "C0")

ax.plot(data2.loc[:, "Cust. ID"].values.tolist(), data2.loc[:, "Waiting Time"].values.tolist(), color = "C1", label = "0.6")

#ax.plot(data3.loc[:, "Cust. ID"].values.tolist(), data3.loc[:, "Waiting Time"].values.tolist(), color = "C3", label = "0.8")

plt.title('Waiting Time')
ax.legend(loc = 'best')
plt.show()
