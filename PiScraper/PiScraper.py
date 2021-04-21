import bisect
import json
import os

import requests


def getDate(ledgerdate):
    return int(ledgerdate.split('T')[0].replace('-', ''))


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


def scrapeCarelessly(link):
    page = requests.get(link)
    X = json.loads(page.content)
    return X


def scrape_pi_testnet_ledger(ledgerID):
    ledgerID_S = str(ledgerID)
    ledgerbase = "https://api.testnet.minepi.com/ledgers/" + ledgerID_S
    ledgerdict = scrapeToCache(ledgerbase, "ldgr_" + ledgerID_S)
    return ledgerdict


def getLastLedgerNumber():
    ledgerdict = scrapeCarelessly("https://api.testnet.minepi.com/ledgers?order=desc")
    return ledgerdict['_embedded']['records'][0]['sequence']


def identify_greq(date, knownDates: dict):
    L = list(knownDates.keys())
    L.sort()
    V = [knownDates[e] for e in L]
    return


def identify_sender(transactionDict):


def main():
    last = getLastLedgerNumber()
    data = scrapeToCache("https://api.testnet.minepi.com/ledgers/1354636", 'ld_1354636.txt')
    return


if __name__ == "__main__":
    main()
