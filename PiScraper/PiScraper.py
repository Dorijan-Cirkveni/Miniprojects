import json
import os

import requests


def getDate(ledgerdate):
    return int(ledgerdate.split('T')[0].replace('-', ''))


def saveToCache():
    # TODO
    return


def scrapeToCache(link, cachename):
    if cachename is not None:
        cache = 'cache\\' + cachename
        if not os.path.exists(cache):
            page = requests.get(link)
            F = open(cache, 'wb')
            F.write(page.content)
            F.close()
        F = open(cache, 'rb')
        content = F.read()
        F.close()
    else:
        page = requests.get(link)
        content = page.content
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


def getSendersForAllTransactions(currentLink, cacheUse=True):
    i = 0
    score = dict()
    if cacheUse:
        pass  # TODO
    while True:
        ledgerdict = scrapeToCache(currentLink, None)
        txList = ledgerdict['_embedded']["records"]
        if len(txList) == 0:
            break
        for tx in txList:
            source = tx["source_account"]
            if source not in score:
                score[source] = 0
            score[source] += 1
        currentLink = ledgerdict['_links']['next']['href']
        i += 1
    return score


def getSendersForLedgersInRange(beginLedger, endLedger):
    sdx = dict()
    for i in range(beginLedger, endLedger):
        print(i)
        data = getSendersForAllTransactions('https://api.testnet.minepi.com/ledgers/{}/transactions'
                                            .format(str(i)))
        for e in data:
            if e not in sdx:
                sdx[e] = 0
            sdx[e] += data[e]
    return  # TODO


def main():
    getSendersForLedgersInRange(1373100, 1373150)
    return


if __name__ == "__main__":
    main()
