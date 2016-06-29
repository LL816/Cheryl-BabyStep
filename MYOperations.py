from MYPatterns import MyPatterns
import operator

class MyOperations:
    def __init__(self):
        self.latest = {'title':'','support':'','opposite':'','link':''}
        self.top10 = []

    def getLatest(self, patterns, html):
        self.latest = patterns.getLatestInfo(html)
        for item in reversed(self.latest.keys()):
            print item + ': ' + self.latest[item]

    def getTop10(self, patterns, html):
        allMatch = patterns.AllInfo(html)
        index = 0
        rank = {}
        for item in allMatch:
            rank[index] = int(item[1]) - int(item[2])
            index = index + 1

        sorted_rank = sorted(rank.items(),key=operator.itemgetter(1),reverse=True)
        index = 0
        for item in sorted_rank:
            self.top10.append(allMatch[item[0]])
            index = index + 1
            if index == 10:
                break

        for item in self.top10:
            print 'title: ' + item[0] +' support: ' +item[1] + ' opposite: ' + item[2] + ' link: ' +item[3]


