import requests
import re
from bs4 import BeautifulSoup
from utils import *


def getHtmlContent(page):
    url = "https://github.com/search?p=" + str(page) + "&q='快应用'"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
    }
    result = requests.get(url, headers=HEADERS, timeout=5)
    try:
        if result.status_code == 200:
            return result.text
    except:
        print("获取链接失败!")


def isStarReachLimit(star, limit):
    pattern = re.compile(r"^(\d+)(\.{0,1})(\d*)k")
    num = pattern.match(star)
    if num and int(num.groups()[0]) >= 1:
        return True
    pattern = re.compile(r"^(\d+)")
    num = pattern.match(star).groups()[0]
    if num and int(num) > limit:
        return True
    return False


def parseHtml(html, urlList):
    soup = BeautifulSoup(html, "lxml")
    repoList = soup.find(class_="repo-list").find_all("li")
    for li in repoList:
        item = li.find("a", class_="v-align-middle")
        star = li.find_all("a", class_="muted-link")
        if len(star) == 1:
            star = star[0].get_text().strip()
        else:
            star = star[len(star) - 1].get_text().strip()
        if isStarReachLimit(star, 3):
            link = "https://github.com" + item["href"]
            urlList.append(link)


def spider(page):
    urlList = []
    htmlBody = getHtmlContent(page)
    parseHtml(htmlBody, urlList)
    print_json(urlList)


if __name__ == "__main__":
    for page in range(1, 3):
        try:
            spider(page)
        except:
            continue
