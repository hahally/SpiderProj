# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    href = scrapy.Field()
    base_info = scrapy.Field()
    header = scrapy.Field()
    property_Info = scrapy.Field()
    building_plan = scrapy.Field()
    project_desc = scrapy.Field()
    surrounding = scrapy.Field()
    community = scrapy.Field()
    traffic_condition = scrapy.Field()

