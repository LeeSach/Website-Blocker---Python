#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from datetime import datetime as dt
import ctypes, sys


# In[2]:


#we need to add those site to host file during working hours and removing them immediately when it’s go home time.
sites_to_block = [
    'www.facebook.com', 'facebook.com',
    'www.youtube.com', 'youtube.com',
    'www.gmail.com', 'gmail.com'
]


# In[3]:


#This step initializes all the required variables that will be used in the script. Here, the host_path is set to the path of the 
#hosts file. In python, r is used to represent the raw string.
#The redirect is assigned to the localhost address, i.e. 127.0.0.1. 

Linux_host = '/etc/hosts'
#Window_host = r"C:\Windows\System32\drivers\etc\hosts"
#Had to change url of Window_host from host file which is in System32 folder which requires permissions to write and read. 
#Host.txt is now on desktop and i am not getting error now
Window_host = r"C:\Users\mufar\Desktop\hosts.txt"
default_hoster = Window_host
redirect = "127.0.0.1"


# In[4]:


def block_websites(start_hour , end_hour):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour): 
            print("Do the work ....")
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in  sites_to_block:
                    if site not in hosts:
                       hostfile.write(redirect+' '+site+'\n')
        else:
            with open(default_hoster, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print('Good Time')
        time.sleep(3)


# In[ ]:


if __name__ == '__main__':
    block_websites(9, 17)


# In[ ]:




