def domain_name(url):
    return url.split("//")[-1].split('www.')[-1].split('.')[0]


d1 = 'http://www.google.com'
d2 = 'https://www.google.com'
d3 = 'www.google.com'
d4 = 'google.com'


print(domain_name(d1))
print(domain_name(d2))
print(domain_name(d3))
print(domain_name(d4))



