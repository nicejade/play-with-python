import sys

sys.path.append("..")
import requests
from bs4 import BeautifulSoup
from utils import *


def main():
    url = "https://nicelinks.site/explore/all\?_escaped_fragment_"
    htmlContent = requests.get(url)
    soup = BeautifulSoup(htmlContent.text, "lxml")
    nicelinks_list = soup.find(class_="links-list").find_all(
        "div", class_="el-card__body"
    )
    result = []
    for card in nicelinks_list:
        item = card.find(class_="title-link")
        print(item.get_text().strip())
        result.append({"title": item.get_text().strip(), "link": item.get("href")})
    print_json(result)


if __name__ == "__main__":
    main()
