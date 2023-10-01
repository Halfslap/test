#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
# import matplot lib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import streamlit as st


# In[9]:


st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')


# In[10]:


# Import Data
health_data = pd.read_csv("C:/Users/McLovin/.spyder-py3/New Data/oura_2019-01-01_2023-09-09_trends_Original.csv")


# In[11]:


health_data


# In[12]:

