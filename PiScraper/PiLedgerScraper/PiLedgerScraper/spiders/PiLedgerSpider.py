import scrapy


class PiLedgerSpider(scrapy.Spider):
    name = "ledger"

    def start_requests(self):
        urls = [
            "https://api.testnet.minepi.com/ledgers/1354636/transactions"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urll = response.url.split("/")
        page = urll[-2]
        filename = f'{page}wasd.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

