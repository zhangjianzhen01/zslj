# 调用requests库
import requests
# 调用日志代码
from business import logger as rz
# 调用登录系统代码
import business.dlxt
from business import dlxt

# 定义token
a = dlxt.test_dl()['data']['token']


# 创建任务单


def test_cjrwd():
    # 创建url
    cj_url = 'http://1.13.4.226:9002/admin/businesss/addTaskOrder'

    # 创建请求头
    cj_header = {
        "Content-Type": "application/json;charset=UTF-8", "authorization": f"Bearer {a}"
    }
    # 创建请求体
    cj_data = {"customer_id": 1459, "company_province": 161792, "company_city": 161793, "company_area": 162794,
               "company_address": "中江路", "company_name": "宋", "cust_no": "KH22100019",
               "plan_time": "1998-01-31T08:56:03.000Z", "contact_name": "刘亦亭", "contact_phone": "15000295726",
               "describe": "测试的情况描述", "price_list": [
            {"id": 51, "form_id": 5, "form_name": "售后表", "classify_info": ["4", "44", "46"], "classify_id": 46,
             "service_content": "维修服务/配件维修", "service_price": "15.00", "service_divide": 1, "status": 0,
             "creator_id": 107, "operate_id": 107, "created_at": "2022-12-16 12:52:04",
             "updated_at": "2022-12-16 12:52:21", "deleted_at": 0, "creator_name": "黄庆锋", "operate_name": "黄庆锋",
             "classify_name": "内服-内部维修", "classify_info_name": ["售后", "维修服务", "内服-内部维修"],
             "problem_num": 0}], "annex_list": [], "business_id": "695"}

    # 创建post请求
    r = requests.post(url=cj_url, json=cj_data, headers=cj_header)
    rz.logger.debug(f'发送请求:{r}')
    # 打印返回json数据
    print(r.json())
    # 设置创建成功断言
    assert r.json()['msg'] == 'success'
    assert r.json()['code'] == 200

# test_cjrwd()
