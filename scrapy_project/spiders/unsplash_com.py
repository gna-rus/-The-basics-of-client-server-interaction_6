import scrapy
from scrapy.http import HtmlResponse # Импортирую методы типа HtmlResponse
from pprint import pprint
from scrapy import Selector
from jobparser.items import JobparserItem
import wget

class UnsplashComSpider(scrapy.Spider):
    name = "unsplash_com"
    allowed_domains = ["unsplash.com"]

    def __init__(self, query=None):
        super().__init__()
        self.start_urls = [f"https://unsplash.com/s/photos/{query}"]


    def parse(self, response):
        print(self.start_urls)
        links = response.xpath("//figure[@data-testid='photo-grid-masonry-figure']/link[@itemprop='acquireLicensePage']/@href").getall() # возвращает список ссылок всех атрибутов страницы по xpath
        print(links)
        for link in links:
            yield response.follow(link, callback=self.parse_img)

    def parse_img(self, response: HtmlResponse):
        commit = response.xpath('//p[@class="liDlw"]/text()').get()
        author = response.xpath('//a[@class="vGXaw uoMSP kXLw7 R6ToQ JVs7s R6ToQ"]/text()').get()
        loggin_of_author = response.xpath('//a[@class="vGXaw uoMSP kXLw7 R6ToQ JVs7s R6ToQ"]/@href').get()
        Published_datatime = response.xpath('//span[@class="IwfFI jhw7y"]/span/time/text()').get()
        url_img = response.xpath('//img[@class="I7OuT DVW3V L1BOa"]/@srcset').get()
        print(author, loggin_of_author)
        print(commit)
        print(Published_datatime)
        print(url_img)
        yield JobparserItem(author=author, commit=commit, Published_datatime=Published_datatime, url_img=url_img)
