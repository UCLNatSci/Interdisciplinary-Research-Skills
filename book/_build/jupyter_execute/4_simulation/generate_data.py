#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

def generate_data(name, n_hours, rate, K, pop_0):

    initial_population = pop_0
    pop = np.zeros(n_hours)

    pop[0] = initial_population
    for i in range(n_hours - 1):
        pop[i + 1] = (pop[i] + pop[i] * rate * (1 - pop[i]/K)) * np.random.normal(1, 0.05)

    plt.figure()
    plt.plot(pop)

    np.savetxt("data_exp_{}.txt".format(name), pop * 1000)

    s = "|".join([str(round(p, 2)) for p in pop[:9]])
    print("|" + s + "|")

    print(repr(np.round(pop[:9], 2)))


# In[2]:


np.random.seed(3)
generate_data("X", 24, 1, 1000, 1)
generate_data("Y", 24, .46, 55, 1)


# In[3]:


np.random.seed(3)
generate_data("B", 24, 0.4, 55, 10)
generate_data("C", 24, 0.7, 103, 1)
generate_data("A", 24, 0.9, 540, 1)


# In[ ]:




