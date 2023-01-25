#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import section
import pandas as pd
import openpyxl
import requests
import numpy as np
import random
import hvplot.pandas
import datetime as dt
from pathlib import Path
import seaborn as sns


# In[3]:


Provincial_School_data = r"C:\Users\Aarthi Manoharan\Arun\1 Project Day 1\fintech-project01\Data-Arun\Provincial_School_data_december2022.xlsx"
Provincial_School_df = pd.read_excel('Provincial_School_data_december2022.xlsx', sheet_name='SIF_2021prelim_EQAO1819_EN')
Provincial_School_df.head()


# In[4]:


# Remove rows where the percentage of school-aged children who live in low-income households is 'SP'
Provincial_School_df = Provincial_School_df[Provincial_School_df['Percentage of School-Aged Children Who Live in Low-Income Households'] != 'SP']

# Convert the percentage of school-aged children who live in low-income households to a numeric data type
Provincial_School_df['Percentage of School-Aged Children Who Live in Low-Income Households'] = pd.to_numeric(Provincial_School_df['Percentage of School-Aged Children Who Live in Low-Income Households'])

# Remove unnecessary columns
Provincial_School_df = Provincial_School_df.drop(columns=['Board Number', 'School Number', 'School Special Condition Code', 'Building Suite', 'P.O. Box', 'Phone Number', 'Fax Number', 'School Website', 'Board Website'])

# Rename columns for clarity
Provincial_School_df = Provincial_School_df.rename(columns={'Percentage of School-Aged Children Who Live in Low-Income Households': 'Percentage of Low-Income Households'})

# Print the cleaned DataFrame
print(Provincial_School_df)


# ### From this data, you can:
# Analyze the performance of individual schools and school boards, and compare them against each other. Understand the achievement trends of students over time by looking at the change in grade 6 mathematics achievement over three years, change in grade 9 applied mathematics achievement over three years and change in grade 10 OSSLT literacy achievement over three years Identify schools or school boards that have particularly high or low achievement levels, or that have shown significant improvement or decline over time. Analyze the relationship between student achievement and socio-economic characteristics, such as the percentage of school-aged children living in low-income households and percentage of students whose parents have no degree, diploma or certificate. Understand the student demographics of different schools and school boards and compare them.

# In[5]:


import pandas as pd
import geoviews as gv
import geoviews.feature as gf
import hvplot.pandas
from pathlib import Path

# Read the data from the Excel file
Provincial_School_df = pd.read_excel('Provincial_School_data_december2022.xlsx', sheet_name='SIF_2021prelim_EQAO1819_EN')


school_type =  Provincial_School_df[["School Name", "Board Name" ]].groupby("School Name").sum()
# Review the DataFrame
school_type


# In[6]:


Board_type =  Provincial_School_df[["Board Name" ]].groupby("Board Name").mean()
Board_type


# ### Five-Year Graduation Rate
# A student is considered a five-year graduate if they receive an OSSD (Ontario Secondary School Diploma) within five years of starting Grade 9.
# 
# As of August 31, 2021, 89.0 per cent of students were graduating in five years and 84.2 per cent in four years. The four-year and five-year graduation rate is calculated as the percentage of students who receive an OSSD within four or five years of starting Grade 9. Students who have transferred out of province, or died, are not included in calculating the graduation rate.
# 
# For students to earn an OSSD, they must:
# 
# Earn a minimum of 30 credits, including 18 compulsory credits and 12 optional credits
# meet the provincial secondary school literacy requirement, and
# complete 40 hours of community involvement activities.
# 
# Source Link = https://www.app.edu.gov.on.ca/eng/bpr/allBoards.asp?chosenIndicator=11&submit.x=19&submit.y=13

# In[7]:


Graduation_rate = r"C:\Users\Aarthi Manoharan\Arun\1 Project Day 1\fintech-project01\Data-Arun\Graduation_Rate_5yrs.xlsx"
Graduation_rate_df = pd.read_excel('Graduation_Rate_5yrs.xlsx', sheet_name='Graduation rate')
Graduation_rate_df.head()


