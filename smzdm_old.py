import urllib2
import re
import time

site = 'http://www.smzdm.com/'

##Some websites [2] dislike being browsed by programs, or send different versions to different browsers [3].
## By default urllib2 identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the Python release,
## e.g. Python-urllib/2.5), which may confuse the site, or just plain not work. The way a browser identifies itself is through the User-Agent header [4].
## When you create a Request object you can pass a dictionary of headers in.
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
request=urllib2.Request(site,headers = headers)

TITLE = r'<h4class="itemName">(.*?)target="_blank">(.*?)<spanclass="red">'
SUPPORT =r'"class="good"id="rating_worthy_(.*?)<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>'
OPPOSITE =r'"class="bad"id="rating_unworthy_(.*?)<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>'
LINK = r'<divclass="buy"style="z-index:2;"> <ahref="(.*?)"'

while 1:
    try:
        response = urllib2.urlopen(request) ##in case fail to open certain url
    except urllib2.HTTPError as e:
        print(e.reason)

    html = response.read()
    html = html.replace(" ","")
    html = html.replace("\t","")
    html = html.replace("\r\n"," ")

    title = re.search(TITLE,html)
    support = re.search(SUPPORT,html)
    opposite = re.search(OPPOSITE,html)
    link = re.search(LINK,html)
    ## match VS search:  match pattern starts from the very first character; search whole file contains certain pattern

    if title:
        print title.group(2)
    if support:
        print support.group(2)
    if opposite:
        print opposite.group(2)
    if link:
        print link.group(1)
    else:
        print("ERROR!!")

    time.sleep(60)
