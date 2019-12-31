#!/usr/bin/env python
# coding: utf-8

# In[4]:


from itertools import groupby
import random 
import numpy as np
stu=[[1,"hello1",'3',"mca"],
    [2,"hello2",'2',"mca"],
    [3,"hello3",'3',"mca"],
    [4,"hello4",'4',"mca"],
    [5,"hello5",'4',"mca"],
    [6,"hello6",'3',"mca"],
    [7,"hello7",'2',"mca"],
    [8,"hello8",'4',"mca"],
    [9,"hello9",'2',"mca"],
    [10,"hello10",'3',"mca"],
    [11,"hello11",'5',"mca"]]
stu=sorted(stu, key=lambda x: x[2])

res =  groupby(stu, lambda x: x[2])
for i,v in res:
    print(i , "  " ,list(v))
    
res = [list(v) for i, v in groupby(stu, lambda x: x[2])]
for i in res:
    print(random.sample(i,1))
#print(res)


# In[ ]:





# In[ ]:





# In[ ]:




