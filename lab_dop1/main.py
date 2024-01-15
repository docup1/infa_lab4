from json2xml import json2xml
from json2xml.utils import readfromstring
from time_counter import start, end, count


t1 = start()

for i in range(100):

    with open("data/index.json", "rb") as json_file:
        data = readfromstring(json_file.read().decode())

    with open("data/index.xml", "w", encoding = 'UTF-8') as xml_file:
        xml_file.write(json2xml.Json2xml(data, wrapper="root", attr_type = False, item_wrap = True, pretty = True).to_xml())

t2 = end()

count(t1, t2)



