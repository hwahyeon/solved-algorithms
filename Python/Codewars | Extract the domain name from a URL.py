from urllib import parse

def domain_name(url):
    url_ = parse.urlparse(url)
    lst_ = url_.path.split('.') if url_.scheme == '' else url_.netloc.split('.')
    return lst_[1] if 'www' in lst_ else lst_[0]
