#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import streamlit as st
import pickle


# In[6]:


from absenteeism_module import *


# ####################################

# In[9]:


def Input_output():
    data=st.file_uploader("upload file", type={"csv", "txt"})
    if data is not None:
        df=pd.read_csv(data)
        model=absenteeism_model("model", "scaler")
        model.load_and_clean_data("Absenteeism_new_data.csv")
    result=""
    if st.button("Click here to predict"):
        result= model.predicted_outputs()
        st.balloons()
    st.success("The output is as follow: ")
    st.write(result)
if __name__=="__main__":
    Input_output()
        


# In[ ]:




