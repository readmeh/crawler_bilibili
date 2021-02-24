import scrapy
from ..items import teacherItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        teachers = response.xpath('//div[@class="li_txt"]')
        for teacher in teachers:
            tname = teacher.xpath("./h3/text()").get()
            trank = teacher.xpath("./h4/text()").get()
            tinfo = teacher.xpath("./p/text()").get()
            timg = 'http://www.itcast.cn{}'.format(teacher.xpath("./../img/@data-original").get())

            item = TeacherItem(tname=tname,trank=trank,tinfo=tinfo,timg=timg)
            yield item