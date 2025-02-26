# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
import datetime
import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst,Join # 将我们的值 对他做两次处理

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # items 类似字典的作用，但是比字典强
    pass


def add_jobbole(value):
    return value+ "-jobbole"


def date_convert(value):
    try:
        create_data = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_data = datetime.datetime.now().date()

    return create_data

def get_nums(value):
    import re
    match_re = re.match(".*?(\d+).*",value)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def remove_comment_tags(value):
    # 去掉tag中提取得评论
    if "评论" in value:
        return ""
    else:
        return value

def return_value(value):
    return value


class ArticleItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(lambda x:x+"-jobbole")  # 加上字段
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),  # 加上字段
        # output_processor=TakeFirst() # 取第一个
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field(  # 这有个点，需要注意
        output_processor=MapCompose(return_value)

    )
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)  #
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field(
        input_processor=MapCompose(remove_comment_tags),
        output_processor=Join(",")
    )
    content = scrapy.Field()


class ZhihuQuestionItem(scrapy.Item):
    # 知乎的问题item
    zhihu_id = scrapy.Field()
    topics =  scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    watch_user_num = scrapy.Field()
    click_num = scrapy.Field()
    crawl_time = scrapy.Field()

class ZhihuAnswerItem(scrapy.Item):
    #处理知乎的问题回答item
    zhihu_id = scrapy.Field()
    url = scrapy.Field()
    question_id = scrapy.Field()
    content = scrapy.Field()
    parise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()