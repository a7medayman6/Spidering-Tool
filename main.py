from Spider import Spider
from domainChecker import get_domain_name


project_name = 'drewadwade'
base_url = 'https://drewadwade.github.io/ctfs/'
domain = get_domain_name(base_url)
spider = Spider(project_name, base_url, domain)
#top = Spider.wait_list.pop()
#Spider.wait_list.add(top)
#spider.crawl(top)