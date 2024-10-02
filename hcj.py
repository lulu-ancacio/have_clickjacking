#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def hcj(root_domain, xframe = '', csp = ''):
    
    site = 'http://'+root_domain
    
    request = requests.get(site)    
    header = request.headers
    html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Have ClickJacking?</title>
</head>
<body>
    <h1>- Have ClickJacking? <br>
        - Yes, look!</h1>
    <iframe width=830px height=550px src="{site}"></iframe>
</body>
</html>
'''

    def criar_html(html, url):
        with open(('hcj_'+url+'.html'), 'w') as arq:
            arq.write(html)
    
    if 'x-Frame-Options' in header:
        xframe = (header['X-Frame-Options']).upper()
    if 'content-security-policy' in header:
        csp = (header['content-security-policy']).upper()
        
    resultado = {
            'ClickJacking': None,
            'X-Frame-Options':xframe,
            'Content-Security-Policy':csp
        }
        
    if xframe == 'SAMEORIGIN' or xframe == 'DENY' or ("FRAME-ANCESTORS 'SELF'" or "FRAME-ANCESTORS 'NONE'") in csp:
        resultado['ClickJacking'] = False
        return resultado
    else:
        criar_html(html, root_domain)
        resultado['ClickJacking'] = True
        return resultado

