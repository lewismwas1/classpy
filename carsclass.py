#!/usr/bin/env python
# coding: utf-8

# In[29]:


class Car:
    def __init__(self,name,color,year):
        self.name = name
        self.color = color
        self.year = year
        
r1 = Car("Bentley","White",2023)

print(f"This is a {r1.color} {r1.name} model {r1.year}.")


# In[30]:


class Car:
    def __init__(self, name, color, year):
        self.name = name
        self.color = color
        self.year = year

car1 = Car("Toyota", "White", 2023)

print(f"This is a {car1.color} {car1.name} model {car1.year}.")


# In[33]:


class Car:
    def __init__(self,name,color,year):
        self.name = name
        self.color = color
        self.year = year
        
r2 = Car("Mercedes","Blue",2024)
print(f"This is a {r2.color} {r2.name} model {r2.year}")


# In[ ]:




