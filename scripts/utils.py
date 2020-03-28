import re
import os
from pathlib import Path
from urllib.parse import urlparse

# 检查是否为 url
def check_is_url(string):
    return re.match("(https?\://[a-zA-Z0-9\-_\u4e00-\u9fa5\.\?/&\=\:]+)", string)


# 检查是否是期待的文件（根据文件后缀）
def check_is_expected(filename):
    expected_file_list = [".md", ".js", ".html"]
    file_extension = os.path.splitext(filename)[-1]
    return file_extension in expected_file_list


# 找出 string 中所有链接，数组；
def find_all_urls(string):
    # findall() 查找匹配正则表达式的字符串
    links = re.findall("(https?\://[a-zA-Z0-9\-_\u4e00-\u9fa5\.\?/&\=\:]+)", string)
    return links


# 对 url 是以 "/" 或 "//" 地址，恢复真是地址
def restore_url_real_path(target_url, url):
    parse_result = urlparse(url)
    scheme = parse_result.scheme
    netloc = parse_result.netloc
    if target_url.startswith("//"):
        return scheme + ":" + target_url
    if target_url.startswith("/"):
        return scheme + "://" + netloc + target_url
    return target_url
