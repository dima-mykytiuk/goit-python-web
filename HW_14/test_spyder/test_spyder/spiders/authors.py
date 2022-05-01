from test_spyder.models import Tag, Quote, Biography, db_session
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            quote_to_db = Quote(author=''.join(quote.xpath("span/small/text()").extract()),
                                quote=quote.xpath("span[@class='text']/text()").get().replace('”', '').replace('“', ''),
                                link=self.start_urls[0] + quote.xpath("span/a/@href").get())
            quote_to_db.tags = [Tag(name=tag) for tag in quote.xpath("div[@class='tags']/a/text()").extract()]
            db_session.add(quote_to_db)
            db_session.commit()
        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)
