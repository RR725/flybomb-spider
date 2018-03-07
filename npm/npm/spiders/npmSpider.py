import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from npm.items import NpmItem
import urllib


class Jianshu(CrawlSpider):
    name = 'npm'
    start_urls = ['https://www.jianshu.com/trending/monthly']
    url = 'https://www.jianshu.com'

    def parse(self, response):
        item = NpmItem()
        selector = Selector(response)
        articles = selector.css('.note-list li')

        for article in articles:
            title = article.css('.title').xpath('text()').extract()
            url = article.css('.title').xpath('@href').extract()
            author = article.css('.nickname').xpath('text()').extract()

            # 下载所有热门文章的缩略图, 注意有些文章没有图片
            try:
                image = article.css('a img').xpath('@src').extract()

                urllib.urlretrieve('https:' + image[0],
                                   '/Users/meizu/Documents/images/%s-%d.jpg' %
                                   (author[0], title[0]))
            except:
                print('--no---image--')

            item['title'] = title
            item['url'] = self.url + url[0]
            item['author'] = author

            yield item

        next_link = selector.xpath(
            '//*[@id="list-container"]/div/button/@data-url').extract()

        if len(next_link) == 1:

            next_link = self.url + str(next_link[0])
            print("----" + next_link)
            yield Request(next_link, callback=self.parse)
