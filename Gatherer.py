from html.parser import HTMLParser
from urllib import parse
from urllib.request import urlopen

class Gatherer(HTMLParser):
    
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.urls = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.urls.add(url)

    def gather_urls(self):
        html_page = ''
        try:
            response = urlopen(self.page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html = response.read()
                html_page = html.decode('utf-8')
                #search in html page here
                self.feed(html_page)
                print("gathering...")
            return self.getUrls()
        except:
            return set()        


    def getUrls(self):
        return self.urls                

    def error(self, message):
        pass

