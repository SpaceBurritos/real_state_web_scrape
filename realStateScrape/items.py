# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RealstatescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    #location = scrapy.Field()
    id = scrapy.Field()
    status = scrapy.Field()
    loc_type = scrapy.Field()
    view_type = scrapy.Field()
    total_lot_size = scrapy.Field()
    lot_living = scrapy.Field()
    num_bedrooms = scrapy.Field()
    num_full_bath = scrapy.Field()
    stories = scrapy.Field()
    floor_type = scrapy.Field()
    construction_status = scrapy.Field()
    year = scrapy.Field()
    has_aircon = scrapy.Field()
    furnished_type = scrapy.Field()
    pool_type = scrapy.Field()
    has_jacuzzi = scrapy.Field()
    parking_type = scrapy.Field()
    has_internet = scrapy.Field()
    has_television = scrapy.Field()
    country = scrapy.Field()
    state = scrapy.Field()
    county = scrapy.Field()
    district = scrapy.Field()
    city = scrapy.Field()
    price_ac_area = scrapy.Field()
    price_sq_m = scrapy.Field()
    pass
