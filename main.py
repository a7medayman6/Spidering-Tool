"""
the driver code.
"""
from Spider import Spider
from domainChecker import get_domain_name
from files_organization import *

PROJECT_NAME = 'crackstation'
BASE_URL = 'https://crackstation.net/'
DOMAIN = get_domain_name(BASE_URL)
SPIDER_ID = 1
SEARCH_WORD = 'security'
Spider(PROJECT_NAME, BASE_URL, DOMAIN, 'Spider' + str(SPIDER_ID), SEARCH_WORD)
while True:
    if len(Spider.wait_list) <= 0:
        break 
    BASE_URL = Spider.wait_list.pop()
    Spider.wait_list.add(BASE_URL)
    Spider(PROJECT_NAME, BASE_URL, DOMAIN, 'Spider' + str(SPIDER_ID), SEARCH_WORD)

URLS_GATHERED = len(Spider.crawled)
print ('\n' + "Finished Crawlin.\n" + "Number of URLs Gathered:\t" + str(URLS_GATHERED))

if SEARCH_WORD != '' :
    print("\nSearch Results:\nThe Search Word Found in These URLS:\n")
    for url in Spider.search_results:
        print (url)
    write_set(Spider.search_results_file, Spider.search_results)
