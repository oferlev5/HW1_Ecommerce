#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import networkx as nx
import random
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('instaglam_1.csv')
G = nx.from_pandas_edgelist(df, source = "userID", target = "friendID" )
# color_map = []
# for node in G:
#     if node == 145:
#         color_map.append('blue')
#     else: 
#         color_map.append('green')      
# nx.draw(G, node_color=color_map, with_labels=True)
nx.draw(G, with_labels=True)




# nx.draw(G,pos,with_labels = True)
# plt.savefig('graph.png', dpi = 1000)


# In[3]:


# nx.clustering(G)


# In[4]:


dick = nx.triangles(G)
val = dick.values()
total = sum(val)
total


# In[5]:


print(nx.transitivity(G))


# In[6]:


df0 = pd.read_csv('instaglam0.csv')
G0 = nx.from_pandas_edgelist(df0, source = "userID", target = "friendID" )
nx.draw(G0,with_labels = True)


# In[7]:


print(nx.transitivity(G0))


# In[8]:


dick0 = nx.triangles(G0)
val0 = dick0.values()
total0 = sum(val0)
total0


# In[9]:


G.number_of_edges()


# In[10]:


G0.number_of_edges()


# In[11]:


G.number_of_edges()-G0.number_of_edges()


# In[12]:


1607/1147665


# ### נסיון 2 של שחר ועופר
# 

# In[13]:


nx.number_connected_components(G)


# In[14]:


nx.number_connected_components(G0)


# ניתן לראות שמעבר בין מצב -1 לבין מצב 0 מספר רכיבי הקישורת לא קטן. ידוע כי קשתות רק נוצרות ולא נמחקות ולכן אנו מסיקים שההסתברות ליצירת קשת  בין שני רכיבי קשירות בגרף היא 0

# #### בתוך רכיבי קשירות

# In[15]:


M = nx.Graph()


# In[16]:


M.add_edges_from([('a','b') , ('b','c'), ('b','d'), ('a','e'), ('e','d')])


# In[17]:


nx.draw(M,with_labels = True)


# In[18]:


list1 = nx.triangles(M)
list1


# In[19]:


nx.transitivity(M)


# In[20]:


def get_open_triangles_node(G, node):
    open_triangles = []
    neighbors1 = set(G.neighbors(node))

    for node1 in neighbors1:
        # remove the target node from the target node's neighbor's
        # neighbor's, since it will certainly go back to itself
        neighbors2 = set(G.neighbors(node1))
        neighbors2.discard(node)

        for node2 in neighbors2:
            neighbors3 = set(G.neighbors(node2))

            if node not in neighbors3:
                open_triangle = set([node])
                open_triangle.update([node1, node2])
                open_triangles.append(open_triangle)
    
    return len(open_triangles)


# In[21]:


def count_open_triangles(G):
    count = 0
    nodes = list(G.nodes)
    for node in nodes:
        count += get_open_triangles_node(G, node)
    return int(count/2)


# In[22]:


count_open_triangles(M)


# In[23]:


count_open_triangles(G)


# In[24]:


nx.transitivity(G)


# In[25]:


dick = nx.triangles(G)
val = dick.values()
total = sum(val)
total/3


# In[ ]:





# In[26]:


def prob(G,u,v):
    return len(sorted(nx.common_neighbors(G,u,v)))/count_open_triangles(G)
    


# In[27]:


prob(M,'a','b')


# In[36]:


S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
# nx.draw(S[0],with_labels = True)
nodes1 = list(S[0].nodes)
nodes2 = list(S[0].nodes)
list_of_prob = []
open_t = count_open_triangles(S[0])
for n1 in nodes1:
    for n2 in nodes2:
        if n1 != n2:
            prob1 = len(sorted(nx.common_neighbors(G,n1,n2)))/open_t
            temp = (prob1,n1,n2)
            list_of_prob.append(temp)
list_of_prob


# In[38]:


# for x in list_of_prob:
#     if x[1] == :
#         print(x)
#

# In[29]:


S0 = [G0.subgraph(c).copy() for c in nx.connected_components(G0)]
nx.draw(S0[17],with_labels = True)
len(S0[19].edges)
prob(S0[17], 939109,898006)


# 
