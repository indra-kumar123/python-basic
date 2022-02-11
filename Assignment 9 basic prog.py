#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Disarium number


import math

def digitsCount(Number):
    length = 0
    while Number != 0:
        length = length + 1
        Number = Number // 10
    return length

def digitsSum(Number, length):
    Sum = 0
    rem = 0

    while Number > 0:
        rem = Number % 10
        Sum = Sum + math.pow(rem, length)
        Number = Number // 10
        length = length - 1
    return Sum


Number = int(input("Enter the Number to Check Disarium Number = "))
length = digitsCount(Number)
Sum = digitsSum(Number, length)

print("The Sum of the Digits     = %d" %Sum)

if Sum == Number:
    print("%d is a Disarium Number." %Number)
else:
    print("%d is Not a Disarium Number." %Number)


# In[11]:


# Disarium number between 1 to 100

def Length(n):    
    length = 0;    
    while(n != 0):                    
        length = length + 1;    
        n = n//10;    
    return length;    
     
#sumDigit()  
def sumdigit(num):    
    rem = sum = 0;    
    len = Length(num);     
        
    while(num > 0):    
        rem = num%10;   
        sum = sum + (rem**len);    
        num = num//10;    
        len = len - 1;    
    return sum;    
      
result = 0;    
     

print("Disarium numbers between 1 and 100 are");    
for i in range(1, 101):          
    result = sumdigit(i);    
        
    if(result == i):    
        print(i),   


# In[16]:


## Happy number

def numSquareSum(n):
    squareSum = 0;
    while(n):
        squareSum += (n % 10) * (n % 10);
        n = int(n / 10);
    return squareSum;
 

def isHappynumber(n):
 

    slow = n;
    fast = n;
    while(True):
         
        
        slow = numSquareSum(slow);
 
        
        fast = numSquareSum(numSquareSum(fast));
        if(slow != fast):
            continue;
        else:
            break;
 
   
    return (slow == 1);
 
n = 100;
if (isHappynumber(n)):
    print(n , "is a Happy number");
else:
    print(n , "is not a Happy number");


# In[20]:


# Harshad number

number = int(input('Enter number: '))


copy = number


digit_sum = 0

while number:
    digit_sum += number%10
    number //= 10


if copy%digit_sum == 0:
    print('%d is Harshad Number' % (copy))
else:
    print('%d is Not Harshad Number' % (copy))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




