# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Модуль Items.py Нужен для упаковки данных
import scrapy

# обработчики для лоадеров (каждый обработчик или ПРЕобработчик или ПОСТобработчик)
from itemloaders.processors import TakeFirst, MapCompose, Compose


def correct_text(value):
    value = value.strip()
    return value

class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    # output_processor=TakeFirst()
    commit = scrapy.Field(input_processor=MapCompose(correct_text)) # Обьявляю поля которые надо вытянуть из Паука (смотри hhru, эти переменные есть там)
    author = scrapy.Field(output_processor=TakeFirst())
    loggin_of_author = scrapy.Field(output_processor=TakeFirst())
    Published_datatime = scrapy.Field(output_processor=TakeFirst())
    url_img = scrapy.Field(output_processor=TakeFirst())
    print(commit)
    print()



