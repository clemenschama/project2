#!/usr/bin/env python
# coding: utf-8

# In[231]:


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[233]:


football= pd.read_csv("2020-2021.csv")


# In[235]:


df= pd.DataFrame(football)#this creates a data frame


# In[239]:


#df#reads the data frame


# In[241]:


#to select the columns we will work with
df= df[["Date", "Time", "HomeTeam", "AwayTeam", "AR", "HR", "Referee", "AS", "HS", "FTHG", "FTAG","HF","AF"]]


# In[243]:


#rint(df)


# In[245]:


#df.info() #this tells us information about our data such as data type, column name etc


# In[247]:


#df.isnull().sum() #this counts the number of empty or null entries


# In[249]:


#to check if the names of the columns are formated correctly
#df.columns


# In[255]:


#to make a histogram showing number of away and home goals per team
#sample data
data = df[["HomeTeam", "HS"]]

#CREATE A DataFrame
df2= pd.DataFrame(data)
#df2


# In[257]:


#group by HomeTeam and sum of HomeShots
total_shots= df.groupby("HomeTeam")["HS"].sum().reset_index()


# In[259]:


#sort the teams by total goals in descending order
total_shots = total_shots.sort_values(by="HS", ascending=False)


# In[261]:


print(total_shots)


# In[265]:


#plot a histogram of the shots column
plt.bar(total_shots["HomeTeam"], total_shots["HS"], color="blue",edgecolor="black")
st.title("Total home shots by team")
plt.xlabel("teams")
plt.ylabel("number of total shots")
plt.xticks(rotation=90)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()


# In[267]:


#make a data frame for referees
refs= df[["Referee"]]


df3= pd.DataFrame(refs)


# In[269]:


#count the number of occurances of each name

name_count= df3["Referee"].value_counts().reset_index()
name_count.columns = ["Referee","Counts"]
#print(name_count)


# In[271]:


#streamlit app layout
st.title("Referees and the number of games played")
st.dataframe(name_count)


# In[ ]:




