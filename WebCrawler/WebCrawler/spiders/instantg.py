
import scrapy
from scrapy import Request
from WebCrawler.items import ReviewsInstantItem
import time
from urllib.parse import urlparse
from urllib.parse import parse_qs


class InstantgSpider(scrapy.Spider):
    name = 'instantg'
    allowed_domains = ['www.instant-gaming.com']
    start_urls = ['http://www.instant-gaming.com/']

    def parse(self, response):
        pass

class InstantgSpider(scrapy.Spider):
    name = 'instantg'
    allowed_domains = ['www.instant-gaming.com']
    platforme = ['steam','playstation-5','ubisoft-connect']
    start_urls = [[f'https://www.instant-gaming.com/en/search/?type%5B0%5D={i}&page={n}' for i in ['steam','playstation-5','ubisoft-connect'] ]for n in range(1,4)]

    
    def start_requests(self):
        for urls in self.start_urls:
            for url in urls :
                parsed_url = urlparse(url)
                self.captured_value = parse_qs(parsed_url.query)['type[0]']

                yield Request(url=url, callback=self.parse_instant)
                

    def parse_instant(self, response):
        liste_indices = response.css('.item')

        for instant in liste_indices:
            item = ReviewsInstantItem()
            
            try: 
              item['title'] = instant.css('.information .title ::text').extract()
            except:
              item['title'] = 'None'
            
            try: 
              item['img'] =  instant.css('.picture ::attr(data-src)').extract()
            except:
                item['img'] = 'None'        
            try: 
              item['price'] =  instant.css('.information .price ::text').extract()
            except:
                item['price'] = 'None'
            
            try: 
              item['discount'] = instant.css('.discount ::text').extract()
            except:
              item['discount'] = 'None'
            
            try: 
              item['time'] = time.strftime('%d/%m/%Y ::%H:%M:%S')
            except:
              item['time'] = 'None'
            
            try: 
              item['platform'] = "None"
            except:
              item['platform'] = 'None'
            
      

   
            yield item