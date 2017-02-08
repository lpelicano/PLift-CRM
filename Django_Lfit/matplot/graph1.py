from pylab import * 
import numpy as np 


S2B = np.array(arange(0.9, 3.0, 0.1))
BP = np.array([16,20,20,22,22,24,26,26,28,28])
SQT = np.array([8,8,10,10,12,12,12,14,14,14,16,16,16,18,18,18,20,20,20])
DL = np.array([6,6,6,6,8,8,8,10,10,10,10,12,12,12,14,14,14,16,16,18,18,18,20,20,20])

plot(arange(len(BP)), BP)
plot(arange(len(SQT)), SQT)
plot(arange(len(DL)), DL)

xlabel('Strength/BodyWeight')
ylabel('Total Fatigue % per week')
title('Correlation between correct fatigue and strength level')
grid(True)
show()