from urllib.request import urlopen
from files_organization import * 
from domainChecker import in_domain
from Gatherer import Gatherer
import os



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
        Spider.wait_list_file = os.path.join(Spider.project_name, 'waiting.txt')
        Spider.crawled_file = os.path.join(Spider.project_name, 'crawled.txt')
        Spider.trigger()
        Spider.crawl(base_url)

    @staticmethod
    def trigger():
        mkdir(Spider.project_name)
        touch(Spider.project_name, Spider.base_url) 
        Spider.wait_list = read(Spider.wait_list_file)
        Spider.crawled = read(Spider.crawled_file)


    @staticmethod
    def crawl(url):
        new_links = set()
        print(len(Spider.wait_list))
        print(url)
        if url not in Spider.crawled:
            new_links = Spider.gather_urls(url)
            Spider.add_links(new_links)
        
        Spider.update(url)
          

    @staticmethod
    def add_links(links):
        for url in links:
            if url not in Spider.wait_list and url not in Spider.crawled:
                # check if the domain is right
                if in_domain(Spider.domain, url):
                    Spider.wait_list.add(url)

    @staticmethod
    def update(url):
        if url in Spider.wait_list:
            Spider.wait_list.remove(url)
        Spider.crawled.add(url)
        write_set(Spider.wait_list_file, Spider.wait_list) 
        write_set(Spider.crawled_file, Spider.crawled) 
            
    @staticmethod
    def gather_urls(url):
        html_page = ''
        print("gathering...")
        try:
            response = urlopen(url)
            if 'text/html' in response.getheader('Content-Type'):
                html = response.read()
                html_page = html.decode('utf-8')
                gatherer = Gatherer(Spider.base_url, url)
                gatherer.feed(html_page)
                return gatherer.getUrls()
                #search in html page here
                
        except Exception as e:
            print(str(e))
        
        return set()   
       





##CODE LOGIC
    #  1.Create dirictory, wait list file, and the crawled file
    #  2.Put the base url in the wait list
    #       2.1.Check if the page in the same domain first, if not: ignore it
    #  3.Gather url from the page
    #  4.Put the gathered urls in the wait list set
    #  5.Put the crawled page (base) in the crawled set
    #  6.Remove the base page from the waitlist
    #  7.Repeat from step 3 for each url in the wait list set     