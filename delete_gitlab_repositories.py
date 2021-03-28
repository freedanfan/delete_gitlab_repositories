#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    : delete_gitlab_repositories.py    
@Time    : 2021/03/28 13:21
@Author  : freedanfan
@Contact : freedanfan@mail.com
@License : Copyright (c) 2021, MIT License

@Desc    : 批量删除GitHub的仓库

@Modify Time      @Author        @Version    @Desciption
------------      -----------    --------    -----------
2021/03/28        freedanfan      1.0         New
"""

from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token 5a2aa5506c59d7d085e03968faa08406ecc8564f",  # 此处的XXX代表上面的token
    "X-OAuth-Scopes": "repo"
}

with open('./repos.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    if line == '' or line[0] == '#':
        continue
    try:
        name, repo = line.strip().split("/")
    except IOError:
        continue
    urls.append(url.format(name, repo))

for i in range(len(urls)):
    print("repository =", urls[i])
    ret = requests.delete(url=urls[i], headers=headers)
    sleep(2)
    print(ret)
