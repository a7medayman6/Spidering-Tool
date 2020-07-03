"""
the driver code.
"""
from Spider import Spider
from domainChecker import get_domain_name
from files_organization import *
from urllib.request import urlopen
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

PROJECT_NAME = 'crackstation'
BASE_URL = 'https://crackstation.net/'
DOMAIN = ''
SPIDER_ID = 1
SEARCH_WORD = 'security'

PROJECT_NAME = input('Enter the project name:\t')



while True:
    BASE_URL = input('Enter The website URL:\t')
    if re.match(regex, BASE_URL) is not None :
        RESPONSE = urlopen(BASE_URL).getcode()
        if RESPONSE != 200:
            WRONG = True
            print ("WRONG URL") 
        else:
            break    
    else:
        WRONG = True
        print ("WRONG URL") 
        
       
DOMAIN = get_domain_name(BASE_URL)
SEARCH_WORD = input('Enter the search text, if there is none press enter:\t')


Spider(PROJECT_NAME, BASE_URL, DOMAIN, 'Spider' + str(SPIDER_ID), SEARCH_WORD)
while True:
    if len(Spider.wait_list) <= 0:
        break 
    BASE_URL = Spider.wait_list.pop()
    Spider.wait_list.add(BASE_URL)
    Spider(PROJECT_NAME, BASE_URL, DOMAIN, 'Spider' + str(SPIDER_ID), SEARCH_WORD)
    SPIDER_ID += 1

URLS_GATHERED = len(Spider.crawled)
print ('\n' + "Finished Crawling.\n" + "Number of URLs Gathered:\t" + str(URLS_GATHERED))

if SEARCH_WORD != '' :
    print("\nSearch Results:\nThe Search Word Found in These URLS:\n")
    for url in Spider.search_results:
        print (url)
    #write_set(Spider.search_results_file, Spider.search_results)
