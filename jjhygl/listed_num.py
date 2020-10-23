import datetime
from common.data_store import insert, select
from common.send_requst import send_requst
from common.substr_by_str import substr_by_str
from jjhygl.dto.agent import Agent

# 发送请求
from jjhygl.dto.day_total import DayTotal
from jjhygl.model.request_model import RequestModel


# def send_requst(url, headers, methond):
#     req = request.Request(url=url, headers=headers, method=methond)
#     response = request.urlopen(req)
#     html = response.read().decode('utf-8')
#     return html

# 解析字符串
def analysis(str):
    # 截取字符串
    startSubStr = "<div class=\"lastMonthList\">"
    endSubStr = "</div>"
    str = substr_by_str(str, startSubStr, endSubStr)

    # 提取数据
    strs = str.split("\n")
    startSubStr1 = "<b class=\"b1\">"
    endSubStr1 = "</b>"
    startSubStr2 = "<b class=\"b2\">"
    endSubStr2 = "套</b>"
    result = []
    i = 0
    for item in strs:
        i += 1
        if i == 1 or i == len(strs):
            continue
        value1 = item[item.find(startSubStr1) + len(startSubStr1) : item.find(endSubStr1)]
        value2 = item[item.find(startSubStr2) + len(startSubStr2) : item.find(endSubStr2)]
        agent = Agent(value1, value2)
        result.append(agent)
    return result

# 每日数据存入数据库
def store(data):
    sql = """insert into house_agent 
    (`name`, `count`, `date`) 
    values (%s, %s, %s)"""

    params = []
    for item in data:
        params.append([item.name, item.cnt, item.date])
    params = tuple(params)
    insert(sql, params)

# 每日数据总量存入数据库
def store_total(data):
    total = 0
    for item in data:
        total += int(item.cnt)
    sql = """select total from day_total
    where date = %s"""
    param = str(datetime.date.today() + datetime.timedelta(-1))
    last_total = select(sql, param)
    if last_total.__len__() != 0:
        last_total = last_total[0][0]
    else:
        last_total = 0

    day_total = DayTotal(total, last_total)
    sql = """insert into day_total 
    (`total`, `increase`, `date`) 
    values (%s, %s, %s)"""
    params = []
    params.append([day_total.total, day_total.increase, day_total.date])
    params = tuple(params)
    insert(sql, params)


# 杭州二手房管理平台各中介挂牌数量
def action():
    print("-----start-------")

    requst_model = RequestModel()
    html = send_requst(requst_model.url, requst_model.headers, requst_model.mothod)
    data = analysis(html)
    store(data)
    store_total(data)

    print("-----end---------")


if __name__ == '__main__':
    print("start")
    action()
    print("end")

