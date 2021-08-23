import os
import sys

from django.core.management.base import BaseCommand
from scrapy import cmdline


class Command(BaseCommand):
    def handle(self, *args, **options):
        sys.path.insert(0, 'C:/Users/FacilOrdi/Desktop/scraping/scrapyy')
        os.environ['SCRAPY_SETTINGS_MODULE'] = 'scrapyy.scrapyy.settings'
        cmdline.execute("scrapy crawl basic".split())