# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Модуль Items.py Нужен для упаковки данных
import scrapy

class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    commit = scrapy.Field() # Обьявляю поля которые надо вытянуть из Паука (смотри hhru, эти переменные есть там)
    author = scrapy.Field()
    loggin_of_author = scrapy.Field()
    Published_datatime = scrapy.Field()
    url_img = scrapy.Field()


