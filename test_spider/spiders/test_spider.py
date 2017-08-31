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
        house_items=response.xpath("//ul[@id='newhouse-list']//li[@class='clearfix']");
        
        items=[];
        for house_item in house_items:
            item=HouseItem();
            
            title_sel=house_item.xpath("div[@class='show-detail fl']/p[1]");
            item["name"]=title_sel.xpath("a")[0].extract();
            item["discount"]=title_sel.xpath("span/em")[0].extract();
            item["is_on_sell"]=title_sel.xpath("i")[0].extract();
            item["url"]=house_item.xpath("a@href")[0].extract();
            
            dtl_sel=house_item.xpath("div[@class='show-detail fl']/div[1]");
            item["alias"]=dtl_sel.xpath("p[1]/span[2]")[0].extract();
            item["desc"]="";    #dtl_sel.xpath("")[0].extract();
            item["room_types"]=dtl_sel.xpath("p[2]/span[2]")[0].extract();
            item["open_qt_time"]=dtl_sel.xpath("div[1]/p[1]/span[1]")[0].extract();
            item["close_qt_time"]=dtl_sel.xpath("div[1]/p[1]/span[2]")[0].extract();
            item["zone"]=dtl_sel.xpath("p[3]/span[2]")[0].extract();
            item["addr"]=dtl_sel.xpath("p[3]/span[2]/em")[0].extract();
            item["tag"]=" ".join(tag.extract() for tag in dtl_sel.xpath("div/div[2]/p"));
            
            oth_inf_sel=house_item.xpath("div[@class='show-price']");
            item["price"]=oth_inf_sel.xpath("span[1]")[0].extract();
            item["price_unit"]=oth_inf_sel.xpath("span[2]")[0].extract();
            item["phone_number"]=oth_inf_sel.xpath("p[1]/i")[0].extract();
            item["house_type_pic"]=[img.extract() for img in oth_inf_sel.xpath("div[@class='dm-photo']/ul/li/a/img@src")];
            
            photo_sel=house_item.xpath("p[@class='house-photo fl']");
            item["house_pic"]=photo_sel.xpath("a/img@src")[0].extract();
            item["house_type"]=photo_sel.xpath("span/em")[0].extract();
            
            items.append(item);
        return items;
    