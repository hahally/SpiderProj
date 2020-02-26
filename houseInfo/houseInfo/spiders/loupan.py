# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from houseInfo.items import HouseinfoItem
import json

class LoupanSpider(scrapy.Spider):
    name = 'loupan'
    allowed_domains = ['m.loupan.com']
    start_urls = ['http://m.loupan.com/cs/loupan/',
                  'http://m.loupan.com/cs/loupan/p2/',
                  'http://m.loupan.com/cs/business/',
                  'http://m.loupan.com/cs/business/p2']

    def parse(self, response):
        print("----- parse -----")

        my = HouseinfoItem()

        header = response.css('body > div.pages.pages-xx > div.baseInfo')
        detail = response.css('body > div.pages.pages-xx > div.block')

        #
        for item in header:
            # print(detail[0].css('div.con > div:nth-child(1) > p::text').get())
            my['href'] = response.url
            my['header'] = {
                'name':item.css('h1::text').get(),
                'tag':item.css('div.tag span::text').get(),
                'address':item.css('div:nth-child(6)::text').get(),
                'tel':item.css('div:nth-child(5)::text').get(),
                'average_price':item.css('p.price::text').get(),
                'update':item.css('p.date::text').get(),
                'start_date ':item.css('div:nth-child(4)::text').get(),
            }

        if detail:
            my['base_info'] = {
                'title':detail[0].css('div:nth-child(3) > div.tit::text').get(),
                'start_desc':detail[0].css('div.con > div:nth-child(1) > p::text').get(),
                'end_desc ':detail[0].css('div.con > div:nth-child(2) > p::text').get(),
                'decoration_status':detail[0].css('div.con > div:nth-child(3) > p::text').get(),
                'region_plate ':detail[0].css('div.con > div:nth-child(4) > p::text').get(),
                'pre_sale_license ':detail[0].css('div.con > div:nth-child(5) > p::text').get(),
                'property_rights_years':detail[0].css('div.con > div:nth-child(6) > p::text').get(),
                'proj_feature':detail[0].css('div.con > div:nth-child(7) > p::text').get(),
            }
            my['property_Info'] = {
                'title': detail[1].css('div:nth-child(4) > div.tit::text').get(),
                'company':detail[1].css('div.con > div:nth-child(1) > p::text').get(),
                'category':detail[1].css('div.con > div:nth-child(2) > p::text').get(),
                'costs':detail[1].css('div.con > div:nth-child(3) > p::text').get(),
            }
            my['building_plan'] = {
                'title':detail[2].css('div:nth-child(5) > div.tit::text').get(),
                'developer':detail[2].css('div.con > div:nth-child(1) > p::text').get(),
                'type':detail[2].css('div.con > div:nth-child(2) > p::text').get(),
                'parking_space':detail[2].css('div.con > div:nth-child(3) > p::text').get(),
                'building_area':detail[2].css('div.con > div:nth-child(4) > p::text').get(),
                'area':detail[2].css('div.con > div:nth-child(5) > p::text').get(),
                'households':detail[2].css('div.con > div:nth-child(6) > p::text').get(),
                'volume_rate':detail[2].css('div.con > div:nth-child(7) > p::text').get(),
                'greening_rate':detail[2].css('div.con > div:nth-child(8) > p::text').get(),
            }
            my['project_desc'] = {
                'title':detail[3].css('div:nth-child(6) > div.tit::text').get(),
                'info':detail[3].css('div.con.con2 p::text').getall(),
            }

            my['surrounding'] = {
                'title':detail[4].css('div:nth-child(7) > div.tit::text').get(),
                'info':detail[4].css('div.con.con2 p::text').getall(),
            }

            my['community'] = {
                'title':detail[5].css('div:nth-child(8) > div.tit::text').get(),
                'info':detail[5].css('div.con.con2 p::text').getall(),
            }
            my['traffic_condition'] = {
                'title':detail[6].css('div:nth-child(9) > div.tit::text').get(),
                'info':detail[6].css('div.con.con2 p::text').getall(),
            }
            yield my

        next_urls = []    # 保存下一页链接
        next_info = []    # 保存详情链接
        # 第一页
        if response.url==self.start_urls[0]:
            next_info += response.css('div.list > div.item > a::attr(href)').getall()

         # 第 1 页之后
        if str(response.url).split('/')[-2][0]== 'p':
            data = json.loads(response.text)
            next_page = data['next_page']
            href = Selector(text=data['list_item']).css('a::attr(href)').getall()
            if data['list_item']:
                next_urls.append(next_page)
                next_info += href


        for info in next_info:
            info_url = info+'info/'
            yield scrapy.Request(url=info_url, callback=self.parse)

        for next_url in next_urls:
            url = next_url
            yield scrapy.Request(url=url,callback=self.parse)

    def close(spider, reason):
        # 在 close_spider 之后
        # spider close reason
        print("----- spider close: %s -----"%reason)
