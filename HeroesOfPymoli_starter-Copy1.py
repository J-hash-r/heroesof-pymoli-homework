#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[394]:


# Dependencies and Setup
import pandas as pd
import csv
import os
import statistics
import numpy as np
import matplotlib.pyplot as plt


# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# In[395]:


purchase_data.columns


# * Display the total number of players
# 

# In[396]:


Count =  purchase_data['SN'].nunique()
Count


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[397]:


# Unique items in item name column
Unique =pd.unique(purchase_data['Item Name'])
UniqueCount = len(Unique)

#Average Price
Average = purchase_data['Price'].mean()
Average

#Maximum, Minimum and Range
Max = 0
Min = 0

Max = purchase_data['Price'].max()
Min = purchase_data['Price'].min()


Range = Max - Min
Summary_DF = pd.DataFrame({"Number of player":[Count],
                           "Unique Items":[UniqueCount],
                           "Average Price":[Average],
                           "Maximum Price":[Max],
                            "Minimum Price":[Min],
                           "Range" :[Range]})
                                  

Summary_DF


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[398]:


#Count of items purchased per person

Purchase = purchase_data.groupby(['SN','Gender']).count()
Purchase_Count = pd.DataFrame(Purchase["Purchase ID"])

Purchase_Count


# In[399]:


GROUP = purchase_data.groupby(['SN','Gender']).size()


#GROUP_DF = pd.DataFrame(GROUP)
#GROUP_DF.rename(columns= {"0": "Purchases per Player"})
#GROUP_DF.head()

#Purchases_Player = GROUP_DF[3:]
#Purchases_Player
GROUP 


# In[400]:


#Total spent per person on items

Purchase = purchase_data.groupby(['SN','Gender']).sum()
Purchase_Total = pd.DataFrame(Purchase["Price"])
#Purchase_Count
Purchase_Total


# In[401]:


GROUP_DF["Purchase Total"] = Purchase_Total
 
GROUP_DF.head()


# In[402]:


del GROUP_DF[0]
del GROUP_DF["AVG SPEND"]
del GROUP_DF["PURCHASES per Player"]
del GROUP_DF["Purchase_Total]
GROUP_DF.head()


# In[408]:


GENDERGROUPING_Means  = GROUP_DF.groupby(['Gender']).mean()
GENDERGROUPING_Means 
#Avg Spend	Purchases per Player	Purchase Total


# 
# ## Purchasing Analysis (Gender)

# In[409]:


GENDERGROUPING_TOTALS  = GROUP_DF.groupby(['Gender']).count()
GENDERGROUPING_TOTALS  

Percentages = (round((GENDERGROUPING_TOTALS["Avg Spend"]/Count) * 100))

GENDERGROUPING_TOTALS["Percentages"] = Percentages
GENDERGROUPING_TOTALS


# In[410]:


GENDERGROUPING_TOTALS_BYGENDER  = GROUP_DF.groupby(['Gender']).sum()
GENDERGROUPING_TOTALS_BYGENDER['Purchase Total']


# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[411]:


Gender_Summ = pd.DataFrame({"Total Spend By Gender":GENDERGROUPING_TOTALS_BYGENDER['Purchase Total'],
                           "Percentage of Players by Gender":GENDERGROUPING_TOTALS["Percentages"],
                           "Average Spend by Gender":GENDERGROUPING_Means["Avg Spend"],
                           "Average Purchases per player by Gender":GENDERGROUPING_Means["Purchases per Player"],
                           "Average Total Purchase by Gender":GENDERGROUPING_Means["Purchase Total"]})
Gender_Summ


# ## Age Demographics

# In[412]:


Age = purchase_data["Age"]
counts, bins, bars = plt.hist(Age)
plt.xlabel("Age")
plt.ylabel("No.Of Players")
plt.show()

Counts = counts
Bins = bins
Bins = np.delete(Bins,0)


# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[413]:


Percentage_By_Age = (Counts/Count) * 100
len(Percentage_By_Age)
Age_DF=pd.DataFrame({"Age Bins":Bins,
                    "Number Of Players":Counts,
                    "Percentage of Players":Percentage_By_Age})
Age_DF


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[414]:


Purchase2 = purchase_data.groupby(['Age']).count()
Purchase2.head()


# In[415]:


Purchaseagetots = purchase_data.groupby(['Age']).sum()
Purchaseagetots.head()


# In[416]:


Purchaseagemean = purchase_data.groupby(['Age']).mean()
Purchaseagemean.head()


# In[417]:


AGESUMM2 = pd.DataFrame({"Total Purchases":Purchase2['Purchase ID'],
                        "Total Spend per Age":Purchaseagetots['Price'],
                        "Mean spend per age":Purchaseagemean['Price'] })
AGESUMM2.head()


# ## Top Spenders

# In[418]:


purchase_data.head()


# In[439]:



Purchase_Data_Item_Names = pd.DataFrame(purchase_data.groupby(["Item Name"]).count())
Purchase_Data_Item_Names.head()


# In[440]:


Purchase_Data_Item_Names2 = 0
Purchase_Data_Item_Names2 = purchase_data.groupby(["Item Name"]).sum()
Purchase_Data_Item_Names2.head()


# In[458]:


Purchase_Data_Item_Names4 = pd.DataFrame({"Item Spend":Purchase_Data_Item_Names2["Price"],
                                         "Total Bought":Purchase_Data_Item_Names["Purchase ID"]})



Purchase_Data_Item_Names4.head()


# In[469]:


Purchase_Data_Item_Names5 = Purchase_Data_Item_Names4 
Purchase_Data_Item_Names5.sort_values(by = ["Total Bought"], ascending = False)


# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:


GROUP_DF.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[ ]:




