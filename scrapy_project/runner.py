# Это файл для удобного запуска пауков

from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy_project.spiders.hhru import HhruSpider
from scrapy_project.spiders.unsplash_com import UnsplashComSpider

if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    process = CrawlerProcess(get_project_settings())
    process.crawl(UnsplashComSpider, query='cat')
    process.start()
