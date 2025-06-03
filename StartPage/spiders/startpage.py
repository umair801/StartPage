import scrapy
from ..sp_IMPORT import names
from datetime import datetime


class StartPageSpider(scrapy.Spider):
    name = "startpage"
    custom_settings = {
        "FEEDS": {f"{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv": {"format": "csv"}}
    }
    
    index = 0
    def start_requests(self):
        headers = {
            'accept-language': 'en-US,en;q=0.9,ar;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        }

        for name in names:
            yield scrapy.FormRequest(
                url=f'https://www.startpage.com/sp/search?query=realestate.com.au/agent {name}',
                headers=headers,
                callback=self.parse_data,
                meta={'name': name},
            )

    def parse_data(self, response):
        name = response.meta['name']
        
        with open(f'HTML_Files/{self.index}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f'file {self.index}.html saved...')
        self.index += 1
        
        
        rows = response.xpath('//a[contains(@href,"realestate.com.au/agent/")]')
        for row in rows:
            url = row.xpath('./@href').get()
            
            yield {
                'name': name,
                'agent url': url.replace('reviews', ''),
                'URL': response.url,
            }
            
            
    
