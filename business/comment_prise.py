# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger


def comment_prise(comment_id, corpid, cookies):
    """点赞评论

    :param comment_id: _description_
    :param corpid:
    :param cookies:
    """
    timestamp = int(time.time() * 1000)
    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    url = f'https://qy.51vj.cn/userpreference/comment/prise/{comment_id}'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'app-id': '31',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002'
    }

    payload = {}
    response = requests.post(
        url, params=params, headers=headers, cookies=cookies, data=payload)

    logger.debug(response.text)
