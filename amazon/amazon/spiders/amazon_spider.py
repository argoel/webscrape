from scrapy.spider import Spider

f = open('amazonURLs', 'w')

class AmazonSpider(Spider):
  name = 'amazon'
  allowed_domains = ["amazon.com"]
  base_url = "http://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aon&rh=k%3Ashoes%2Cn%3A7141123011&page={0}&keywords=shoes&ie=UTF8&qid=1441335866&spIA=B00SDPCKPW,B0146J3JDA,B00UZVNHDQ,B00UZVSY48"
  start_urls = []
  for k in range(400):
    url = base_url.format(k)
    print url
    start_urls.append(url)

  def parse(self, response):
    print "Parsing response"
    asins = response.xpath('//@data-asin').extract()
    for asin in asins:
      f.write(asin+'\n')
