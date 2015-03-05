
# coding: utf-8

# In[7]:

##Project Euler Problems

#Problem 16: Power digit sum

def powersum(x):
    return sum([int(i) for i in str(x)])

print(powersum(2 ** 1000))


# In[ ]:



