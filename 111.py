import requests ,bs4
from bs4 import BeautifulSoup

def getHTMLtest(url):
    try:
        re = requests.get(url)
        re.raise_for_status()
        re.encoding = re.apparent_encoding
        return re.text
    except Exception as e:
        print(e)

def sveCompany(clist,html):
    soup =  BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            clist.append([tds[0].string, tds[4].string, tds[1].string])
def printCompany(clist,num):
    print("{0:^10}\t{1:{3}^50}\t{2:{3}^5}\)".format("排名","国家","企业名称",chr(12288)))
    for i in range(num):
        u=clist[i]
        print("{0:^10}\t{1:{3}^50}\t{2:{3}^5}".format(u[0] , u[1] , u[2] , chr(12288)))
def main():
    sinfo = []
    url = 'http://www.fortunechina.com/fortune500/c/2020-08/10/content_372148.htm'
    html=getHTMLtest(url)
    sveCompany(sinfo, html)
    printCompany(sinfo,500)
main()
