from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lerua_parser import settings
from lerua_parser.spiders.lerua import LeruaSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeruaSpider, search='электроинструмент')
    process.start()
