
Week01 学习笔记

1.Xpath所查找的目标标签是某个节点下的子节点，且需获取所有目标标签的text时，可通过在节点Xpath后添加双斜杠的方式查找到其下所有相同标签的子节点.如本期作业中，要查找的电影类型：
#电影类型
    film_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]//a/text()')

2.练习了GitHub的常用用法，Python的requests、BeautifulSoup、pandas、lxml库中的常用方法

3.练习了scrapy抓取猫眼电影首页10部电影名称、类型、上映时间，对scrapy的基本结构有了一定掌握：
（1）文件层级结构：爬虫项目名称/爬虫名称/spiders
    spiders中存放爬虫逻辑文件（爬虫名.py）
（2）爬虫名称文件下，包含爬虫各组成部分的文件：settings.py(配置文件)、items.py(x爬虫要抓取的数据项）、pipelines.py(管道文件，配置需写入文件的字段及导出形式)
（3）由于我按老师讲解视频创建的项目spiders，导致有点分不清各个目录与项目名称的对应关系，因此最后以后创建项目名称时不要使用spiders,而使用有意义的名称

4.scrapy编写完成后，在终端执行【scrapy crawl 爬虫名】命令，始终不能导出文件，通过查阅网络得知，需要修改配置settings.py，去掉注释符ITEM_PIPELINES = {
   'testspider.pipelines.TestspiderPipeline': 300,
}，并将其中的testspider调整为使用中的爬虫项目名

5.find查询的结果是单个值，find_all查询出的结果是列表，在赋值时不能讲列表赋值给非列表变量。

6.在写入文件时发现始终只写最后一个链接的值，发现是因为没有使用“追加”模式，导致每次都更新文件

7.使用for i in list: 取出的是列表中的每一项值。  使用for i in range(len(list)):,取出的i是，list的下角标，由于对python的使用还不熟悉，导致这里容易出错。

8.Week01由于一直在学习python的基础语法，导致进度没跟上，目前对python基础语法仍不h熟悉，但比之前好一些了，学习效率会相对提高
