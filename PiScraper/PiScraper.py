import json
import os

import requests

def getDate(ledgerdate):
    return int(ledgerdate.split('T')[0].replace('-',''))
def scrapeToCache(link, cachename):
    cache = 'cache\\' + cachename
    if not os.path.exists(cache):
        page = requests.get(link)
        F = open(cache, 'wb')
        F.write(page.content)
        F.close()
    F = open(cache, 'rb')
    content = F.read()
    F.close()
    X = json.loads(content)
    return X


def scrape_pi_testnet_ledger(ledgerID):
    ledgerbase = "https://api.testnet.minepi.com/ledgers/" + str(ledgerID)
    ledgerdict = scrapeToCache(ledgerbase)
    return ledgerdict

def getLastLedgerNumber():
    ledgerbase = "https://api.testnet.minepi.com/ledgers
    ledgerdict = scrapeToCache(ledgerbase)
    return 


def identify_first_at(date, knownDates=dict()):

    return


def main():
    data = scrapeToCache("https://api.testnet.minepi.com/ledgers/1354636", 'ld_1354636.txt')
    return


if __name__ == "__main__":
    main()
