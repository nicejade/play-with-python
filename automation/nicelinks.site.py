from helium import *

# Api Docs: https://heliumhq.com/docs/api_documentation#python
"""
使用 helium 库，来一键获取指定网站（nicelinks）的一块文本内容（箴言锦语）；
"""


def visite_nicelinks():
    start_chrome("nicelinks.site/?utm_source=python-helium", headless=True)
    go_to("https://nicelinks.site/explore/all/?utm_source=python-helium")
    sentence_elem = find_all(S("#sentence"))
    print("倾城之链 箴言锦语\n")
    for elem in sentence_elem:
        print(elem.web_element.text + "\n")
    kill_browser()


if __name__ == "__main__":
    visite_nicelinks()
