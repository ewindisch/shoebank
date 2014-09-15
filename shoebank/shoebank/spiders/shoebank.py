import scrapy
import scrapy.contrib.spiders as spiders
import urlparse

class Shoe(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    color = scrapy.Field()
    price = scrapy.Field()
    size = scrapy.Field()
    width = scrapy.Field()
    style = scrapy.Field()


def request_generator():
   for full_size in range(5, 17):
        for half_size in (0, 5):
            size = "%02i%i" % (full_size, half_size)

            for width in ('3A', '2A', 'A', 'B', 'C', 'D', 'E', '2E', '3E'):
                yield scrapy.FormRequest("http://shoebank.com/FactorySecondInventory.php", formdata={'SIZE': size, 'DIM': width, 'STATUS': 'All Styles', 'LAST': '', 'SUB_DEPT': '', 'SORT_BY': 'Price (low to high)'})


class ShoeBankSpider(spiders.CrawlSpider):
    name = 'shoebank'
    allowed_domains = ['shoebank.com']
    #start_urls = ['']

    def start_requests(self):
        return request_generator()
        #[scrapy.FormRequest("http://shoebank.com/FactorySecondInventory.php", formdata={'SIZE': '105', 'DIM': '3E', 'STATUS': 'All Styles', 'LAST': '', 'SUB_DEPT': '', 'SORT_BY': 'Price (low to high)'})]

    def parse(self, response):
        for sel in response.xpath('//td'):
            shoe = Shoe()
            shoe['url'] = sel.xpath("a[@class='GenericLink2']/@href").extract()
            shoe['name'] = sel.xpath("a/div[@class='shoeBankName']/text()").extract()
            shoe['price'] = sel.xpath("a/div[@class='shoeBankPrice']/text()").extract()
            shoe['color'] = sel.xpath("a/div[@class='shoeBankColor']/text()").extract()
            #shoe['style'] = sel.xpath("a/span[@class='shoeBankStyle']/text()").extract()

            surl = urlparse.urlparse(bytes(sel.xpath("a[@class='GenericLink2']/@href").extract()))
            query = urlparse.parse_qs(surl.query)
            shoe['width'] = query.get('DIM')
            shoe['size'] = query.get('SIZE')
            shoe['style'] = query.get('STY')
            yield shoe
