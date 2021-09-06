#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

n_hours = 24
initial_population = 1445
pop = np.zeros(n_hours)
rate = 1.1
K = 10000000

pop[0] = initial_population
for i in range(n_hours - 1):
    pop[i + 1] = (pop[i] + pop[i] * rate * (1 - pop[i]/K)) * np.random.normal(1, 0.05)
    
print(pop)
plt.plot(pop)

np.savetxt("data_exp_X.txt", pop)

n_hours = 24
initial_population = 3087
pop = np.zeros(n_hours)
rate = .7
K = 10000000

pop[0] = initial_population
for i in range(n_hours - 1):
    pop[i + 1] = (pop[i] + pop[i] * rate * (1 - pop[i]/K)) * np.random.normal(1, 0.05)
    
print(pop)
plt.plot(pop)

np.savetxt("data_exp_Y.txt", pop)


# In[ ]:




