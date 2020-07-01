from Spider import Spider
from domainChecker import get_domain_name


project_name = 'drewadwade'
base_url = 'https://drewadwade.github.io/ctfs/'
domain = get_domain_name(base_url)
Spider(project_name, base_url, domain)
