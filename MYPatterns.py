import re

class MyPatterns:
    patterns={}
    def __init__(self):
    #    self.patterns['TITLE'] = re.compile(r'<divclass="list".*?<h4class="itemName">.*?target="_blank">(.*?)<spanclass="red">')
    #    self.patterns['SUPPORT'] = re.compile(r'"class="good"id="rating_worthy_.*?<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>')
    #    self.patterns['OPPOSITE'] = re.compile(r'"class="bad"id="rating_unworthy_.*?<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>')
    #    self.patterns['LINK'] = re.compile(r'<divclass="buy"style="z-index:2;"> <ahref=".*?"')
        self.patterns['ALL'] = re.compile(r'<divclass="list".*?<h4class="itemName">.*?target="_blank">(.*?)<spanclass="red">.*?"class="good"id="rating_worthy_.*?<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>.*?"class="bad"id="rating_unworthy_.*?<spanclass="scoreTotal"><.*?><em>(\d*?)</em></span>.*?<divclass="buy"style="z-index:2;"> <ahref="(.*?)"')


    def getLatestInfo(self,html):
        #return {'title':self.getTitle(html),'support':self.getSupport(html),'opposite':self.getOpposite(html),'link':self.getLink(html)}
        latest = re.search(self.patterns['ALL'],html)
        if latest:
            return {'title':latest.group(1),'support':latest.group(2),'opposite':latest.group(3),'link':latest.group(4)}
        else:
            return {'title':'','support':'','opposite':'','link':''}


    def AllInfo(self,html):
        all = re.findall(self.patterns['ALL'],html)
        if all:
            return all
        else:
            return [()]

#    def getTitle(self,html):
#        ## match VS search:  match pattern starts from the very first character; search whole file contains certain pattern
#        title = re.search(self.patterns['TITLE'],html)
#        if title:
#            return title.group(1)
#        else:
#            return ''
#
#    def getSupport(self,html):
#        support = re.search(self.patterns['SUPPORT'],html)
#        if support:
#            return support.group(1)
#        else:
#            return ''
#
#    def getOpposite(self,html):
#        opposite = re.search(self.patterns['OPPOSITE'],html)
#        if opposite:
#            return opposite.group(1)
#        else:
#            return ''
#
#    def getLink(self,html):
#        link = re.search(self.patterns['LINK'],html)
#        if link:
#            return link.group(1)
#        else:
#            return ''
#
#    def allTitle(self,html):
#        ## match VS search:  match pattern starts from the very first character; search whole file contains certain pattern
#        title = re.findall(self.patterns['TITLE'],html)
#        if title:
#            for item in title:
#                print item
#        else:
#            return ''
#
#    def allSupport(self,html):
#        support = re.findall(self.patterns['SUPPORT'],html)
#        if support:
#            for item in support:
#                print item
#        else:
#            return ''
#
#    def allOpposite(self,html):
#        opposite = re.findall(self.patterns['OPPOSITE'],html)
#        if opposite:
#            for item in opposite:
#                print item
#        else:
#            return ''
#
#    def allLink(self,html):
#        link = re.findall(self.patterns['LINK'],html)
#        if link:
#            for item in link:
#                print item
#        else:
#            return ''
#
