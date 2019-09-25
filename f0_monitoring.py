#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
n = int(input("number of channels "))
arr = [float(input("Enter the initial temperature of channel ")) for i in range(n)]
f0 = float(input("Enter the desired F0 value "))
z = int(input("Enter the Z value "))
_f0 = 0


# In[56]:


import random
min_temp = []
min_time = []
all_temp = []
all_time = []
all_f0 = []
for i in range(n):
    print("**********************")
    all_temp.append([])
    all_time.append([])
    temp = arr[i]
    _f0=0 
    while temp < 200.00:
        for time in range(240):
            t = 1
            y = (temp-121.1)/z
            _f0 += float(pow(10,y)) 
            _f0 = round(_f0,3)
            print(time,"TEMP: ",temp, "F0: ",_f0)
            all_time[i].append(time)
            if _f0 ==0.001:
                min_time.append(time)
            all_temp[i].append(temp)
            temp += round(random.uniform(0.3,1.5),2)
            temp = round(temp,2) 
            if round(_f0) >= f0:
                all_f0.append(_f0)
                time1 = time
                while temp > 100.00:
                    for time_con in range(time1,240):
                        t = 1
                        y = (temp-121.1)/z
                        _f0 += float(pow(10,y))         
                       # print("TEMP: ",temp, "F0: ",round(_f0,3))
                        temp -= round(random.uniform(0.3,1.5),2)
                        temp = round(temp,2)
                    break
                break
        break
        
                
            
        
           
                    
                
                    
    


# # Calculating the come up time

# In[57]:


print("MIN TIME: ",min_time)
cut = min(min_time)
print(cut)


# # Finding the minimum temperature 

# In[58]:


cu_temp = []
for j in range(n):
    cu_temp.append(all_temp[j][cut])
minT = min(cu_temp)
print(minT)
for k in range(n):
    if cu_temp[k] == minT:
        print(k)


# # Calculate the process time

# In[59]:


all_time[k]
process_end = all_time[k].pop()
print(process_end)
process_time = process_end - cut
achieved_f0 = all_f0[k]
print("F0 achieved: ", achieved_f0)
print("process start time: ", cut)
print("process end time: ",process_end)
print("PROCESS TIME: ", process_time)

