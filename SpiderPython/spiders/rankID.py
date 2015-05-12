# -*- coding: utf-8 -*-
#获取排行榜图书书号
import scrapy
import re
from qidian.items import Item

class RankSpider(scrapy.Spider):
    name = "rank"
    allowed_domains = ["http://script.cmfu.com/Script/Top.js"]
    start_urls = ['http://script.cmfu.com/Script/Top.js']
  
    def parse(self, response):
        item = Item()  
        content = response.body
        pattern1 = re.compile(r'new Book\(\'\d+\'')
        item1 = re.findall(pattern1,content)

        pattern2 = re.compile(r'new Book\(')
        item2 = re.split(pattern2,str(item1))
        print '!!!!!!!!!!!!!!!!!!!!!!!!!'
        print item2
        print '!!!!!!!!!!!!!!!!!!!!!!!!!'               
        
        item['rankID']=item2
        yield item