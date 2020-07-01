from urllib.parse import urlparse



def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

def in_domain(domain, url):
    url_domain = get_domain_name(url)
    if domain == url_domain:
        return True
    return False            