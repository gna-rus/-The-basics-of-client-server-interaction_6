# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.images import FilesPipeline
from pprint import pprint

import json
import requests


class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        return item# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# Модуль pipelines.py принимает упакованные данные из items.py и проводит фиксацию данных (отправляет данные куда либо или загружает данные в файл)

from pymongo import MongoClient

class JobparserPipeline:
    # def __init__(self):
    #     client = MongoClient('localhost', 27017) # Инициализирую подключение к БД
    #     self.mongo_base = client.items05122024 # создаю БД в Манго


    def process_item(self, item, spider):
        print(item)

        # dict1 = {}
        # dict1[item['Published_datatime']] = [item['author'],item['commit'], item['loggin_of_author'], item['image_urls']]
        #
        # # Добавляю данные в json
        # with open('result.json', 'a', encoding='utf-8') as file:
        #     json.dump(dict1, file, ensure_ascii=False, indent=4)
        #     file.write(',\n')
        #
        # return item

class ImagePipeLineRes(FilesPipeline):
    def get_media_requests(self, item, info):
        url = item['image_urls'][0]
        print(type(url), url)
        try:
            yield scrapy.Request(url)
        except Exception as err:
            print(err)
        print()

    def item_completed(self, results, item, info):
        pprint(results)
        return item
# class ImagePipeLineRes:
#     def process_item(self, item, spider):
#         print('ImagePipeLineRes', item['image_urls'])
#         adres = item['image_urls'][0]
#         response = requests.get(adres)
#         path = 'D:\python\pythonProject\GitHub\-The-basics-of-client-server-interaction_6\image'
#         with open(f'{path}.jpg', 'wb') as f:
#             f.write(response.content)
