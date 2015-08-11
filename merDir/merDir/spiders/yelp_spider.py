from scrapy.spider import Spider

f = open('yelpURLs', 'w')
searchPin = '94305'

class YelpSpider(Spider):
  name = 'yelp'
  allowed_domains = ["yelp.com"]
  base_url = "http://www.yelp.com/search?find_loc={0}&ns=1&start=".format(searchPin)
  start_urls = []
  for k in range(100):
    start = k*10
    url = base_url + str(start)
    print url
    start_urls.append(url)

  def parse(self, response):
    print "Parsing response"
    ibiz = response.xpath('//div[@class="biz-listing-large"]//span[@class="indexed-biz-name"]/a/@href').extract()
    for biz in ibiz:
      f.write(biz+'\n')

