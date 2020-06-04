import scrapy
import re
import datetime
from ..items import VersaceItem


class VersaceSpiderSpider(scrapy.Spider):
    name = 'versace_spider'

    def start_requests(self):
        start_urls = ['https://www.versace.com/fr/fr-fr/femmes/',
                      'https://www.versace.com/us/en-us/women/']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse_category)

    def parse_category(self, response):
        product_main_sub_category = response.css("a.level-2-link.category-link ").css("::attr(href)").extract()
        subcategory_list = product_main_sub_category
        for url in subcategory_list[:1]:
            yield scrapy.Request(url=url, callback=self.parse_all_items_links)

    def parse_all_items_links(self, response, all_links=[]):
        product_how = response.css(".results-found-breadcrumb").css("::text").extract()
        amount_of_page = int(re.search(r'[0-9]{1,}', product_how[0])[0]) // 24 + 1
        for i in range(amount_of_page):
            all_links.append(str(response)[5:-1]+'?start='+str(i*24)+'&sz=24&format=page-element')
        for url in all_links:
            yield scrapy.Request(url=url, callback=self.parse_all_items)

    def parse_all_items(self, response, all_items_list=[]):
        product_url = response.css(".name-link").css("::attr(href)").extract()
        for i in product_url:
            new = 'https://www.versace.com'+i
            all_items_list.append(new)
        for url in all_items_list:
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        items = VersaceItem()
        product_name = response.css(".product-name").css("::text").extract()
        product_price = response.css(".js-sl-price").css("::text").extract()
        product_category = response.css(".breadcrumb-parent-category span").css("::text").extract()
        product_colour = response.css(".attribute-value").css("::text").extract()
        product_size = response.css(".swatch-value").css("::text").extract()
        product_description_full = response.css(".js-full-content").css("::text").extract()
        product_description_short = response.css(".product-description").css("::text").extract()
        product_region = response.css(".currency-placeholder:nth-child(1)").css("::text").extract()

        items['product_name'] = product_name[0].strip()
        items['product_price'] = product_price[0].strip()
        items['product_currency'] = re.search(r'[$€£]', product_price[0].strip())[0]
        items['product_category'] = product_category
        items['product_colour'] = product_colour
        items['product_size'] = [i.strip() for i in product_size] if product_size else ['no available']
        items['product_description'] = product_description_full[0].strip() if product_description_full else product_description_short[0].strip()
        items['product_region'] = product_region[1].strip()
        items['product_link'] = str(response)[5:-1]
        items['product_time'] = datetime.datetime.now()
        yield items
