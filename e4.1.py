#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
counts = pd.Series([632,1638,456,112])
print(counts)


# In[2]:


counts.values


# In[3]:


counts.index


# In[4]:


bacteria = pd.Series([632,1638,569,115],
                    index=['Firmicutes','Proteobacteria','Actinobacteria','Bacteroidetes'])
print(bacteria)


# In[5]:


bacteria['Actinobacteria']


# In[6]:


bacteria[bacteria.index.str.endswith('bacteria')]


# In[7]:


'Bacteroidetes' in bacteria


# In[8]:


bacteria[0]


# In[9]:


bacteria.name='counts'
bacteria.index.name='phylum'
print(bacteria)


# In[10]:


bacteria[bacteria>1000]


# In[11]:


bacteria_dict={'Firmicutes':632,'Proteobacteria':1632,'Actinobacteria':569,'Bacteroidetes':115}


# In[12]:


bact=pd.Series(bacteria_dict)
print(bact)


# In[13]:


bacteria2=pd.Series(bacteria_dict,
                   index=['Cyanobacteria','Firmicutes','Proteobacteria','Actinobacteria'])
print(bacteria2)


# In[14]:


bacteria2.isnull()


# In[15]:


bacteria+bacteria2


# In[17]:


bacteria_data = pd.DataFrame({'value':[632,1638,569,115,433,1130,754,555],
                             'patient':[1,1,1,1,2,2,2,2],
                             'phylum':['Firmicutes','Proteobacteria','Actinobacteria','Bacteroidetes','Firmicutes','Proteobacteria','Actinobacteria','Bacteroidetes']})
#print(bacteria_data) - or - since print() is optional
bacteria_data


# In[18]:


bacteria_data[['phylum','value','patient']]


# In[19]:


bacteria_data.columns


# In[20]:


bacteria_data['value']


# In[22]:


type(bacteria_data['value'])


# In[23]:


bacteria_data['value']


# In[24]:


bacteria_data.loc[3]


# In[25]:


bacteria_data[['value']]


# In[26]:


bacteria_data.head()


# In[27]:


bacteria_data.tail(3)


# In[28]:


bacteria_data.shape


# In[29]:


bacteria_data=pd.DataFrame([{'patient':1,'phylum': 'Firmicutes','value':632},
                           {'patient':1,'phylum': 'Proteobacteria','value':1638},
                           {'patient':1,'phylum': 'Actinobacteria','value':569},
                           {'patient':1,'phylum': 'Bacteroidetes','value':115},
                           {'patient':2,'phylum': 'Firmicutes','value':433},
                           {'patient':2,'phylum': 'Proteobacteria','value':1130},
                           {'patient':2,'phylum': 'Actinobacteria','value':754},
                           {'patient':2,'phylum': 'Bacteroidetes','value':555}])


# In[30]:


bacteria_data


# In[31]:


vals = bacteria_data.value
vals


# In[32]:


vals[5]=0
vals


# In[33]:


bacteria_data


# In[34]:


vals=bacteria_data.value.copy()
vals[5]=1000


# In[35]:


bacteria_data


# In[36]:


bacteria_data.value[5]=1130


# In[37]:


bacteria_data


# In[38]:


bacteria_data['year']=2013
bacteria_data


# In[39]:


bacteria_data.phylum


# In[40]:


treatment=pd.Series([0]*4+[1]*2)
treatment


# In[41]:


bacteria_data['treatment']=treatment
bacteria_data


# In[42]:


bacteria_data.values


# In[43]:


df=pd.DataFrame({'foo':[1,2,3],'bar':[0.4,-1.0,4.5]})
df.values, df.values.dtype


# In[44]:


bacteria_data.index[0]=15


# In[45]:


bacteria2.index=bacteria.index
bacteria2


# In[47]:


medals=pd.read_table('olympics.2018.txt',sep='\t',
                    index_col=0,
                    header=None,
                    names=['country','medals','population'])
medals.head()


# In[48]:


oecd_site='https://www.oecd.org/about/budget/member-countries-budget-contributions.htm'


# In[49]:


pd.read_html(oecd_site)


# In[50]:


mb=pd.read_csv("microbiome.csv")


# In[51]:


pd.read_csv("microbiome.csv", skiprows=[3,4,6]).head()


# In[52]:


few_recs=pd.read_csv("microbiome.csv",nrows=4)
few_recs


# In[53]:


data_chunks=pd.read_csv("microbiome.csv",chunksize=5)
data_chunks


# In[54]:


next(data_chunks)


# In[55]:


next(data_chunks)


# In[56]:


mb=pd.read_csv("microbiome.csv",index_col=['Taxon','Patient'])
mb.head()


# In[57]:


mb.index


# In[58]:


mb.loc[('Firmicutes',2)]


# In[59]:


mb.xs(1,level='Patient')


# In[61]:


mb.swaplevel('Patient','Taxon').head()


# In[62]:


print('Michael Lopez')


# In[ ]:




