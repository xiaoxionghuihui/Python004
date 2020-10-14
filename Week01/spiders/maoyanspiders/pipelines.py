# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanspidersPipeline:
    def process_item(self, item, spider):
        filmname = item['filmname']
        filmtime = item['filmtime']
        filmtype = item['filmtype']
        output = f"|{filmname}|\t|{filmtype}|\t|{filmtime}|\n\n"
        with open('./maoyan_scrapy.txt','a+',encoding='utf8') as f:
            f.write(output)
        return item
