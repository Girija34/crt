#!/usr/bin/env python
# coding: utf-8

# In[3]:


str1="india"
print(str1*10,)


# In[6]:


text='india is great'
print(text.title())


# In[7]:


text='India Is Great'
print(text.swapcase())


# In[8]:


text='India, Is, Great'
print(text.split())


# In[11]:


print('-'.join(['India','Is', 'Great']))


# In[13]:


str1='donkey monkey'
print(list(enumerate(str1)))


# In[14]:


str1='66'
print(str1.zfill(4))


# In[5]:


val=int(input())
x=0
y=0
for i in range(1,val+1):
    if(i%2!=0):
        x=x+7
    else:
        y=y+6
if(val%2!=0):
    print('{} term in the program is {}'.format(val,x-7))
else:
    print('{} term in the program is {}'.format(val,y-6))


# In[8]:


a=int(input("enter the term"))
if a%2==0:
    a=a//2
    print(6*(a-1))
else:
    a=a//2+1
    print(7*(a-1))


# In[11]:


import string
ch='g'
print('a'<=ch <='z')


# In[12]:


str1="hello"
print(dir(str1))


# In[13]:


import re
str1="she sells sea shells at sea shore"
p1="sells"
if re.search(p1,str1):
    print("match found")
else:
    print(p1,"not present in string")


# In[14]:


import re
str1="she sells sea shells at sea shore"
p1="sells"
rep='ocean'
ns=re.sub(p1,rep,str1,1)
print(ns)


# In[16]:


import re
p=r"[aeiou]"
if re.search(p,"clue"):
    print("matchy vowel")


# In[17]:


import re
p=r"[bcdfghjklmnpqrstvwxyz]"
if re.search(p,"clue"):
    print("matchy vowel")


# In[18]:


import re
p="[listen,silent]"
if re.search(p,"clue"):
    print("true")


# In[25]:


str1='listen'
str2='silent'
if len(str1)==len(str2):
    print("true")
else:
    print("false")


# In[36]:


n=int(input())
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+2
    else:
        b=b+1
if(n%2!=0):
    print('{}'.format(a-2))
else:
    print('{}'.format(b-1))


# In[30]:



a=int(input("enter the term"))
if a%2==0:
    a=a//2
    print(1*(a-1))
else:
    a=a//2+1
    print(2*(a-1))


# In[32]:


a=int(input("enter the term"))
if a%2==0:
    a=a//2
    print(1*(a-1))
else:
    a=a//2+1
    print(2*(a-1))


# In[39]:


size=int(input("enter the size of the bin"))
max=count=flag=0
x=input()
arr=list(x)
for i in range (0,size):
    if arr[i]=='1':
        count=count+1;
        flag=1;
    elif (arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count >max:
        max=count
print(max)
        


# In[40]:


size=int(input("enter the size of the bin"))
max=count=flag=0
x=input()
arr=list(x)
for i in range (0,size):
    if arr[i]=='1':
        count=count+1;
        flag=1;
    elif (arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count >max:
        max=count
print(max)
        


# In[ ]:




