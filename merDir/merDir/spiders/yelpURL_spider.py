from scrapy.spider import Spider

fw = open('yelpDir', 'w')

def getStrStrip(elist):
  if(elist):
    return str(elist[0].encode('utf8')).strip()
  else:
    return ''

class YelpSpider(Spider):
  name = 'yelpURL'
  allowed_domains = ["yelp.com"]
  base_url = "http://www.yelp.com"
  start_urls = []
  with open('yelpURLs', 'r') as f:
    for line in f:
      start_urls.append(base_url+line[:-1])
      print line

  def parse(self, response):
    print "Parsing response"
    name = getStrStrip(response.xpath('//div[@class="biz-page-header-left"]/h1[@itemprop="name"]/text()').extract())
    print name
    addr = response.xpath('//div[@class="mapbox-text"]/ul/li[@class="address"]//address/span/text()').extract()
    address = ''
    for ad in addr:
      ads = str(ad.encode('utf8')).strip()
      address = address + ads + ' '
    phone = getStrStrip(response.xpath('//div[@class="mapbox-text"]/ul/li//span[@class="biz-phone"]/text()').extract())
    
    web = getStrStrip(response.xpath('//div[@class="mapbox-text"]/ul/li//div[@class="biz-website"]/a/text()').extract())
    
    writeLn = name + ',' +  address + ',' +  phone + ',' +  web
    fw.write(writeLn+'\n')

