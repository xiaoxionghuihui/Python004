"""需求：
（1）爬取猫眼电影的前10个电影名称、电影类型和上映时间，
（2）以UTF-8字符集保存到CSV格式的文件中"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import lxml.etree

#目标url
myurl = 'https://maoyan.com/films'
#构造http请求的headers:User-Agent/Cookie
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
           'Cookie':'__mta=256825268.1601628181864.1602567036573.1602567526564.18; uuid_n_v=v1; uuid=4637F650048B11EBA834BBA9FFFEB0168E44FA9B8BAA4597B37F8EBACF13E42C; _lxsdk_cuid=174e87a93ffc8-0aacd061ee4402-31697305-fa000-174e87a9400c8; _lxsdk=4637F650048B11EBA834BBA9FFFEB0168E44FA9B8BAA4597B37F8EBACF13E42C; _csrf=32e8419a563bae62469e30af070fcfeea3d40c4b17418f0f8dc789b7c2d58632; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601628181,1602557005; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1602567531; __mta=256825268.1601628181864.1602567526564.1602567530838.19; _lxsdk_s=17520704f4c-423-8e2-9a0%7C%7C8'}
#通过requests.get方法访问目标url，并保存在变量response变量中
response = requests.get(myurl,headers=headers)
print(f'Status_code is: {response.status_code}')
#BeautifuleSoup解析上一步返回的网页内容为BeautifulSoup对象
soup = bs(response.text,'html.parser')

#（1）取前10部电影链接，并存入列表中
#存放前10个电影链接
filmhrefs = [] 
#找到存放电影链接的html块，并存放在列表中，便于取前10个数据
ftags = soup.find_all('div',attrs={'class':'channel-detail movie-item-title'})
#列表切片取前10个数据
for tags in ftags[0:10]:
    for htag in tags.find_all('a',):
        #拼接取电影链接，并存入列表
        filmhrefs.append(f"https://maoyan.com{htag.get('href')}")
print(len(filmhrefs))

#（2）通过链接进入详情页，并获取电影类型/上映时间
for href in filmhrefs:
    filmdetail = requests.get(url=href,headers=headers)
    selector = lxml.etree.HTML(filmdetail.text)
    #电影名称
    film_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
    #电影类型
    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]//a/text()')
    #上映时间
    film_time = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
    film_list = [film_name,film_type,film_time]
    #print(film_list)测试是否能正常获取
    film_pd = pd.DataFrame(data = film_list)

    film_pd.to_csv('./maoyan_filmlist.csv',encoding='utf8',index=False,header=False,mode='a')
