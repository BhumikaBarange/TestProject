#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
df=pd.read_csv("Combined_dataset.csv")
df


# In[45]:


df.duplicated().sum()


# In[52]:


df.isna().sum()


# In[53]:


df.drop(columns=['network_data_call_sign','network_data_language','network_family_data_network_family_id','network_family_data_network_family_name',
'network_family_data_network_family_brand_id',    
'network_family_data_network_id',               
'network_family_data_network_name' ,              
'network_family_data_network_brand_id'])


# In[54]:


df.drop(columns=[
    'network_data_call_sign',
    'network_data_language',
    'network_family_data_network_family_id',
    'network_family_data_network_family_name',
    'network_family_data_network_family_brand_id',
    'network_family_data_network_id',
    'network_family_data_network_name',
    'network_family_data_network_brand_id'
], inplace=True)


# In[10]:


df


# In[56]:


df.isna().sum()


# In[59]:


df.drop_duplicates(inplace=True)


# In[60]:


df.isna().sum()


# In[61]:


df.dropna(inplace=True)


# In[15]:


df.isna().sum()


# In[62]:


df


# In[63]:


df.drop(columns=['File Name',
                 'Date Time',
                 'AcquireId'], inplace=True)


# In[64]:


df_cleaned=df


# In[67]:


df


# In[66]:


import pandas as pd
import numpy as np

# Sample cleaned dataset (for demonstration)
# df_cleaned = pd.read_csv('your_cleaned_dataset.csv') # Load your dataset here

# Assuming you have a list of numeric columns
numeric_cols = [
    'network_data_id',
    'network_data_brand_id',
    'network_family_data_id',
    'conversion_data_matched_data_rate_exposed',
    'conversion_data_matched_data_rate_unexposed',
    'conversion_data_matched_data_incremental',
    'audience_data_impressions',
    'audience_data_impressions_national_live',
    'audience_data_impressions_raw',
    'airings_data_total',
    'airings_data_spend_estimated'
]  # Adjust with your actual numeric columns

# Step 3: Define the function to calculate percentage difference for numeric columns
def calculate_percentage_difference(row1, row2):
    # Calculate the absolute difference and percentage difference for each column
    difference = abs(row1 - row2)
    percentage_diff = (difference / (row1.replace(0, np.nan))) * 100  # Use np.nan for zero to avoid inf values
    return percentage_diff

# Step 4: Calculate percentage difference for each row against the next row
# Using shift to compare each row with the next
percentage_differences = df_cleaned[numeric_cols].shift(-1).combine(df_cleaned[numeric_cols], calculate_percentage_difference)

# Add the percentage differences to the DataFrame
for i, col in enumerate(numeric_cols):
    df_cleaned[f'percentage_difference_{col}'] = percentage_differences.iloc[:, i]

# Step 5: Calculate the mean percentage difference across all percentage difference columns
df_cleaned['mean_percentage_difference'] = df_cleaned[[f'percentage_difference_{col}' for col in numeric_cols]].mean(axis=1)

# Step 6: Filter rows where the mean percentage difference is significant (greater than 0)
df_filtered = df_cleaned[df_cleaned['mean_percentage_difference'] > 0]

# Output the filtered result
df_filtered


# In[70]:


# Export df_filtered as Excel
# Export df_filtered as Excel to a specific path
df_filtered.to_excel('D:/New folder/df_filtered.xlsx', index=False)



# In[ ]:




