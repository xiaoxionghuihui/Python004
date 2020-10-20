import scrapy
from bs4 import BeautifulSoup
from maoyanfilmsproxy.items import MaoyanfilmsproxyItem


class MyfproxiesSpider(scrapy.Spider):
    name = 'myfproxies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']

    # def parse(self, response):
    #     pass
    #（1）访问电影列表页
    def start_requests(self):
            url = 'https://maoyan.com/films'
            yield scrapy.Request(url=url,callback=self.parse)

    #（2）爬取电影链接
    def parse(self,response):
        # items = []
        soup = BeautifulSoup(response.text,'html.parser')
        href_list = soup.find_all('div',attrs={'class':'channel-detail movie-item-title'})
        for i in href_list[0:10]:
            item = MaoyanfilmsproxyItem()
            filmhref = f"https://maoyan.com{i.find('a').get('href')}"

            item['filmhref'] = filmhref
            # items.append(item)
            yield scrapy.Request(url=filmhref,meta={'item':item},callback=self.parse2)
    
    #（2）详情页获取目标内容
    def parse2(self,response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text,'html.parser')
        #电影名称
        filmname = soup.find('h1',attrs ='name').text
        item['filmname'] = filmname
        #上映时间
        timetemp = soup.find_all('li',attrs ='ellipsis')
        filmtime = timetemp[2].get_text()
        item['filmtime'] = filmtime
        #电影类型
        type_list = soup.find_all('a',attrs ='text-link')
        type_text=[]
        for i in range(len(type_list)):
            type_text.append(type_list[i].get_text())
        filmtype = ''.join(type_text)
        item['filmtype'] = filmtype
        yield item
        