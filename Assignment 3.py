#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Q 1.  Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# l = (8, 2, 3, 0, 7)
# print(sum(l))

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total 
    
    
# l = (8, 2, 3, 0, 7)
print(sum((8,2,3,0,7)))


# In[7]:


# Q 2. Write a Pyhton program to reverse a string
# Sample input: '1234abcd'
# Sample output:'dcba4321'

def value_reverse(value):
    reverse= value[::-1]
    print(reverse)
    
sample_input = '1234abcd'
result = value_reverse(sample_input)


# In[41]:


# Q 3.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters


string : 'The quick Brow Fox'

    
upper, lower = 0, 0

for a in string:
    #first we've to count the total number of upper case characters in the string
    if (a.isupper()):
        upper = upper + 1
     #then we've to count the total number of lower case characters in the string   
    elif (a.islower()):
        lower = lower +1
        
print("No. of upper case characters", upper)
print("No. of lower case characters", lower)


# In[ ]:




