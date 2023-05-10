from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from labirint import settings
from labirint.spiders.lab import LabSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LabSpider)
    process.start()

