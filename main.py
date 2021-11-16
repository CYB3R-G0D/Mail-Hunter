import urllib.request
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
import urllib

print("""
                 _ _ _                 _
 _ __ ___   __ _(_| | |__  _   _ _ __ | |_ ___ _ __
| '_ ` _ \ / _` | | | '_ \| | | | '_ \| __/ _ | '__|
| | | | | | (_| | | | | | | |_| | | | | ||  __| |
|_| |_| |_|\__,_|_|_|_| |_|\__,_|_| |_|\__\___|_|

Find professional email addresses of a business from its domain.
# script by @cyb3r-g0d
    """ )

company = input("Type [like company.com]: ")
text= f'inurl%3A"{company}"+AND+intext%3A"%40{company}"'
url = 'https://google.com/search?q=' + text
urls = []

request = urllib.request.Request(url)
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
raw_response = urllib.request.urlopen(request).read()
html = raw_response.decode("utf-8")
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
    urls.append(link.get('href'))
    with open(f'{company}.txt', 'w') as f:
        f.write(str('\n'.join(urls)))

def repeat():
    lines = open(f'{company}''.txt', 'r').readlines()
    lines_set = set(lines)
    final  = open(f'{company}''.txt', 'w')
    for line in lines_set:
        if "google.com" not in line.strip("\n"):
            final.write(line)
repeat()            

def search():
    f = open(f'{company}.txt')
    lks = [lk.strip() for lk in f.readlines()]
    for lk in lks:
        EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        session = HTMLSession()
        r = session.get(lk)
        r.html.render()
        for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
            print(re_match.group())
search()             