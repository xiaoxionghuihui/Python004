# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from maoyanfilmsproxy.items import MaoyanfilmsproxyItem
import pymysql

#modified by xiongli，Date:20201020
#Note:修改MaoyanfilmsproxyPipeline类，增加连接数据库并写入的操作
class MaoyanfilmsproxyPipeline:
    def __init__(self):   
        self.conn = pymysql.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'xiongli',
            db = 'xiongli2020',
            charset ='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        filmname = item['filmname']
        filmtime = item['filmtime']
        filmtype = item['filmtype']
        output = f"|{filmname}|\t|{filmtype}|\t|{filmtime}|\n\n"
        with open('./maoyan_scrapy.txt','a+',encoding='utf8') as f:
            f.write(output)
        #连接数据库，并导入到数据库     
        sqls = "INSERT INTO filmlist(filmname,filmtype,filmtime) VALUES (%s,%s,%s)"

        try:
            self.cur.execute(sqls,(item['filmname'],item['filmtype'],item['filmtime']))
            self.conn.commit()
        except:
            self.conn.rollback()
            print('写入数据库出错!')
        return item
    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()