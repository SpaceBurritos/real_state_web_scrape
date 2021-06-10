import scrapy
from scrapy.loader import ItemLoader
from ..items import RealstatescrapeItem


class QuotesSpider(scrapy.Spider):
    name = "realState"

    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        'accept-language': 'en-US, en;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'Accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    def start_requests(self):
        urls = [
            'https://www.re.cr/en/recent-for-sale-for-rent-properties-in-costa-rica'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for href in response.xpath("//a[contains(@class, 'summary url')]//@href"):
            url = href.extract()
            yield response.follow(url,
                                  callback=self.parse_dir_contents,
                                  headers=self.headers)

        next_page = response.xpath("//span[@class = 'next']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page,
                                  headers=self.headers)


    def parse_dir_contents(self, response):

        for i in response.xpath("//*[@class = 'listing detail']"): #("//*[@id='listing-info']"):
            real_state = ItemLoader(item=RealstatescrapeItem(), selector=i)
            real_state.add_xpath('name', "./h1/text()")
            real_state.add_xpath('price', ".//div[@class = 'listing__price']/dd/text()")
            real_state.add_xpath('id', ".//div[@class = 'listing__id']/dd/text()")
            real_state.add_xpath("status", ".//div[@class = 'listing__workflow_status']/dd/text()")
            real_state.add_xpath("loc_type", ".//div[@class = 'listing__location_type']/dd/text()")
            real_state.add_xpath("view_type", ".//div[@class = 'listing__view_type']/dd/text()" )
            real_state.add_xpath("total_lot_size", ".//div[@class = 'listing__lot_size']/dd/text()")
            real_state.add_xpath("lot_living", ".//div[@class = 'listing__living_area']/dd/text()")
            real_state.add_xpath("num_bedrooms", ".//div[@class = 'listing__beds']/dd/text()")
            real_state.add_xpath("num_full_bath", ".//div[@class = 'listing__baths']/dd/text()")
            real_state.add_xpath("stories", "//tbody/tr[@class = 'stories']/td/text()")
            real_state.add_xpath("floor_type", "//tbody/tr[@class = 'flooring_type_meta']/td/text()")
            real_state.add_xpath("construction_status", "//tbody/tr[@class = 'construction_status']/td/text()")
            real_state.add_xpath("year", "//tbody/tr[@class = 'year_built']/td/text()")
            real_state.add_xpath("has_aircon", "//tbody/tr[@class = 'air_condition_meta']/td/text()")
            real_state.add_xpath("furnished_type", "//tbody/tr[@class = 'furnished_meta']/td/text()")
            real_state.add_xpath("pool_type", "//tbody/tr[@class = 'pool_meta']/td/text()")
            real_state.add_xpath("has_jacuzzi", "//tbody/tr[@class = 'jacuzzi_meta']/td/text()")
            real_state.add_xpath("parking_type", "//tbody/tr[@class = 'parking_meta']/td/text()")
            real_state.add_xpath("has_internet", "//tbody/tr[@class = 'internet_meta']/td/text()")
            real_state.add_xpath("has_television", "//tbody/tr[@class = 'television_meta']/td/text()")
            real_state.add_xpath("country", "//tbody/tr[@class = 'country']/td/text()")
            real_state.add_xpath("state", "//tbody/tr[@class = 'state']/td/text()")
            real_state.add_xpath("county", "//tbody/tr[@class = 'county']/td/text()")
            real_state.add_xpath("district", "//tbody/tr[@class = 'district']/td/text()")
            real_state.add_xpath("city", "//tbody/tr[@class = 'city']/td/text()")
            real_state.add_xpath("price_sq_m", "//tbody/tr[@class = 'price_per_sqm']/td/text()")
            real_state.add_xpath("price_ac_area", "//tbody/tr[@class = 'price_per_ac_area']/td/text()")
            yield real_state.load_item()
