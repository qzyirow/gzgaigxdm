# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:40:25 2020

@author: yiren
"""

import requests
import os
from urllib.request import urlopen
import re

url = 'http://www.bbsnet.com/'

# index_page = requests.get(url)
# # print(r.text)

html = urlopen(url).read().decode('utf-8')
# print(html)
# print(type(html))


# # find body of html
# key = r'<body.*</body>'
# body = re.search(key, html)
# print(body)


# # direct search
class_name = r'<li class="post box row fixed-hight">'
# class_num = len(re.findall(class_name, html))
# print(class_num)
# # has 30 object

position_list = []
positions = re.finditer(class_name, html)
for p in positions:
    # print(p)
    position_list.append(p.start())
# print(position_list)
# print(type(position_list[0]))

components = []
for i in range(len(position_list)):
    if i == len(position_list)-1:
        component = html[position_list[i]::]
    else:
        component = html[position_list[i]:position_list[i+1]]
    components.append(component)
# print(components[0])

ref = r'href=".*?"'
img = r'img src=".*?" '
title = r'title=".*?"'
print(re.search(ref, components[0]))
print(re.search(img, components[0]))
print(re.search(title, components[0]))
# print(components[0][329:404])
# res = re.search(r'(href=".*?")+[.*](img src=".*?")+[.*](title=".*?")+',components[0])
# res = re.match(r'(?P<ref>href=".*?")',components[0])
# print(res)


results = []
for element in components:
    result = {}
    result['title'] = re.search(title, element).group()
    result['link'] = re.search(ref, element).group()
    result['emoticon'] = re.search(img, element).group()
    results.append(result)

print(results)




# ----------------------------------------------
# test on regex

test = """
abc

<qzyirow>
 i like playing 
</qzyirow>

abc

<qzyirow1>
 i like sleeping
</qzyirow1>

abc

<qzyirow>
 i like eating
</qzyirow>
"""
# print(test)

abc = 'a'
res = re.search(abc, test)
# print(res)
# test_key = r'(<qzyirow>).*(</qzyirow>)'
test_key = r'qzyirow'
ptn = re.compile(test_key)
# print(re.search(ptn, test))
# print(re.findall(ptn, test))
res2 = re.finditer(test_key, test)
# print(res2)
# ----------------------------------------------


