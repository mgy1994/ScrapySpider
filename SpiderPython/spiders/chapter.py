# -*- coding: utf-8 -*-
#获取第一章URL
import scrapy
import re
import json
from qidian.items import Item

#获取书名ID的json文件
f = file(r'C:\qidian\rankID.json')
jsonobj = json.load(f)
jsonstr= str(jsonobj)

pattern = re.compile(r'\d+')
index = re.search(pattern,jsonstr)
# print index.group(0)

class ChapterScrapy(scrapy.Spider):
	name = 'chapter'
	allowed_domains=["http://read.qidian.com/BookReader/"+str(index.group(0))+".aspx"]
	start_urls=["http://read.qidian.com/BookReader/"+str(index.group(0))+".aspx"]

	def parse(self, response):
    		item = Item()
    		content = response.body
    		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    		print response.xpath("//div[@class='box_cont'][2]/div/ul/li[1]/a/@href").extract()
    		print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    		item['contentURL'] = response.xpath("//div[@class='box_cont'][2]/div/ul/li[1]/a/@href").extract()
    		yield item