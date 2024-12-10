# def correct_info(text):
#     list_value = []
#     result = ''
#     for i in text:
#         list_value.append(i.replace(" ", ""))
#     for i in list_value:
#         for j in i:
#             if j in '1234567890Р':
#                 result += j
#
#
#     if result.count('Р') > 1:
#         nomber = result.find('Р')
#         text = '' + result[:nomber+1] +' - ' + result[nomber+1:]
#         result = text
#
#
#
#     return result
#
#
#
# file1 = ['Плоский термопресс Bulros T-300']
# file2 = ['\r\n                ', '\r\n                    520 000                ', '\r\n                ', 'Р', '                ', '\r\n                ', '\r\n                ', '            ']
# print(correct_info(file2))


import json
data = {'cost': '52700 Р',
 'name': ['Плоский термопресс121 Bulros T-201'],
 'url_items': 'https://www.foroffice.ru/products/description/57113.html'}

dict1 = {}
dict1[data['name'][0]] = [data['cost'], data['url_items']]
print(dict1)

with open('result.json', 'a', encoding='utf-8') as file:
    json.dump(dict1, file, ensure_ascii=False, indent=4)
    file.write(',\n')