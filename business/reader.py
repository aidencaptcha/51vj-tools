# -*- coding: utf-8 -*-
import time
import requests
from loguru import logger
# from settings import CORPID, USER_COOKIES


def reader(business_id, corpid, cookies):
    """阅读动态"""
    timestamp = int(time.time() * 1000)
    # corpid = CORPID
    # _cookie = USER_COOKIES

    url = f'https://qy.51vj.cn/club/reader/{business_id}'
    params = {
        '_': f'{timestamp}',
        '_v': '1.2.7',
        'corpid': f'{corpid}',
        'appid': '31',
        'parentid': '1002',
    }
    payload = {}
    headers = {
        'Accept': 'application/json;charset=utf-8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 'cookie': _cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

    response = requests.post(url, params=params, headers=headers, cookies=cookies, data=payload)
    logger.debug(response.text)


# if __name__ == '__main__':
#     business_id = 'xxx'
#     reader(business_id)

# 成功响应:
# {"success": true,"msg": "更新成功","community": {"pv": 1}}
