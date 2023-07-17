#!/usr/bin/env python
# coding: utf-8

# In[13]:


import torch


# In[4]:


torch.__version__


# In[5]:


torch.cuda.is_available()


# In[8]:


torch.cuda.get_current_device()


# In[10]:


import numpy as np
st=[1,4,6,7,8,9,0]


# In[11]:


arr=np.array(st)


# In[12]:


type(arr)


# In[14]:


tensors=torch.from_numpy(arr)


# In[15]:


tensors


# In[16]:


tensors[:3]


# In[17]:


tensors[1:5]


# In[18]:


tensors[0]


# In[19]:


tensors[0]=44


# In[20]:


tensors


# In[23]:


arr


# In[ ]:


here you can see the arr and tensors are values changing because of they are using same memory space


# In[ ]:


# another method 


# In[21]:


tensor=torch.tensor(arr)


# In[22]:


tensor


# In[24]:


tensor[0]=22


# In[25]:


arr


# In[26]:


##zeros and ones
torch.zeros(2,5)


# In[27]:


torch.zeros(1,3)


# In[29]:


torch.ones(2,5,dtype=torch.int32)


# In[30]:


torch.ones(3,2)


# In[33]:


#addition & multiplication

x=torch.tensor([12,32,44,55])
y=torch.tensor([16,2,55,676])


# In[34]:


torch.add(x,y)


# In[35]:


torch.add(x,y).sum()


# In[36]:


torch.multiply(x,y)


# In[37]:


x.mul(y)


# In[38]:


x.dot(y)


# In[39]:


torch.multiply(x,y).sum()


# In[59]:


#matrix 


# In[66]:


x = torch.tensor([[1,444,2],[1,5,5]], dtype=torch.float)
y = torch.tensor([[5,7],[8,6],[9,11]], dtype=torch.float)


# In[67]:


x@y


# In[68]:


torch.matmul(x,y)


# In[69]:


torch.mm(x,y)


# In[ ]:




