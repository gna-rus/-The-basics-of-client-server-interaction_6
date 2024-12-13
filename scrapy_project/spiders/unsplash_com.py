import scrapy
from scrapy.http import HtmlResponse # Импортирую методы типа HtmlResponse
from pprint import pprint
from scrapy import Selector
from jobparser.items import JobparserItem
from scrapy.loader import ItemLoader

class UnsplashComSpider(scrapy.Spider):
    name = "unsplash_com"
    allowed_domains = ["unsplash.com"]

    def __init__(self, query=None):
        super().__init__()
        self.start_urls = [f"https://unsplash.com/s/photos/{query}"]


    def parse(self, response):
        """Функция, возвращающая ссылки всех результатов поиска.
        По этим ссылкам паук в дальнейшем будет переходить и на новых страницах собирать информацию"""
        print(self.start_urls)
        links = response.xpath("//figure[@data-testid='photo-grid-masonry-figure']/link[@itemprop='acquireLicensePage']/@href").getall() # возвращает список ссылок всех атрибутов страницы по xpath
        print(links)
        for link in links:
            # переходим по ссылке и на новой странице проводим сбор информации
            yield response.follow(link, callback=self.parse_img)

    def correct_url(self, value: str):
        """Функция для обработки пакета ссылок картинок"""
        print(value)
        return [value.split(" ")[0]]

    def parse_img(self, response: HtmlResponse):
        """Функция для формирование пакеда данных и выгрузки с сайта в items.py"""
        loader = ItemLoader(item=JobparserItem(), response=response)
        loader.add_xpath('commit', '//p[@class="F7hSb"]/text()')
        loader.add_xpath('author', '//a[@class="bimlc Pc_c1 rkYpC KZwZl wQd_A KZwZl"]/text()')
        loader.add_xpath('loggin_of_author', '//a[@class="dYuCf"]/@href')
        loader.add_xpath('Published_datatime', '//span[@class="X5fE_ yZhvJ"]/span/time/text()')
        # loader.add_xpath('image_urls', '//img[@class="I7OuT DVW3V L1BOa"]/@srcset')

        image_urls = response.xpath('//img[@class="tzC2N fbGdz cnmNG"]/@srcset').get()
        loader.add_value('image_urls', self.correct_url(image_urls))

        # передаем loader в pipelines
        yield loader.load_item()




