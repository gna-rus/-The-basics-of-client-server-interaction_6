import scrapy
from scrapy.http import HtmlResponse # Импортирую методы типа HtmlResponse

class UnsplashComSpider(scrapy.Spider):
    name = "unsplash_com"
    allowed_domains = ["unsplash.com"]

    def __init__(self, query=None):
        super().__init__()
        self.start_urls = [f"https://unsplash.com/s/photos/{query}"]


    def parse(self, response):
        print(self.start_urls)
        links = response.xpath("//img[@class='I7OuT DVW3V L1BOa']").getall() # возвращает список ссылок всех атрибутов страницы по xpath
        print(links)
        for link in links:
            yield response.follow(link, callback=self.parse_img)

    def parse_img(self, response: HtmlResponse):
        print(1, end = '\n\n\n')




