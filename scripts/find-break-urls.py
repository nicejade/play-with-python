import os
import re
import sys
import time
import requests
from pathlib import Path
from utils import *

# 增加重连次数
requests.adapters.DEFAULT_RETRIES = 5

# 爬出来的所有链接
all_urls_list = []
# 不能正常访问链接
break_urls_list = []


def read_deal_file(path):
    with open(path, encoding="utf-8") as file:
        contents = file.read()
        file.close()
        all_urls = find_all_urls(contents)
        all_urls_list.extend(all_urls)


def write_urls_to_txt(urls_list, filename):
    output_dir = Path("scripts/output/")
    if not output_dir.is_dir():
        os.mkdir("scripts/output")
    file = open("scripts/output/" + filename, "w")
    print(urls_list)
    urls_list_str = "\n".join(urls_list)
    print(urls_list_str)
    file.write(urls_list_str)
    file.close()


def request_url(url):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
    }
    try:
        req = requests.session()
        # Fix requests“Max retries exceeded with url” error
        req.keep_alive = False  # 关闭多余连接
        resp = req.get(url, headers=HEADERS, timeout=6)
        if resp.status_code != 200:
            print(url)
            break_urls_list.append(url)
    except BaseException as err:
        print("Something Error @Url :" + url)
        print(err)
        break_urls_list.append(url)


def check_is_break(urls_list):
    counter = 0
    # 先将列表去重
    print("所获得的 Url 链接条数为：" + str(len(urls_list)))
    urls_list = list(set(urls_list))
    write_urls_to_txt(urls_list, "all_urls.txt")
    print("去重后的 Url 链接条数为：" + str(len(urls_list)))
    for url in urls_list:
        counter = counter + 1
        print("正在检查第 " + str(counter) + " Url 链接.")
        time.sleep(2)
        request_url(url)
    write_urls_to_txt(break_urls_list, "break_urls.txt")


def traverse_dir(path):
    # 得到文件夹下的所有文件名称
    files = os.listdir(path)
    for file in files:  # 遍历文件夹
        # 判断是否是文件夹，不是文件夹才打开
        sub_path = os.path.join(path, file)
        if os.path.isdir(sub_path) and (sub_path[0] != "."):
            traverse_dir(sub_path)
        else:
            if check_is_expected(file):
                read_deal_file(sub_path)


if __name__ == "__main__":
    argvList = sys.argv
    specifiedPath = argvList[1]
    fileIns = Path(specifiedPath)
    if fileIns.is_dir():
        traverse_dir()
    else:
        read_deal_file(specifiedPath)
    check_is_break(all_urls_list)
