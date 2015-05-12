# -*- coding: utf-8 -*-
#获取第一章内容
import scrapy
import json
import re
from qidian.items import Item

#获取章节URL的json文件
f = file(r'C:\qidian\contentURL.json')
jsonobj = json.load(f)
jsonstr= str(jsonobj)
pattern = re.compile(r'\d+')
url1 = re.findall(pattern,jsonstr)
print url1

class ContentScrapy(scrapy.Spider):
	name = 'content'
	allowed_domains=["http://files.qidian.com/Author5/"+url1[0]+"/"+url1[1]+".txt"]
	start_urls=["http://files.qidian.com/Author5/"+url1[0]+"/"+url1[1]+".txt"]

	def parse(self, response):
    		item = Item()
    		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    		print response.body
    		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    		item['content'] = response.body.decode(response.encoding)
    		yield item    	