#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Spider module for crawling alibi.com
"""
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from activitiesin.items import ActivitiesinItem
import sys

class AlibiSpider(BaseSpider):
    """
    Spider for crawling alibi.com
    """
    name = "alibi"
    allowed_domains = ["alibi.com"]
    start_urls = [
        "http://alibi.com/events/searchresult.html?com=searchresult&t=2", #music
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=8", # word
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=7", # art
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=9", # stage
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=18", # stage
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=11", # song and dance
        #"http://alibi.com/events/searchresult.html?com=searchresult&t=4" # community
    ]

    def parse(self, response):
        """
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['desc'] = site.select('text()').extract()
            items.append(item)
        """
        hxs = HtmlXPathSelector(response)
        searchresults = hxs.select('//section[@id="searchresult"]')
        dates = searchresults.select('.//header[@class=\
                "eventdates"]/text()').extract()
        events = searchresults.select('.//ul[@class="events"]')
        items = []
        category = events[0].select('.//a[@itemprop="eventType"]/text()')\
                .extract()[0]
        for i in xrange(len(dates)):
            current_venue = -1
            venue = ""
            for event in events[i].select("li"):
                location = event.select('.//div/text()').extract()

                try:
                    item = ActivitiesinItem()
                    if len(location):
                        venue = location[0]
                    info = event.select('a[@class="summary"]/text()')\
                            .extract()[0].split(u'•')
                    item['activity'] = info[0]
                    item['location'] = venue
                    item['date'] = dates[i]

                    item['time'] = event.select('.//abbr[\
                            @class="value"]/text()').extract()

                    item['time'] = item['time'][0]

                    item['link'] = ""
                    item['category'] = category

                    if len(info) > 1:
                        item['description'] = info[1]
                    else:
                        item['description'] = ''

                    items.append(item)
                except:
                    pass

        return items
        """
        category = ""
        for evts in events.select('.//div[@class="event_category"]/ \
                        ul/li/a[@itemprop="eventType"]/text()') \
                        .extract():
            print evts
        """
        # Steps
        # 1. Grab a link to the category
        # 2. visit that link
        # 3. parse that link and store all items

