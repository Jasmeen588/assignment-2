#!/usr/bin/env python
# coding: utf-8

#  Assignment Day 3
#  Submitted By Jasmeen kaur

# Ques1 :You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
# 1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
# the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
# later”
# 

# In[1]:


height = int(input("Enter the altitude: "))
if height<=1000:
    print("Land the plane")
elif height>1000 and height<=5000:
    print("Come down to 1000ft")
else:
    print("Go around and try later")


#  Ques2: Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE
# function.
# 

# In[3]:


for i in range(2,200): 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 


# In[ ]:




