# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the Fields for your item here like:
    
    #alternate images
    altImages = scrapy.Field()

    #product Title
    productTitle = scrapy.Field()

    #avgCustReviews
    avgCustomerReviews = scrapy.Field()
    
    numberOfCustomerReviews = scrapy.Field()

    #strike price, if product is on sale
    strikePrice = scrapy.Field()

    #sale price, if product is on sale
    salePrice = scrapy.Field()

    #sale price shipping message
    salePriceShippingMess = scrapy.Field()

    #price if product not on sale
    ourPrice = scrapy.Field()
    
    #our price shipping message
    ourPriceShippingMess = scrapy.Field()

    sizeOptions = scrapy.Field()

    colorOptions = scrapy.Field()

    productFeatures = scrapy.Field()

    productDesc = scrapy.Field()

    salesRank = scrapy.Field()
