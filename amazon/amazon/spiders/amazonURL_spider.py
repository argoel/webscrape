from scrapy.spider import Spider
from amazon.items import AmazonItem

class AmazonSpider(Spider):
  name = 'amazonURL'
  allowed_domains = ["amazon.com"]
  base_url = "http://www.amazon.com/dp/"
  start_urls = []
  with open('shoesAsins', 'r') as f:
    for line in f:
      start_urls.append(base_url+line[:-1])

  def parse(self, response):
    print "Parsing response"
    
    item = AmazonItem()
    ppd = response.xpath('//div[@id="ppd"]')
    leftCol = ppd.xpath('//div[@id="leftCol"]')

    #altImages is the list of thumb images of product
    altImages = leftCol.xpath('//div[@id="altImages"]//li//img/@src').extract()
    item['altImages']=[]
    for img in altImages:
      item['altImages'].append(img)

    centerCol = ppd.xpath('//div[@id="centerCol"]')

    #productTitle is title of product
    productTitle = centerCol.xpath('//span[@id="productTitle"]/text()').extract()[0]
    item['productTitle'] = productTitle

    avgCustomerReviews = centerCol.xpath('//span[@class="reviewCountTextLinkedHistogram noUnderline"]/@title').extract()[0]
    item['avgCustomerReviews']=avgCustomerReviews

    numberOfReviews = centerCol.xpath('//span[@id="acrCustomerReviewText"]/text()').extract()[0]
    item['numberOfCustomerReviews']=numberOfReviews
    
    try:
      strikePrice = centerCol.xpath('//div[@id="price"]//td[@class="a-span12 a-color-secondary a-size-base a-text-strike"]/text()').extract()[0]
      item['strikePrice'] = strikePrice
      salePrice = centerCol.xpath('//span[@id="priceblock_saleprice"]/text()').extract()[0]
      item['salePrice'] = salePrice
      salePriceShippingMess = centerCol.xpath('//span[@id="saleprice_shippingmessage"]/span/text()').extract()[0]
      item['salePriceShippingMess'] = salePriceShippingMess
    except:
      print "This item is not for sale"
    
    try:
      ourPrice = centerCol.xpath('//span[@id="priceblock_ourprice"]/text()').extract()[0]
      item['ourPrice'] = ourPrice

      ourPriceShippingMess = centerCol.xpath('//span[@id="ourprice_shippingmessage"]/span/text()').extract()[0]
      item['ourPriceShippingMess'] = ourPriceShippingMess
    except:
      print "This item is on sale"

    try:
      twister = centerCol.xpath('//form[@id="twister"]')

      options = twister.xpath('//select[@name="dropdown_selected_size_name"]/option/text()').extract()

      sizeOptions = options[1:]
      item['sizeOptions'] = []
      for size in sizeOptions:
        item['sizeOptions'].append(size.strip())

      colorOptions = twister.xpath('//div[@id="variation_color_name"]//li//img/@alt').extract()
       
      colorOptionImgSrc = twister.xpath('//div[@id="variation_color_name"]//li//img/@src').extract()

      colorVariations = twister.xpath('//div[@id="variation_color_name"]//li//img')
      item['colorOptions'] = []
      for colorV in colorVariations:
        color = colorV.xpath('@alt').extract()[0]
        src = colorV.xpath('@src').extract()[0]
        colorD = {}
        colorD[color] = src
        item['colorOptions'].append(colorD)
    except:
      print "Some options in twister failed"

    features = centerCol.xpath('//div[@id="feature-bullets"]//li//text()').extract()
    item['productFeatures'] = []
    for feature in features:
      item['productFeatures'].append(feature)

    rightCol = ppd.xpath('//div[@id="rightCol"]')

    dnd = response.xpath('//div[@id="descriptionAndDetails"]')

    pnd = dnd.xpath('//div[@id="productDescription"]/p/text()').extract()[0]
    item['productDesc'] = pnd

    detb = dnd.xpath('//div[@id="detailBullets"]')
    salesRank = detb.xpath('//li[@id="SalesRank"]/text()').extract()[1]
    item['salesRank'] = salesRank

    yield item