# ### Grade 10 Literacy Test
# The Education Quality and Accountability Office (EQAO) annually assesses the literacy skills of Ontario's Grade 10 students through the Ontario Secondary School Literacy Test. EQAO is an arm's-length agency of the provincial government and provides parents, teachers and the public with accurate and reliable information about student achievement.
# 
# The Ontario Secondary School Literacy Test assesses reading and writing skills that students are expected to have learned in all subjects by the end of Grade 9. Students have the opportunity to rewrite the test if they fail; however, they must pass the test or enrol in and pass the Ontario Secondary School Literacy Course to obtain the graduation literacy requirement.
# 
# In 2018-19, the percentage of Grade 10 students who were eligible to write the test for the first time and who fully participated in and passed the literacy test was 80 per cent for English-language students and 89 per cent for French-language students.
# 
# This chart is a snapshot of Grade 10 literacy test results by board.

# In[8]:


Grade_10_literacy = r"C:\Users\Aarthi Manoharan\Arun\1 Project Day 1\fintech-project01\Data-Arun\Graduation_Rate_5yrs.xlsx"
Grade_10_literacy_df = pd.read_excel('Graduation_Rate_5yrs.xlsx', sheet_name='Grade 10 Literacy Test')
Grade_10_literacy_df.head()


# In[9]:


merged_df = pd.merge(Board_type, Graduation_rate_df, on='Board Name')
merged_df


# In[10]:


import seaborn as sns
merged_df = pd.merge(Board_type, Graduation_rate_df, on='Board Name')
merged_df
# Use the heatmap() function to create the heat map
sns.heatmap(merged_df.set_index("Board Name"), cmap="YlGnBu", annot=True, fmt='.2f', linewidths=.5, cbar=False)


# In[11]:


merged_df_1 = pd.merge(merged_df, Grade_10_literacy_df, on ='Board Name')
merged_df_1


# In[12]:


import seaborn as sns
merged_df_1 = pd.merge(merged_df, Grade_10_literacy_df, on ='Board Name')
merged_df_1
# Use the heatmap() function to create the heat map
sns.heatmap(merged_df_1.set_index("Board Name"), cmap="YlGnBu", annot=True, fmt='.2f', linewidths=.5, cbar=False)


# In[22]:


import matplotlib.pyplot as plt

merged_df_1.set_index("Board Name").plot(kind='bar', stacked=True)
plt.xlabel("Board Name")
plt.ylabel("Percentages")
plt.title("Literacy and Graduation rate in Ontario")
plt.show()


# #In the above code, I first set the index of the dataframe to "Board Name" using .set_index("Board Name"). Then, I use the .plot() method to create a bar plot of the data, with the kind parameter set to 'bar'. I also used stacked=True which will stack the bars of each column on top of each other. Then I set xlabel and ylabel to "Board Name" and "Values" respectively and set the title of the plot to "Bar Plot of Values by Board Name".
# 
# Finally, I use plt.show() to display the plot.

# In[14]:


import matplotlib.pyplot as plt
# extract columns of interest
Provincial_School_data = r"C:\Users\Aarthi Manoharan\Arun\1 Project Day 1\fintech-project01\Data-Arun\Provincial_School_data_december2022.xlsx"
Provincial_School_df = pd.read_excel('Provincial_School_data_december2022.xlsx', sheet_name='SIF_2021prelim_EQAO1819_EN')


socio_economic =  Provincial_School_df[["Percentage of School-Aged Children Who Live in Low-Income Households", "Board Name" ]].groupby("Percentage of School-Aged Children Who Live in Low-Income Households").sum()
# Review the DataFrame
socio_economic


# In[20]:


import holoviews as hv
import pandas as pd

Provincial_School_data = r"C:\Users\Aarthi Manoharan\Arun\1 Project Day 1\fintech-project01\Data-Arun\Provincial_School_data_december2022.xlsx"
Provincial_School_df = pd.read_excel('Provincial_School_data_december2022.xlsx', sheet_name='SIF_2021prelim_EQAO1819_EN')

points = hv.Points(Provincial_School_df, kdims=['Longitude', 'Latitude'], vdims=['School Type', 'School Level'])

hv.extension('bokeh')

points.opts(width=800, height=600, size=5, padding=0.1, tools=['hover'], title='Schools in Ontario')

points.opts(width=800, height=600, size=5, padding=0.1, tools=['hover'], title='Schools in Ontario').opts()


# In[ ]:




