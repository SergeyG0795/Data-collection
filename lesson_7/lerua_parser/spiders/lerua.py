import scrapy
from scrapy.http import HtmlResponse

from scrapy.loader import ItemLoader

from lerua_parser.items import LeruaParserItem


class LeruaSpider(scrapy.Spider):
    name = "lerua"
    allowed_domain = ['https://kazan.leroymerlin.ru/']

    def __init__(self, search, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://kazan.leroymerlin.ru/catalogue/elektroinstrumenty/"]
        # self.start_urls = [f"https://kazan.leroymerlin.ru/search/?q={search}"]

    def parse(self, response: HtmlResponse):

        next_page = response.xpath('//a[@data-qa-pagination-item="right"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        links = response.xpath('//a[@data-qa="product-name"]/@href').getall()

        for link in links:
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response: HtmlResponse):
        loader = ItemLoader(item=LeruaParserItem())
        loader.add_xpath('name', '//h1[@itemprop="name"]/span//text()')
        loader.add_xpath('price', '//span[@slot="price"]//text()')
        loader.add_xpath('url', response.url)
        loader.add_xpath('photos', '//picture[@slot="pictures"]/@src')

        yield loader.load_item()
