# -*- coding: utf-8 -*-
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohua.com']
    start_urls = ['http://xiaohua.com/']

    def parse(self, response):
        pass
