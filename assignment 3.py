#!/usr/bin/env python
# coding: utf-8

# #### 1 Write a Python Program to implement your own myreduce() function which works exactly  like Python's built-in function reduce() 

# In[1]:


def myreduce(num):
    lst=list(range(1,number+1))
    summation=0
    
    for i in lst:
        summation +=i
        
    return lst,summation



number=int(input("Please insert the number :"))

output, total=myreduce(number)


print("List of First n Natural numbers are:",output)
print("Sum of List elements are :", total)


# #### 2 Write a Python program to implement your own myfilter() function which works exactly  like Python's built-in function filter() 

# In[4]:



number=int(input("Please insert the number: "))

lst=list(range(1,number+1))


def myfilter(lst):
    even_list=[]
    odd_list=[]
    
    for i in lst:
            if(i%2==0):
                even_list.append(i)
            else:
                odd_list.append(i)
                
    return even_list, odd_list


#Function Execution
even_list, odd_list =myfilter(lst)

#Output

print("Output:")
print("List of numbers:",lst)
print("List of Even numbers  are:",even_list)
print("List of Odd numbers are:", odd_list)


# #### ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']   

# In[6]:


lst =list('xyz')
l=[x*n for x in lst for n in range(1,5) ]
print(l)


# #### ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']   

# In[8]:


l=[x*n for n in range(1,5) for x in lst ]
print(l)


# #### [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

# In[9]:


number=[2,3,4]
n=[[x+n] for x in number for n in range(0,3)]
print(n)


# #### [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]] 
# 

# In[10]:


number=[2,3,4,5]
n=[[x+n for n in range(0,4)] for x in number ]
print(n)


# #### [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)] 

# In[12]:


number=[1,2,3]
n= [(b,a) for a in number for b in number]
print(number_5)


# In[ ]:




