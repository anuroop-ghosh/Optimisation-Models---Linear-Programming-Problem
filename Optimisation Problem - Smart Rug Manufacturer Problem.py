#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Installing the necessary libraries for the problem
from pyomo.environ import *
import pandas as pd
import numpy as np


# In[5]:


#Reading the problem from the excel data
file_name = 'Optimisation Model - Smart Rug Manufacturer Problem.xlsx'
df = pd.read_excel(file_name, index_col=0)
df_np = df.to_numpy()


# In[7]:


#Importing each value into separate datasets
material_type = df.loc[df.index[0],df.columns[0:-2]].keys() # Material types
wool = df_np[0,0:2] # Wool data
nylon = df_np[1,0:2] # Nylon data
work_hours = df_np[2,0:2] # Work hours required
availability = df_np[0:-1,0:-2] # Availability of resources
selling_price = df_np[3,0:2] # Selling price of each material type
cost = df_np[0:3,3] # Costs for wool, nylon, and labor
available = df_np[0:3,2] # Available resources


# In[8]:


#Defining the model
model = ConcreteModel()
model.TL = Var(range(len(material_type)), domain = NonNegativeReals)


# In[9]:


#Defining the Income Rule
#Profit/Income = selling price - (cost of wool *quantity of wool + cost of nylon*quantity of nylon + cost of labour*quantity of labour )
profit = [0,0]
for i in range(len(profit)):
  for j in range(len(profit)-1):
    profit[i]=selling_price[i]-(wool[i]*cost[j]+ nylon[i]*cost[j+1] + work_hours[i]*cost[j+2])


# In[11]:


#Defining the Objective Function to maximize total profit 
def obj (model):
  return sum(model.TL[i] * (profit[i]) for i in range(len(material_type)))
model.profit = Objective(rule=obj, sense=maximize)


# In[12]:


#Defining the Limit rule to ensure resource usage does not exceed availability
def limit_rule(model, i):
  return sum(model.TL[j] * availability[i,j] for j in range(len(material_type))) <= available[i]
model.cons = Constraint(range(len(available)), rule=limit_rule)


# In[14]:


#Checking the existing Model
model.pprint()


# In[16]:


#Solving the model
solver = SolverFactory('glpk')
results = solver.solve(model)


# In[17]:


#Printing the Results
if results.solver.termination_condition == TerminationCondition.optimal:
   print("Total Income or Profit:",model.profit())
   for i in range(len(material_type)):
     print("Material Type:",material_type[i], "Optimal Quantity:", model.TL[i].value)
else:
    print("Solve failed.")


# In[ ]:




