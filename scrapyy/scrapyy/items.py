# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from emails.models import Email

class EmailItem(DjangoItem):
    django_model = Email

class ScrapyyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass