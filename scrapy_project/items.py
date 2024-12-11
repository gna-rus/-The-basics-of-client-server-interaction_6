# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# Модуль Items.py Нужен для упаковки данных
import scrapy

# обработчики для лоадеров (каждый обработчик или ПРЕобработчик или ПОСТобработчик)
from itemloaders.processors import TakeFirst, MapCompose, Compose


def correct_text_strip(value):
    value = value.strip()
    return value

def correct_text_del_word(value):
    value = value[1:]
    return value

def correct_url(value:str):
    print()
    return value.split(" ")[0]

class JobparserItem(scrapy.Item):
    # define the fields for your item here like:
    # output_processor=TakeFirst()
    commit = scrapy.Field(input_processor=MapCompose(correct_text_strip)) # Обьявляю поля которые надо вытянуть из Паука (смотри hhru, эти переменные есть там)
    author = scrapy.Field()
    loggin_of_author = scrapy.Field(input_processor=MapCompose(correct_text_del_word), output_processor=TakeFirst())
    Published_datatime = scrapy.Field(output_processor=TakeFirst())
    url_img = scrapy.Field(input_processor=MapCompose(correct_url), output_processor=TakeFirst())
    print()




