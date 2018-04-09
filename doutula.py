# -*- coding:utf-8 -*-
import requests
import random
from lxml import etree 
from tempfile import NamedTemporaryFile

keyword = "喜欢你"
res = requests.get('https://www.doutula.com/search', {'keyword': keyword})
html = etree.HTML(res.text)
url = 'http:' + random.choice(html.xpath('//div[@class="image-container"][1]//img[contains(@class, "img-responsive")]/@data-original'))
res = requests.get(url, allow_redirects=False)
f = open("1.jpg","wb")
f.write(res.content)
f.close()