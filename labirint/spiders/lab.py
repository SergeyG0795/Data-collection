import scrapy
from scrapy.http import HtmlResponse

from labirint.items import LabirintItem


class LabSpider(scrapy.Spider):
    name = "lab"
    allowed_domain = ['labirint.ru']
    start_urls = ["https://labirint.ru/books"]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath('//a[@class="pagination-next__text"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath("//a[@class='product-title-link']/@href").getall()

        for link in links:
            yield response.follow(link, callback=self.book_parse)

    def book_parse(self, response: HtmlResponse):
        name = response.xpath('//div[@class="prodtitle"]//h1//text()').get()
        price = response.xpath('//span[@class="buying-priceold-val-number"]//text()').get()
        discount_price = response.xpath('//span[@class="buying-pricenew-val-number"]//text()').get()
        author = response.xpath('//div[@class="authors"]//a[1]//text()').get()
        rate = response.xpath('//div[@id="rate"]//text()').get()

        yield LabirintItem(name=name, price=price, discount_price=discount_price, author=author, rate=rate)
