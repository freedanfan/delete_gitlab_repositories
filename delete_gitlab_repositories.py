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

def parsing_data(token_key, repos_list):
    url = "https://api.github.com/repos/{}/{}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token {}".format(token_key),  # 此处的XXX代表上面的token
        "X-OAuth-Scopes": "repo"
    }
    urls = []
    for line in repos_list:
        if line == '' or line[0] == '#':
            continue
        try:
            name, repo = line.strip().split("/")
        except IOError:
            print("ERROR: cannot delete repo name:", line)
            continue
        urls.append(url.format(name, repo))

    for i in range(len(urls)):
        print("deleting repository: ", urls[i])
        ret = requests.delete(url=urls[i], headers=headers)
        sleep(2)
        print(ret)

    return urls

if __name__ == '__main__':
    # 具有删除权限的 token
    delete_repo_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    # 文档路径，填写需要删除的库
    file_path = './repos.txt'

    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.readlines()

    parsing_data(delete_repo_token, data)

    print("finished.")







