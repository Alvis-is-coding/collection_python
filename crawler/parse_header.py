#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""用于把直接从chrome中直接复制得到的headers，cookies，formdata等转成dict,
作为requests的参数"""


def header_to_dict(s):
    arg_list = [line.strip() for line in s.split('\n')]
    d = {}
    for i in arg_list:
        if i:
            k = i.split(':')[0].strip()
            v = i.split(':')[1].strip()
            d[k] = v
    return d


def cookies_to_dict(s):
    arg_list = [line.strip() for line in s.split(';')]
    d = {}
    for i in arg_list:
        if i.isalnum:
            k = i.split('=')[0].strip()
            v = i.split('=')[1].strip()
            d[k] = v
    return d


def form_to_dict(s):
    arg_list = s.rstrip('&').split('&')
    d = {}
    for i in arg_list:
        if i.isalnum:
            k = i.split('=')[0].strip()
            v = i.split('=')[1].strip()
            d[k] = v
    return d


def to_dict(s, s_type):
    type_to_delimiter = {
        'headers': '\n',
        'cookies': ';',
        'form': '&',
    }
    arg_list = s.rstrip('&').split(type_to_delimiter[s_type])
    d = {}
    for i in arg_list:
        if i:
            k = i.split(':')[0].strip()
            v = i.split(':')[1].strip()
            d[k] = v
    return d


def print_li(li):
    if isinstance(li, dict):
        for k, v in li.items():
            print k, v
    else:
        for i in li:
            print i

# for test


headers_string = """
Host: www.lagou.com
Connection: keep-alive
Content-Length: 39
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://www.lagou.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: http://www.lagou.com/gongsi/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4
"""

cookies_string = """
user_trace_token=20150911115414-e35eaafdf3cd430fb0a9fed4ca568273; LGUID=20150911115415-c53a987d-5838-11e5-8fa5-525400f775ce; index_location_city=%E5%85%A8%E5%9B%BD; fromsite=www.baidu.com; utm_source=""; JSESSIONID=EED312B8948E60558F066C0002C75135; _gat=1; _ga=GA1.2.878965075.1441943655; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1441943655,1443437945; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1444376663; LGSID=20151009150714-5ea0c1d1-6e54-11e5-b35a-5254005c3644; LGRID=20151009154423-8f30b779-6e59-11e5-b35d-5254005c3644
"""

form_string = """
first=false&pn=1&sortField=0&havemark=0
"""

def test_headers_to_dict():
    d = header_to_dict(headers_string)
    print_li(d)


def test_cookies_to_dict():
    d = cookies_to_dict(cookies_string)
    print_li(d)


def test_form_to_dict():
    d = form_to_dict(form_string)
    print_li(d)

test_headers_to_dict()
#test_cookies_to_dict()
#test_form_to_dict()
