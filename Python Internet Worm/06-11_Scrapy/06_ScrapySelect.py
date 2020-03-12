# Python 3.6.5

import scrapy

f = open("06_EG_superHero.xml")
body = f.read()
f.close()

print("> Body : \n{}".format(body))

# Xpath select
print("\n   >>> Xpath Selection <<<")
print("> Select all :")
print(scrapy.selector.Selector(text = body).xpath("/*").extract())
print("> Select first class:")
print(scrapy.selector.Selector(text = body).xpath("/html/body/superhero/class[1]").extract())
print("> Select last class:")
print(scrapy.selector.Selector(text = body).xpath("/html/body/superhero/class[last()]").extract())
print(">        last class name text:")
print(scrapy.selector.Selector(text = body).xpath("/html/body/superhero/class[last()]/name/text()").extract())
print("> Select name is \"en\":")
print(scrapy.selector.Selector(text = body).xpath("//name[@lang='en']").extract())

# Css select
print("\n   >>> Css Selection <<<")
print("> Select all class:")
print(scrapy.selector.Selector(text = body).css('class').extract())
print("> Select all class name")
print(scrapy.selector.Selector(text = body).css('class name').extract())
print("> Select 1-st class name")
print(scrapy.selector.Selector(text = body).css('class name').extract()[0])
print("> Select name is \"en\":")
print(scrapy.selector.Selector(text = body).css('[lang="en"]').extract())

'''
f = open("1.txt")
body = f.read()
f.close()
print(scrapy.selector.Selector(text = body).xpath('//td[@colspan="2"]/text()').extract())
'''