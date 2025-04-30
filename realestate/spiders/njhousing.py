import scrapy


class NjhousingSpider(scrapy.Spider):
    name = "njhousing"
    allowed_domains = ["myhousingsearch.com"]
    start_urls = ["https://www.myhousingsearch.com/tenant/index.html?state_id=4041"]

    def parse(self, response):
        base_url = "https://www.myhousingsearch.com"

        # ------- METRO SECTION -------
        for a in response.css("div.metroSection div.citySearchTable a"):
            city_name = a.css("::text").get().strip()
            href = a.attrib["href"]
            city_url = response.urljoin(href)
            data = {
                "section_type": "metroSection",
                "region": "Metropolitan Areas in New Jersey",
                "city": city_name,
                "url": city_url
            }
            print(data)
            yield data

        # ------- REGION SETS -------
        for section in response.css("div.regionSets div.regionSection"):
            region_name = section.css("div.h2 span.light::text").get(default="").strip().rstrip(":")

            for a in section.css("div.citySearchTable a"):
                city_name = a.css("::text").get().strip()
                href = a.attrib["href"]
                city_url = response.urljoin(href)
                data = {
                    "section_type": "regionSets",
                    "region": region_name,
                    "city": city_name,
                    "url": city_url
                }
                print(data)
                yield data
