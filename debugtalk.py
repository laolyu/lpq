# coding:utf-8
import os
import hashlib
import logging
import time
import uuid
from typing import List
import random
import string


# commented out function will be filtered
# def get_headers():
#     return {"User-Agent": "hrp"}
def get_headers():
    headers = {
        'User-Agent-Platform': 'Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)',
        'lib_net_work_version': '3.0.1',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)',
        'Content-Type': 'application/json; charset=UTF-8',
        'Connection': 'close',
        'appid': 114
    }
    return headers


def get_user_agent():
    return "Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)"


def sleep(n_secs):
    time.sleep(n_secs)
    return f"slept: {n_secs}"  # 必须return否则报错


def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def sum_ints(*args: List[int]) -> int:
    result = 0
    for arg in args:
        result += arg
    return result


def sum_two_int(a: int, b: int) -> int:
    return a + b


def sum_two_string(a: str, b: str) -> str:
    return a + b


def sum_strings(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += arg
    return result


def concatenate(*args: List[str]) -> str:
    result = ""
    for arg in args:
        result += str(arg)
    return result


def setup_hook_example(name):
    logging.warning("setup_hook_example")
    return f"setup_hook_example: {name}"


def teardown_hook_example(name):
    logging.warning("teardown_hook_example")
    return f"teardown_hook_example: {name}"


def url(is_test, host, name):
    if is_test == 'test':
        test = 'test-'
    else:
        test = ''

    url = {
        'api': f'http://{test}api-{host}',
        'report': f'http://{test}new-appreport-{host}',
        'cos': f'http://{test}cos-static-{host}',
        'h5': f'http://{test}h5-{host}'
    }
    result = url[name]
    print(result)
    return result


def get_str_md5(oaid, ware_id, imei, tim, udi, DEVICE_SECRET) -> str:
    # md5(oaid + ware_id + imei + time + udi + 秘钥)
    string = concatenate(oaid, ware_id, imei, tim, udi, DEVICE_SECRET)
    result = hashlib.md5(string.encode('utf8')).hexdigest()  # 创建MD5对象，可以直接传入要加密的数据
    print(result)  # 转化为16进制打印md5值
    return result


def get_time():
    timestamp = int(time.time() * 1000)  # 将秒数转换为毫秒数
    timestamp = str(timestamp)  # 将秒数转换为字符串
    # print(timestamp)
    return timestamp


def get_token():
    import jwt
    payload = {
    "aud": "user",
    "exp": 1682647042,
    "jti": "253_6631",
    "iat": 1680055042,
    "nbf": 1680055042,
    "IsReal": "0",
    "Udi": "987cbbf2c141324cb024a75b09f3773f",
    "AppId": 253,
    "Uid": 6631
}
    rc4 = "c6e4b44b219a784b"
    reg = "c6e4b44b219a784be0ef0efe8344c9d9302de4bd6c5e569898d038ddd8752271"
    update ="581e1b32b6e0d00b039c3c825116aab5293e3a76acef097e646542e1df4cdcb1"
    business ="581e1b32b6e0d00b"
    report_p ="1152921504606847229"
    report_s ="039c3c825116aab5"

    secret = report_s

    algorithm = 'HS256'
    token = jwt.encode(payload, secret, algorithm=algorithm)
    print(token)
    assert token=='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1c2VyIiwiZXhwIjoxNjgyNjQ3MDQyLCJqdGkiOiIyNTNfNjYzMSIsImlhdCI6MTY4MDA1NTA0MiwibmJmIjoxNjgwMDU1MDQyLCJJc1JlYWwiOiIwIiwiVWRpIjoiOTg3Y2JiZjJjMTQxMzI0Y2IwMjRhNzViMDlmMzc3M2YiLCJBcHBJZCI6MjUzLCJVaWQiOjY2MzF9.agEv0iH2azLRZU_CnRZCQhDjPbjSENvULQmwDvfRfIc'
    return token

# get_token()

def get_random(a, b):
    rand_num = random.randint(a, b)
    return rand_num


def generate_random_string(length):
    """
    生成随机字符串
    :param length: 字符串长度
    :return: 随机字符串
    """
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))


def get_oaid():
    # 使用Python的uuid模块生成符合标准格式的UUID
    unique_id = uuid.uuid4()  # 生成 UUID
    oaid = str(unique_id)
    return oaid


