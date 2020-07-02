"""
the driver code.
"""
from Spider import Spider
from domainChecker import get_domain_name


PROJECT_NAME = 'crackstation'
BASE_URL = 'https://crackstation.net'
DOMAIN = get_domain_name(BASE_URL)
Spider(PROJECT_NAME, BASE_URL, DOMAIN)
while True:
    if len(Spider.wait_list) <= 0:
        break 
    BASE_URL = Spider.wait_list.pop()
    Spider.wait_list.add(BASE_URL)
    Spider(PROJECT_NAME, BASE_URL, DOMAIN)

