import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Сбор ссылок на PEP из индекса"""
        numerical_index = response.xpath("//section[@id='numerical-index']")
        tbody = numerical_index.css("tbody")
        links = tbody.css("a::attr(href)").getall()
        for link in links:
            str.join(link, '/')
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'h1.page-title::text'
        ).get().split(' – ', 1)

        data = {
            'number': number.replace('PEP ', ''),
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }

        yield PepParseItem(data)
