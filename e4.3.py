#!/usr/bin/env python
# coding: utf-8

# In[35]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fmin
import seaborn as sns
sns.set_context('talk')
sns.set_style('white')

RANDOM_SEED = 20090425


# In[36]:


from io import StringIO


# In[37]:


data_string="""
Drugs   Score
0    1.17    78.93
1    2.97    58.20
2    3.26    67.47
3    4.69    37.47
4    5.83    45.65
5    6.00    32.92
6    6.41    29.97
"""


# In[38]:


lsd_and_math = pd.read_table(StringIO(data_string), sep="\s+", index_col=0)


# In[39]:


lsd_and_math


# In[40]:


lsd_and_math.plot(x='Drugs',y='Score',style='ro',legend=False,xlim=(0,8))


# In[41]:


sum_of_squares = lambda o,x,y: np.sum((y-o[0]-o[1]*x)**2)


# In[42]:


sum_of_squares([0,1], lsd_and_math.Drugs, lsd_and_math.Score)


# In[43]:


x,y=lsd_and_math.T.values
b0,b1=fmin(sum_of_squares, [0,1],args=(x,y))
b0,b1


# In[44]:


ax=lsd_and_math.plot(x='Drugs',y='Score',style='ro', legend=False, xlim=(0,8), ylim=(20,90))
ax.plot([0,10], [b0, b0+b1*10])
for xi, yi in zip(x,y):
    ax.plot([xi]*2,[yi,b0+b1*xi], 'k:')


# In[75]:


sum_of_absval = lambda o,x,y: np.sum(np.abs(y - o[0] - o[1]*x))

b0,b1 = fmin(sum_of_absval, [0,0], args=(x,y))
print('\nintercept: {0:.2}, slope: {1:.2}'.format(b0,b1))
ax = lsd_and_math.plot(x='Drugs',y='Score',style='ro',legend=False,xlim=(0,8))
ax.plot([0,10],[b0,b0+b1*10])


# In[76]:


sum_squares_quad = lambda o,x,y: np.sum((y-o[0]-o[1]*x-o[2]*(x**2))**2)


# In[77]:


b0,b1,b2=fmin(sum_squares_quad, [1,1,-1], args=(x,y))
print('\nintercept: {0:2}, x: {1:.2}, x2: {2:.2}'.format(b0,b1,b2))
ax=lsd_and_math.plot(x='Drugs',y='Score',style='ro',legend=False,xlim=(0,8))
xvals=np.linspace(0,8,100)
ax.plot(xvals,b0+b1*xvals+b2*(xvals**2))


# In[84]:


salmon = pd.read_table("salmon.dat",delim_whitespace=True,index_col=0)
salmon.plot.scatter(x='spawners',y='recruits');


# In[85]:


from pymc3 import HalfCauchy

ax=sns.kdeplot(HalfCauchy.dist(1).random(size=10000),gridsize=2000)
ax.set_xlim(0,100);


# In[86]:


from pip._internal import main
try: 
    import pymc3
except: 
    from pip.internal import main
    main(['install', 'pymc3'])
    import pymc3
    
from pymc3 import HalfCauchy

ax = sns.kdeplot(HalfCauchy.dist(1).random(size=10000), gridsize=2000)
ax.set_xlim(0,100);


# In[95]:


from pymc3 import Normal, Model

with Model() as drugs_model:
    
    intercept = Normal('intercept', 0, sd=100)
    slope = Normal('slope', 0, sd=100)
    o = HalfCauchy('o', 1)


# In[96]:


with drugs_model:
    u = intercept + slope*x
    score= Normal('score', u, sd=o, observed=y)


# In[97]:


from pymc3 import sample

with drugs_model:
    drugs_sample = sample(1000, random_seed=RANDOM_SEED)


# In[90]:


from pymc3 import plot_posterior

plot_posterior(drugs_sample[500:]);


# In[91]:


from pymc3 import sample_ppc

with drugs_model:
    drugs_ppc = sample_ppc(drugs_sample, 1000)


# In[92]:


from pymc3 import sample_posterior_predictive

with drugs_model:
    drugs_ppc = sample_posterior_predictive(drugs_sample,1000)


# In[93]:


drugs_ppc['score'].shape


# In[98]:


fig, axes = plt.subplots(4,2)
axes_flat = axes.flatten()

for ax, real_data, sim_data in zip(axes_flat[:1], y, drugs_ppc['score'].T):
    ax,hist(sim_data, bins=20)
    ax.vlines(real_data, *ax.get_ylim(), colors='red')
    ax.set_yticklabels([])
    sns.despine(left=True)
        
axes_flat[-1].axis('off')
plt.tight_layout()


# In[99]:


print('Michael Lopez')


# In[ ]:




