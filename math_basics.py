import numpy as np
'''Let's create some fake income data, centered around 27,000 with 
a normal distribution and standard deviation of 15,000, 
with 10,000 data points.
'''
incomes = np.random.normal(27000, 15000, 10000)
print(np.random)
print(np.mean(incomes)) #calculate the mean

import matplotlib.pyplot as plt
plt.hist(incomes,50)
# plt.show()

print(np.median(incomes)) #calculate the median

from scipy import stats
ages = np.random.randint(18, high=90, size=500)
print(stats.mode(ages)) #calculate the mode

print(incomes.std()) #calculate standard deviation
print(incomes.var()) #calculate variance

