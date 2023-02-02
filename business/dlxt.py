import requests
from business import logger as rz

# 登录系统
# 定义token列表
tk = {'token': None}
# 登录URL
dl_url = "http://1.13.4.226:9001/login"


def test_dl():
    # 登录请求体
    dl_data = {"username": "admin", "password": "huazhou3"}
    # 登录请求头
    dl_header = {"Content-Type": "application/json;charset=UTF-8"}
    # 登录post请求
    r = requests.post(url=dl_url, json=dl_data, headers=dl_header)
    rz.logger.debug(f'发送请求:{r}')
    # 打印响应返回结果
    print(r.json()['message'])
    # 断言登录成功
    assert r.json()['message'] == '登录成功'
    assert r.json()['code'] == 10000
    tk['token'] = r.json()['data']['token']
    return r.json()
# test_dl()
