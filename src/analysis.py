#!/usr/bin/env python
# coding: utf-8

# # Employee Data Analysis
# 
# ## Project Overview
# This notebook analyzes employee data using Python.
# 
# ## Objectives
# - Load employee data
# - Analyze department-wise salary
# - Find average salary
# - Identify employees from Chennai

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Libraries imported successfully!")


# In[2]:


df = pd.read_csv("../data/employees.csv")

print("Employee Data:")
display(df.head())


# In[3]:


print("Dataset Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
display(df.describe())


# In[4]:


department_salary = df.groupby("department")["salary"].mean()

print("Average Salary by Department:")
display(department_salary)


# In[5]:


city_count = df["city"].value_counts()

print("Employee Count by City:")
display(city_count)


# In[6]:


chennai_employees = df[df["city"] == "Chennai"]

print("Employees from Chennai:")
display(chennai_employees)


# In[7]:


department_salary.plot(kind="bar", color="skyblue")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[8]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[ ]:




