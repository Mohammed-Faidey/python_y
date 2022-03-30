#!/usr/bin/env python
# coding: utf-8

# In[1]:



def solve(a,b):
    a = a.lower() 
    b = b.lower()
    # case 3
    if (a == b) and ('*' not in a) :
        print(" string: {} and string: {} is the same string".format(a,b))
        return True
    
    
    elif (a != b )and ('*' in a ):
        
        for i in range(0, len(a)):
            astrix_locs = []
            
            if a[i] == '*':
                
                astrix_locs.append(i)
                print(astrix_locs)
                
        return True
                
    else :
        return False
        
                


# In[3]:


def tokens(str1):
    # 
    str1 = str1.lower()
    str1Len = len(str1)
    str_rep = []
    for i in range(0, str1Len+1):
        stop_times = 0
        str_rep.append(str1[stop_times : i])
        i +=1
       
        #print(str_rep)
    return str_rep


# In[4]:


def str_rep(tokens_list, dad_str) : 
    
    
    sons_tuples = []
    for son_str in tokens_list:
        sons_tuples.append((son_str, dad_str.count(son_str)))
    return sons_tuples 


# In[ ]:




