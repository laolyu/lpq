import hashlib
import logging
import os
import time
from typing import List


def get_headers():
    headers = {
        'User-Agent-Platform': 'Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)',
        'lib_net_work_version': '3.0.1',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)',
        'Content-Type': 'application/json; charset=UTF-8',
        'Connection': 'close'
    }
    return headers


def get_user_agent():
    return "Dalvik/2.1.0 (Linux; U; Android 10; GLK-AL00 Build/HUAWEIGLK-AL00)"


def sleep(n_secs):
    time.sleep(n_secs)


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


def get_file_md5(filepath):
    # 获取文件的md5
    if not os.path.isfile(filepath):
        print('文件不存在')
        return
    myhash = hashlib.md5()
    f = open(filepath, "rb")
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    print(myhash.hexdigest())
    print(myhash.hexdigest().upper())
    return myhash.hexdigest()


def url(is_test, host, name):
    if is_test:
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
    # print(result)
    return result


def get_str_md5(oaid, ware_id, imei, tim, udi, DEVICE_SECRET) -> str:
    # md5(oaid + ware_id + imei + time + udi + 秘钥)
    string = concatenate(oaid, ware_id, imei, tim, udi, DEVICE_SECRET)
    result = hashlib.md5(string.encode('utf8')).hexdigest()  # 创建MD5对象，可以直接传入要加密的数据
    print(result)  # 转化为16进制打印md5值
    return result


def get_time():
    timestamp = int(time.time() * 1000)  # 将秒数转换为毫秒数
    # print(timestamp)
    return timestamp
