import scrapy
from scrapy.http import HtmlResponse
from labirint_parser.labirint.items import LabirintItem


class LabSpider(scrapy.Spider):
    name = "lab"
    allowed_domains = ["labirint_parser.ru"]
    start_urls = ["https://labirint.ru/books"]

    def parse(self, response: HtmlResponse):
        next_page = response.css('a.pagination-next__text::attr(href)').extract_first()
        yield response.follow(next_page, callback=self.parse)

        books = response.css('div.product').extract()
        for link in books:
            yield response.follow(link, callback=self.book_parse)

    def book_parse(self, responce: HtmlResponse):
        name = responce.css('div.product-title-link span.product-title::text').extract_first()
        price = responce.css('div.price span.price-val::text').extract_first()
        discount_price = responce.css('div.price span.price-old::text').extract_first()
        author = responce.css('div.product-author span::text').extract_first()
        yield LabirintItem(name=name, price=price, discount_price=discount_price, author=author)
