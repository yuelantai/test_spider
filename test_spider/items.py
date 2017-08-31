# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field;

class HouseItem(Item):
    name=Field();
    alias=Field();
    desc=Field();
    price=Field();
    discount=Field();
    house_type=Field();
    open_qt_time=Field();
    close_qt_time=Field();
    addr=Field();
    is_on_sell=Field();
    tag=Field();
    url=Field();
    phone_number=Field();
    house_pic=Field();
    house_type_pic=Field();
    
