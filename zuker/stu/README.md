记录学习scrapy的配置环境信息
用到的版本控制服务是 Anaconda
环境 ：
技术语言 python3.5
框架 scrapy1.3 elasticsearch5
框架 django1.11 redis
开发系统 windows/ linux / mac
数据库 mysql5.6 redis
IDE pycharm
工具 virtualenv datagrip
python版本工具 Anaconda

Anaconda下的python3.5.4的名称 python35_scrapy
存放位置在 /Users/lee/anaconda3/envs/python35_scrapy/bin/python3.5
创建指定版本的py 例如chuangjianpy3.5版本 起名叫 py35
> conda create --name py35 python=3.5

如何使用

To activate this environment, use:

> source activate scrapy__py35

To deactivate an active environment, use:

> source deactivate

如何安包
安装 virtualenv
> conda install virtualenv

查看 已经安装的包列表
> conda list

查看 指定环境下的py包
> conda list -n py名字
例如 conda list -n python35_scrapy

安装virtualenv virtualenvwrapper
> conda install virtualenv virtualenvwrapper

安装python3.5的虚拟环境的虚拟环境 命名为 article_spider

> mkvirtualenv --python=/Users/lee/anaconda3/envs/python35_scrapy/bin/python3.5 article_spider

查看虚拟环境和使用
> 创建爬虫
 cd  /Users/lee/PycharmProjects/chanjet_git/lee_codes/zuker/stu/article/
 scrapy startproject ArticleSpider
 cd ArticleSpider/
 scrapy genspider jobbole blog.jobbole.com






