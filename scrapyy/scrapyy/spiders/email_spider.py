from scrapyy.scrapyy.items import EmailItem
import scrapy 
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
import re
import pandas as pd
from scrapy.crawler import CrawlerProcess

from urllib.parse import urlparse

class firstSpider(scrapy.Spider): 
    name = "basic"
    start_urls = []
    custom_settings = {
            'DOWNLOAD_DELAY': 0,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 1
        }
    def _init_(self):

        for ker in ["Ensa+Marrakech","Ensa+Safi","Ensias"]:
            url = 'https://www.google.com/search?q=site:http://ma.linkedin.com/in/+%22gmail%22+%22'
            url=url +ker
            url=url+"%22&start="
            print(url)

            for start in range(0, 30, 10):
                    self.start_urls.append(url + str(start))
    
    def parse(self, response):
        items = []
        print('response url:', response.url)
        df = pd.DataFrame()
        xlink = LinkExtractor()
        
        link_list=[]
        link_text=[]
        divs = response.xpath('//div')
        text_list=[]
        text_list1=[]
        text_list2=[]
        for span in divs.xpath('text()'):
            if len(str(span.get()))>100:
                text_list.append(span.get()) 
                def func(s, pat):
                    pat = r'\b\S*%s\S*\b' % re.escape(pat) 
                    return re.findall(pat, s)
                def listToString(s): 
                    str1 = ""
                    return (str1.join(s))
            
                for i in text_list:
                    text_list1.append(func(i,"gmail"))
                for b in text_list1:
                    k=listToString(b) 
                    item = EmailItem() 
                    item['email'] = k
                    items.append(item)
                    text_list2.append(k)
        print(text_list2)  

        #for link in xlink.extract_links(response):
        #    if  'linkedin' in link.text:
        #        l=str(link)
        #        l1=l[39:150]
        #       l1.split('&')
        #        link_list.append(l1.split('&')[0])
        #        link_text.append(link.text)
        #df['textmeta'] = text_list2
        #df.to_csv('output15.csv', mode='a')
        #df = pd.read_csv(r'output15.csv')
        #df[~df.duplicated(subset=['textmeta'])].to_csv('output(clean2).csv',index=False)
        
        yield items
        

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(firstSpider)
    process.start()