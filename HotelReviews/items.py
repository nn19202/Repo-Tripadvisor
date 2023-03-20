# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HotelreviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    h_url = scrapy.Field()
    h_reviewer_name = scrapy.Field()
    #h_reviewer_id = scrapy.Field()
    h_comment_date = scrapy.Field()
    h_rating = scrapy.Field()
    h_title_comment = scrapy.Field()
    h_content_comment = scrapy.Field()
    h_reviewer_staydate = scrapy.Field()
    h_trip_type = scrapy.Field()

    pass
