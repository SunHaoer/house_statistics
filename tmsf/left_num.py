import datetime

from common.data_store import select, insert
from common.substr_by_str import substr_by_str
from common.send_requst import send_requst
from tmsf.dto.heyaxuan_left import HeyaxuanLeft
from tmsf.model.request_model import RequestModel

# 解析字符串
def analysis(str):
    # 截取字符串
    startSubStr = "<p class=\"ash1 famwei ft14\">"
    endSubStr = "</p>"
    str = substr_by_str(str, startSubStr, endSubStr)
    startSubStr = "可售"
    endSubStr = "套"
    str = substr_by_str(str, startSubStr, endSubStr)
    num = int(str)

    return num

def store_data(num):
    sql = """select num from heyaxuan_left
        where `date` = %s"""
    param = str(datetime.date.today() + datetime.timedelta(-1))
    last_num = select(sql, param)
    if last_num.__len__() != 0:
        last_num = last_num[0][0]
    else:
        last_num = 0

    heyaxuan_left = HeyaxuanLeft(num, last_num)
    sql = """insert into heyaxuan_left 
        (`num`, `sell_num`, `date`) 
        values (%s, %s, %s)"""
    params = []
    params.append([heyaxuan_left.num, heyaxuan_left.sell_num, heyaxuan_left.date])
    params = tuple(params)
    insert(sql, params)

# 透明售房网和雅轩剩余房源
def action():
    print("-----start-------")

    requst_model = RequestModel()
    html = send_requst(requst_model.url, requst_model.headers, requst_model.mothod)
    data = analysis(html)
    store_data(data)
    print("-----end---------")


if __name__ == '__main__':
    print("start")
    action()
    print("end")


