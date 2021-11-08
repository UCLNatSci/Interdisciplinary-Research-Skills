#!/usr/bin/env python
# coding: utf-8

# # Workshop 4 Answers
# 
# ## Species X simulation

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

r_X = 1
n_hours = 8
initial_population = 1000
pop_X = np.zeros(n_hours + 1)

pop_X[0] = initial_population
for i in range(n_hours):
    pop_X[i + 1] = pop_X[i] + pop_X[i] * r_X
    
print("Population of species X:", pop_X)


# In[2]:


plt.figure(figsize=(6,3))
plt.plot(pop_X)

plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species X")


# ## Species Y simulation

# In[3]:


# Population with slower growth rate
r_Y = 0.1
n_hours = 8
initial_population = 1000
pop_Y = np.zeros(n_hours + 1)

pop_Y[0] = initial_population
for i in range(n_hours):
    pop_Y[i + 1] = pop_Y[i] + pop_Y[i] * r_Y
    
print("Population of species Y:", pop_Y)

plt.figure(figsize=(6,3))
plt.plot(pop_Y)

plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species Y")


# ## Species X experimental data

# In[4]:


# Experimental data collected for X
data_X = np.array([  1.  ,   2.18,   4.45,   8.91,  16.1 ,  31.49,  60.89, 117.58, 214.4 ]) * 1000

# Plot both data and model prediction
plt.figure(figsize=(6,3))
plt.plot(pop_X, label="model")
plt.plot(data_X, label="experiment")

# Figure labels etc
plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species X")
plt.legend()


# ## Species Y experimental data

# In[5]:


# Predictive model for Y
r_Y = 0.4
n_hours = 8
initial_population = 1000
pop_Y = np.zeros(n_hours + 1)
pop_Y[0] = initial_population
for i in range(n_hours):
    pop_Y[i + 1] = pop_Y[i] + pop_Y[i] * r_Y

# Experimental data collected for Y
data_Y = np.array([  1., 1.47, 2.02, 2.81, 4.16, 5.88, 7.98, 10.00, 15.59 ]) * 1000

# Plot both data and model prediction
plt.figure(figsize=(6,3))
plt.plot(pop_Y, label="model")
plt.plot(data_Y, label="experiment")

# Figure labels etc.
plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species Y")
plt.legend()


# ## 24h experiment
# 
# Loading experimental data:

# In[6]:


data_X = np.loadtxt("data_exp_X.txt")
print(data_X)


# In[7]:


r_X = 1
n_hours = 24
initial_population = 1000
pop_X = np.zeros(n_hours + 1)

pop_X[0] = initial_population
for i in range(n_hours):
    pop_X[i + 1] = pop_X[i] + pop_X[i] * r_X
    
plt.figure(figsize=(6,3))
plt.plot(pop_X, label="model")
plt.plot(data_X, label="experiment")

# Uncomment the line below to get a more informative figure
plt.ylim(0, 1.2e6)

plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species X")
plt.legend()


# In[8]:


plt.figure(figsize=(6,3))
plt.plot(data_X)


# ## Logistic Growth
# 
# ### Species X

# In[9]:


# Set up model for species X
r_X = 1
K_X = 1e6
n_hours = 24
initial_population = 1000

pop_X = np.zeros(n_hours + 1)
pop_X[0] = initial_population

# Simulate logistic growth
for i in range(n_hours):
    pop_X[i + 1] = pop_X[i] + pop_X[i] * r_X * (1 - pop_X[i]/K_X)

# Plot of model and experimental data
plt.figure(figsize=(6,3))
plt.plot(pop_X, label="model")
plt.plot(data_X, label="experiment")

plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species X")
plt.legend()


# ### Species Y

# In[10]:


# Load 24h experimental data
data_Y = np.loadtxt("data_exp_Y.txt")

# Set up logistic model for species Y
r_Y = 0.45
K_Y = 5e4
n_hours = 24
initial_population = 1000
pop_Y = np.zeros(n_hours + 1)

pop_Y[0] = initial_population
for i in range(n_hours):
    pop_Y[i + 1] = pop_Y[i] + pop_Y[i] * r_Y * (1 - pop_Y[i]/K_Y)
    
plt.figure(figsize=(6,3))
plt.plot(pop_Y, label="model")
plt.plot(data_Y, label="experiment")

plt.xlabel("time (hours)")
plt.ylabel("population")
plt.title("Species Y")
plt.legend()


# ## Exercise
# 
# Load experimental data for species A, B, C

# In[11]:


data_A = np.loadtxt("data_exp_A.txt")
data_B = np.loadtxt("data_exp_B.txt")
data_C = np.loadtxt("data_exp_C.txt")


# In[12]:


# Write a function for logistic growth
def logistic_growth(r, K, x_0, t_max):
    pop = np.zeros(t_max + 1)
    pop[0] = x_0
    for i in range(t_max):
        pop[i + 1] = pop[i] + pop[i] * r * (1 - pop[i]/K)
    return pop

# Growth parameters for each species (adjust values to achieve good fit!)
r = [.9, .4, .7]
K = [5.5e5, 5.5e4, 1e5]
x_0 = [1000, 10000, 1000]
names = ['A', 'B', 'C']

for i, species in enumerate((data_A, data_B, data_C)):
    
    # Model population growth with species' parameters
    pop = logistic_growth(r[i], K[i], x_0[i], 24)
    
    # Plot model and data
    plt.figure(figsize=(6,3))
    plt.plot(pop, label="model")
    plt.plot(species, label="experiment")

    plt.xlabel("time (hours)")
    plt.ylabel("population")
    plt.title("Species {0}".format(names[i]))
    plt.legend()


# ### Solution
# 
# |Species|Dataset|r|K|$x_0$|
# |---|---|---|---|---|
# |1|B|0.4|5.5e4|10000|
# |2|C|0.7|1e5|1000|
# |3|A|0.9|5.5e5|1000|

# ## Epidemic model

# In[13]:


# Define epidemic model function
def epidemic(a, b, t_max, S_0, I_0):
    
    S = np.zeros(t_max + 1)
    I = np.zeros(t_max + 1)
    
    S[0] = S_0
    I[0] = I_0
    
    for i in range(t_max):
        S[i+1] = S[i] - b * S[i] * I[i]
        I[i+1] = I[i] + b * S[i] * I[i] - a * I[i]

    return S, I


# In[14]:


# Create model, vary values of a and b
a = 0.07
b = 0.00002
S_0 = 20000
I_0 = 100

t_max = 100

S, I = epidemic(a, b, t_max, S_0, I_0)
    
plt.figure(figsize=(6,3))
plt.plot(S, label="Susceptible population")
plt.plot(I, label="Infected population")
# Display legend
plt.legend()

