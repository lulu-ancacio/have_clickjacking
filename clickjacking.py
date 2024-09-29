#!/usr/bin/env python
# coding: utf-8

# In[97]:


import requests

def have_clickjacking(site, xframe = '', csp = ''):
    request = requests.get(site)    
    header = request.headers
    #print(header)

    if "x-Frame-Options" in header:
        xframe = (header['X-Frame-Options']).upper()
    if "content-security-policy" in header:
        csp = (header['content-security-policy']).upper()
        
    if xframe == 'SAMEORIGIN' or xframe == 'DENY' or ("FRAME-ANCESTORS 'SELF'" or "FRAME-ANCESTORS 'NONE'") in csp:
        return {
            'ClickJacking':False,
            'X-Frame-Options':xframe,
            'Content-Security-Policy':csp
        }
    else:
        return {
            'ClickJacking':True,
            'X-Frame-Options':xframe,
            'Content-Security-Policy':csp
        }


# In[ ]:





# In[ ]:




