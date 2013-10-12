# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ActivitiesinItem(Item):
    activity = Field()
    location = Field()
    date = Field()
    time = Field()
    link = Field()
    category = Field()
    description = Field()
