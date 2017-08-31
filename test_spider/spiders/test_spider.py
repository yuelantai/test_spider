from scrapy.spiders import CrawlSpider;
from scrapy.linkextractors import LinkExtractor;
from scrapy.loader import ItemLoader;

from test_spider.items import HouseItem;

class test_spider(CrawlSpider):
    name="test_spider"
    allowed_domains=["shenzhen.qfang.com"];
    start_urls = [
        "http://shenzhen.qfang.com/newhouse/list",
        "http://newhouse.sz.fang.com/house/s/",
    ];
    rules = [
        Rule(LinkExtractor(allow=(r"shenzhen\.qfang\.com.*",)), callback='parse_new_house', follow=True),
        Rule(LinkExtractor(allow=(r"newhouse\.sz\.fang.com.*",)), callback='parse_new_house', follow=True),
    ];
    
    def parse_new_house(self,response):
        self.logger.info(reponse.url);
        house_items=response.xpath("//ul[@id='newhouse-list']//i[@class='clearfix']");
        
        items=[];
        for house_item in house_items:
            item=HouseItem();
            item["name"]=house_item.xpath("");
            item["alias"]=house_item.xpath("");
            item["desc"]=house_item.xpath("");
            item["price"]=house_item.xpath("");
            item["discount"]=house_item.xpath("");
            item["house_type"]=house_item.xpath("");
            item["open_qt_time"]=house_item.xpath("");
            item["close_qt_time"]=house_item.xpath("");
            item["addr"]=house_item.xpath("");
            item["is_on_sell"]=house_item.xpath("");
            item["tag"]=house_item.xpath("");
            item["url"]=house_item.xpath("");
            item["phone_number"]=house_item.xpath("");
            item["house_pic"]=house_item.xpath("");
            item["house_type_pic"]=house_item.xpath("");
            items.append(item);
        return items;
    