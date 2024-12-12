# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
import os
from itemadapter import ItemAdapter
from scrapy.pipelines.images import FilesPipeline
import json
from urllib.parse import urlparse
from pathlib import Path
from scrapy.exceptions import DropItem
from pprint import pprint

class ScrapyProjectPipeline:
    def process_item(self, item, spider):
        return item
# Define your item pipelines here
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

        dict1 = {}
        dict1[item['Published_datatime']] = [item['author'],item['commit'], item['loggin_of_author'], item['image_urls']]

        # Добавляю данные в json
        with open('result.json', 'a', encoding='utf-8') as file:
            json.dump(dict1, file, ensure_ascii=False, indent=4)
            file.write(',\n')

        return item

class ImagePipeLineRes(FilesPipeline):
    def get_media_requests(self, item, info):
        url = item['image_urls'][0]
        print(type(url), url)
        try:
            yield scrapy.Request(url)
        except Exception as err:
            print(err)
        print()

    def list_files(self, directory):
        files = os.listdir(directory)
        for file in files:
            print(file)

    def rename_file(self, dir, old_filename, new_filename):
        full_old_filename = dir+"\\"+old_filename
        full_new_filename = dir+"\\"+new_filename+'.jpeg'
        print(full_new_filename)
        print(full_old_filename)
        directory = os.path.dirname(full_old_filename)
        old_filepath = os.path.join(directory, os.path.basename(full_old_filename))
        new_filepath = os.path.join(directory, full_new_filename)
        try:
            os.rename(old_filepath, new_filepath)
            print(f"Файл успешно переименован: '{full_old_filename}' -> '{full_new_filename}'.")
        except FileNotFoundError:
            print(f"Файл '{full_old_filename}' не найден.")
        except OSError as e:
            print(f"Произошла ошибка при переименовании файла: {e}")

    def item_completed(self, results, item, info):
        dir = r'D:\python\pythonScrapy\images\full'
        print(results)
        print('___', results[0][1]['path'][5:])
        self.list_files(dir)
        self.rename_file(dir, results[0][1]['path'][5:], results[0][1]['path'][5:10])
        return item

