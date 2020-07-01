from filesOrganization import * 
from domainChecker import in_domain
from Gatherer import Gatherer


class Spider:
    
    project_name = ''
    base_url = ''
    domain = ''
    wait_list = set()
    crawled = set()
    wait_list_file = ''
    crawled_file = ''

    def __init__(self, project_name, base_url, domain):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain = domain
        Spider.wait_list_file = Spider.project_name + '/waiting.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.trigger()
        Spider.crawl()

    @staticmethod
    def trigger():
        mkdir(Spider.project_name)
        touch(Spider.project_name, Spider.base_url)
        touch(Spider.project_name, '')
        wait_list = read(Spider.wait_list_file)
        crawled = read(Spider.crawled_file)

    @staticmethod
    def crawl():
        for url in Spider.wait_list:
            gatherer = Gatherer(Spider.base_url, url)
            new_links = gatherer.getUrls
            gatherer.gather_urls()
            Spider.add_links(new_links)
            Spider.move_to_crawled(url)
        write_set(Spider.wait_list_file, Spider.wait_list)    

    @staticmethod
    def add_links(links):
        for url in links:
            if url not in Spider.wait_list and url not in Spider.crawled:
                # check if the domain is right
                if in_domain(Spider.domain, url):
                    Spider.wait_list.add(url)

    @staticmethod
    def move_to_crawled(url):
        Spider.wait_list.remove(url)
        Spider.crawled.add(url)
            







##CODE LOGIC
    #  1.Create dirictory, wait list file, and the crawled file
    #  2.Put the base url in the wait list
    #       2.1.Check if the page in the same domain first, if not: ignore it
    #  3.Gather url from the page
    #  4.Put the gathered urls in the wait list set
    #  5.Put the crawled page (base) in the crawled set
    #  6.Remove the base page from the waitlist
    #  7.Repeat from step 3 for each url in the wait list set     