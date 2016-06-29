import urllib2


class MyUrl:
    def __init__(self,url):
        self.url=url
        ##Some websites [2] dislike being browsed by programs, or send different versions to different browsers [3].
        ## By default urllib2 identifies itself as Python-urllib/x.y (where x and y are the major and minor version numbers of the Python release,
        ## e.g. Python-urllib/2.5), which may confuse the site, or just plain not work. The way a browser identifies itself is through the User-Agent header [4].
        ## When you create a Request object you can pass a dictionary of headers in.
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        self.html = ''

    def openURL(self):
        request=urllib2.Request(self.url,headers = self.headers)
        try:
            response = urllib2.urlopen(request) ##in case fail to open certain url
        except urllib2.HTTPError as e:
            print(e.reason)
        self.html = response.read()

    def postProcess(self):
        return self.html.replace(" ","").replace("\t","").replace("\r\n"," ")
