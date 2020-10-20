Week02 学习笔记
=异常===
1.异常捕获过程：
（1）异常类把错误消息打包到一个对象
（2）该对象会自动查找调用栈
（3）知道运行系统找到明确声明如何处理这些类异常的位置
2.所有异常继承至BaseException类
3.isdigit()方法检测字符串是否只由数字组成
4.自定义异常，就是需将新异常定义为一个类，通过实例化可以调用类定义方法
5.自定义异常类，必须继承自Exception类
6.Python中使用__XXX__格式的函数都有特殊功能，因此叫“魔法方法”
7.__str__需返回一个字符串，当所属类被实例化后，可直接将实例对象当成一个字符串，
即print(对象)，相当于print(a string)
8.with语句必须包含一个__enter__()和__exit__()
出现with语句，就会调用__enter__()，该党发调用完成，就开始执行with其他语句，执行中若遇到错误，则其后的代码将不回再继续执行，而要开始执行__exit__()
__exit__(self,exc_type,exc_val,exc_tb)三个参数分别表示异常类型、异常值、追溯信息
9.在类中实现__call__()函数，则该类可像函数方法一样被调用，相当于重载了括号运算符=pymysql===
1.python链接mysql数据库的步骤：
（1）创建connection-创建游标-连接成功-关闭游标-关闭connection
=cookies验证===
1.HTTP常用方法 GET查询/POST提交表单
2.requests.session()对象可保持多个会话之间的cookie，以使用相同cookie
3.使用fake_useragent模块，可模拟多个浏览器发起请求
=Webdriver模拟浏览器行为===
1.当页面中目标元素被加密显示，导致不易获取时，可通过webdriver控制浏览器软件访问的方式模拟用户操作，但该操作的效率相对要低一些。
2.webdriver是属于selenium模块，需安装selenium:
(1)pip3 install selenium
(2)根据chrome版本号下载chromedriver驱动，解压后放置于python解释器执行目录下，同时也要放置于chrome安装根目录下，若是mac，则是访达-应用程序-选中chrome土表右键查看包内容，该路径下
（3）需设置chrome的安装目录到mac的系统$PATH目录下，修改方法：
echo $PATH
sudo -vi ~.bash_profile (必须sudo,否则无权限修改)
=设置虚拟代理===
1.执行命令：scrapy crawl 爬虫名 --nolog  则将不打印scrapy的执行日志，而只输出执行结果
2.scrapy默认支持系统代理自动导入，即在系统PATH中设置代理ip,scrapy框架可自动导入.操作步骤如下:
(1)export http_proxy='http://ip:port'
ip-代理ip
port-代理端口
http_proxy参数固定，若写错，系统将无法读取
（2）settings.py中打开下载中间件scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
3.GitHub上有很多用户提供了免费代理ip
4.设置代理ip的目的是伪装真实访问ip,避免被服务器识别为爬虫程序后，ip被禁
=设置随机代理ip===
1.若需要设置多个随机的代理，并让request每次访问时，随机选择代理执行访问，则需要修改middlerwares.py 和 settings.py文件
（1）middlewares.py中主要为了实现读取代理-处理代理-设置代理功能，可通过继承系统原有类scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware类，并重写其中的方法__init__(self,auth_encoding='utf-8',proxy_list=None)、from_crawler(cls,crawler)、_set_proxy(self,request,scheme)
（2）settings.py中主要为了增加新编写的类，并进行调用。已经增加代理列表，settings.py中的参数必须是全大写格式，因python中调用settings.py中的参数不支持小写格式。

=做作业时遇到的问题===
1.重新新建了一个project,并创建了spider后，将在week01中的作业修改并复制到新的爬虫文件中，调整完成各类的名称后，执行时报：DEBUG: Rule at line 171 without any user agent to enforce it on.
检查发现是因为settings.py中的USER_AGENT = 'maoyanfilmsproxy (+http://www.yourdomain.com)'的注释符未打开，将注释符去掉后解决

