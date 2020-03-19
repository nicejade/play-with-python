import os
import re
import sys
import time
import requests

all_urls_list = []


def find_all_urls(string):
    # findall() 查找匹配正则表达式的字符串
    links = re.findall("(https?\://[a-zA-Z0-9\-\u4e00-\u9fa5\.\?/&\=\:]+)", string)
    return links


def read_deal_file(path):
    with open(path, encoding="utf-8") as file:
        contents = file.read()
        file.close()
        all_urls = find_all_urls(contents)
        all_urls_list.extend(all_urls)


def check_is_expected(filename):
    expected_file_list = [".md", ".js", ".html"]
    file_extension = os.path.splitext(filename)[-1]
    return file_extension in expected_file_list


def check_is_break(urls_list):
    # 先将列表去重
    print("所获得的 Url 链接条数为：" + str(len(urls_list)))
    urls_list = list(set(urls_list))
    print("去重后的 Url 链接条数为：" + str(len(urls_list)))
    for url in urls_list:
        time.sleep(2)
        HEADERS = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
        }
        try:
            resp = requests.get(url, headers=HEADERS, timeout=6)
            if resp.status_code != 200:
                print(url)
        except BaseException as err:
            print("Something Error @Url :" + url)
            print(err)


def traverse_dir(path):
    # 得到文件夹下的所有文件名称
    files = os.listdir(path)
    for file in files:  # 遍历文件夹
        # 判断是否是文件夹，不是文件夹才打开
        sub_path = os.path.join(path, file)
        if os.path.isdir(sub_path):
            traverse_dir(sub_path)
        else:
            if check_is_expected(file):
                read_deal_file(sub_path)


if __name__ == "__main__":
    argvList = sys.argv
    traverse_dir(argvList[1])
    check_is_break(all_urls_list)
