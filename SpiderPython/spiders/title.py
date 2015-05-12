# -*- coding: utf-8 -*-
# 获取排行榜名称
import scrapy
from qidian.items import Item

class QidianSpider(scrapy.Spider):
    name = "title"
    allowed_domains = ["top.qidian.com"]
    start_urls = ["http://top.qidian.com","http://script.cmfu.com/Script/Top.js"]

    def parse(self, response):
    	print response.xpath("//div[@class='rankcontent']")
        for x in response.xpath("//div[@class='rankcontent']"):
            item = Item()    
            item['title'] = x.xpath("//div[@class='rankcontent']//div[@class='title']/h3/text()").extract()           
            yield item