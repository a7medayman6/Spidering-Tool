from urllib.request import urlopen
from files_organization import * 
from domainChecker import in_domain
from Gatherer import Gatherer
import os



class Spider:
    
    project_name = ''
    base_url = ''
    domain = ''
    dirictory = ''
    wait_list = set()
    crawled = set()
    search_results = set()
    search_word = ''
    wait_list_file = ''
    search_results_file = ''
    crawled_file = ''



    def __init__(self, project_name, base_url, domain, name, search_word):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain = domain
        Spider.search_word = search_word
        self.name = name
        Spider.wait_list_file = os.path.join(Spider.project_name, 'waiting.txt')
        Spider.crawled_file = os.path.join(Spider.project_name, 'crawled.txt')
        Spider.search_results_file = os.path.join(Spider.project_name, 'search_results.txt')
        Spider.trigger()
        print (self.name + "is crawling " + base_url + " ...")
        self.crawl(base_url)

    @staticmethod
    def trigger():
        mkdir(Spider.project_name)
        Spider.dirictory
        touch(Spider.project_name, Spider.base_url) 
        Spider.wait_list = read(Spider.wait_list_file)
        Spider.crawled = read(Spider.crawled_file)


    @staticmethod
    def crawl(url):
        new_links = set()
        if url not in Spider.crawled:
            new_links = Spider.gather_urls(url)
            Spider.add_links(new_links)
        
        Spider.update(url)
          

    @staticmethod
    def add_links(links):
        for url in links:
            if url not in Spider.wait_list and url not in Spider.crawled:
                # check if the domain is right
                #print("Checking the URL domain ...")
                if in_domain(Spider.domain, url):
                    Spider.wait_list.add(url)

    @staticmethod
    def update(url):
        print("Updating the files ...")
        if url in Spider.wait_list:
            Spider.wait_list.remove(url)
        Spider.crawled.add(url)
        write_set(Spider.wait_list_file, Spider.wait_list) 
        write_set(Spider.crawled_file, Spider.crawled) 
            
    @staticmethod
    def gather_urls(url):
        html_page = ''
        print("Gathering links from the URL...")
        try:
            response = urlopen(url)
            if 'text/html' in response.getheader('Content-Type'):
                html = response.read()
                html_page = html.decode('utf-8')
                gatherer = Gatherer(Spider.base_url, url)
                gatherer.feed(html_page)
                #search in html page here
                if Spider.search_word != '':
                    print("Searching ...")
                    if html_page.find(Spider.search_word) and url not in Spider.search_results:
                        Spider.search_results.add(url)
                        print ("Found the word in " + str(url))

                return gatherer.getUrls()
                
        except Exception as e:
            print(str(e))
        
        return set()

   
    #def search(self, page, url):
        
    #    if page.search_word(Spider.search_word) and url not in Spider.search_results:
    #            Spider.search_results.add(url)
    #            print ("Found the word in " + str(url))






##CODE LOGIC
    #  1.Create dirictory, wait list file, and the crawled file
    #  2.Put the base url in the wait list
    #       2.1.Check if the page in the same domain first, if not: ignore it
    #  3.Gather url from the page
    #  4.Put the gathered urls in the wait list set
    #  5.Put the crawled page (base) in the crawled set
    #  6.Remove the base page from the waitlist
    #  7.Repeat from step 3 for each url in the wait list set     