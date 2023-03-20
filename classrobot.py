#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Robot:
    def introduce_self(self):
        print("My name is " + self.name +" and my weight is " + str(self.weight) + " am color " + self.color)
        


# In[43]:


r1 = Robot()
r1.name = "Tom"
r1.weight = 60
r1.color = "Blue"


# In[44]:


r2 = Robot()
r2.name = "Lewis"
r2.weight = 63
r2.color = "Black"


# In[45]:


r1.introduce_self()
r2.introduce_self()


# In[ ]:




