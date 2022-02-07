import scrapy

class SouthAfricanSpider(scrapy.Spider):
    name = 'south_african_startups'

    start_urls = [
        'https://startupper.totalenergies.com/en/juries/aL8VXy8wgq3elR8wbWsN4Q/participations/1950/vote?order=alphabetical&scope=all'
    ]

    def parse(self, response):
        yield{
            'leader_name' : response.css('.content-sm a::text').get(),
            'team_name' : response.css('.content-sm h5::text').get(),
            'startup_idea' : response.css('.content-sm.m-t-xs p::text').get(),
            'team_id' : int(response.css('.media-left.media-middle::text').get().split('/')[0]),
            'all_teams' : int(response.css('.media-left.media-middle::text').get().split('/')[-1])
        }
        next_startup = response.css('.right-project::attr(href)').get()
        if next_startup is not None:
            next_startup = response.urljoin(next_startup)
            yield scrapy.Request(next_startup, callback=self.parse)
        

