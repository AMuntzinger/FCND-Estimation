import numpy as np  

data1 = np.genfromtxt('../config/log/Graph1.txt', delimiter=',')
data2 = np.genfromtxt('../config/log/Graph2.txt', delimiter=',')

data1_std = np.std(data1[1:,1])
data2_std = np.std(data2[1:,1])

print('data1 std = ', data1_std)
print('data2 std = ', data2_std)