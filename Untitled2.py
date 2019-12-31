#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
from random import sample
np.random.seed(1);
data=np.round(np.random.normal(5,2,10))
print(data)


# In[32]:


np.random.choice(data,5)


# In[33]:


np.random.choice(data,5,replace=False)


# In[ ]:





# In[ ]:




