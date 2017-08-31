# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field;

class HouseItem(Item):
    name=Field();
    alias=Field();
    house_type=Field();
    is_on_sell=Field();
    desc=Field();
    price=Field();
    price_unit=Field();
    discount=Field();
    room_types=Field();
    open_qt_time=Field();
    close_qt_time=Field();
    zone=Field();
    addr=Field();
    tag=Field();
    url=Field();
    phone_number=Field();
    house_pic=Field();
    house_type_pic=Field();
    
