import json

import requests


def main(scrapeNew=False):
    if scrapeNew:
        page = requests.get("https://api.testnet.minepi.com/ledgers/1354636/transactions")
        F = open('picache.txt', 'wb')
        F.write(page.content)
        F.close()
        Y = json.loads(page.content)
    F = open('picache.txt', 'rb')
    content = F.read()
    F.close()
    X = json.loads(content)
    return


if __name__ == "__main__":
    main(True)
