import scrapy
from myscrapy.items import englishItem


class EnglishSpider(scrapy.Spider):
    name = 'english'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = ['http://language.chinadaily.com.cn/thelatest/page_{}.html'.format(page) for page in range(0, 348)]

    def parse(self, response):
        divs = response.xpath('//div[@class="gy_box"]')

        for div in divs:
            title = div.xpath('./div/p[1]/a/text()').get()
            url = div.xpath('./div/p[1]/a/@href').get()
            description = div.xpath('./div/p[2]/a/text()').get()
            img_url = div.xpath('./a/img/@src').get()

            item = englishItem(title=title, url=url, description=description, img_url=img_url)
            yield item
