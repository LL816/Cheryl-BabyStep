## one module can have several classes, so from module file import class OR import module, then module.class.method
from MYURL import MyUrl
from MYPatterns import MyPatterns
from MYOperations import MyOperations
import time


def run():
    site = 'http://www.smzdm.com/'

    url = MyUrl(site)
    url.openURL()
    pattern = MyPatterns()
    opertions = MyOperations()

    count = 0
    while 1:
        html = url.postProcess()
        print 'latest news: ******************'
        opertions.getLatest(pattern,html)##every minute retrieve one latest shopping info
        print '******************************'

        if count == 1:
            count = 0
            print 'news summary: ******************'
            opertions.getTop10(pattern,html)##every 10minutes retrieve top 10 worth-to-be shopping info
            print '******************************'
            
        count = count + 1
        time.sleep(60)

if __name__ == '__main__': run()