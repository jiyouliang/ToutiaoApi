## Django web 接口开发-提供5000条爬取的今日头条新闻数据


### 1.导入mysql数据

将当前项目toutiao.sql文件，拷贝到服务器。

![](imgs/0.png)

在toutiao.sql同一个目录下，将sql文件导入数据库中，详细执行命令请参考下面截图。该过程根据提示输入mysql密码：

	$ mysql -uroot -p toutiao < toutiao.sql


![](imgs/2.png)


### 2.修改web项目mysql配置

修改/util/mysqlutils.py模块中mysql配置，改成自己的配置：


![](imgs/3.png)


### 3.运行服务器

在ToutiaoApi项目根目录下运行django：

	python manage.py runserver 0.0.0.0:8080

### 4.访问视图

下图对应视图函数：/apps/news_tech/模块中的news_tech()函数

	http://ip:端口/ToutiaoApi/news_tech?page=1

![](imgs/4.png)

### 5.其他说明

当前django暂时只有“科技”频道视图，toutiao.sql默认提供了今日头条10个频道（科技、热点、推荐、体育、军事等）总共5000多条数据，想要显示所有频道数据，请根据需求自行添加app或者view视图函数。

![](imgs/5.png)








