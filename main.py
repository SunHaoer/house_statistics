import time
from datetime import datetime
from common.data_store import select
from jjhygl import listed_num

# 运行状态
from tmsf import left_num


def get_running_status(param):
    sql = """select status from task_status
    where `name` = %s"""
    result = select(sql, param)
    if result.__len__() != 0:
        result = result[0][0]
    else:
        result = 0
    return result

def do_sth():
    while True:
        # 总开关
        result = get_running_status("is_running")
        if result == 0:
            break

        # 二手房交易监管平台挂牌量
        now = datetime.now()
        if now.hour == 1:    # 每天1点执行
            is_running = get_running_status("listed_num")
            if is_running == 1:
                listed_num.action()

        if now.hour == 22:
            is_running = get_running_status("left_num")
            if is_running == 1:
                left_num.action()

        # 每小时执行
        time.sleep(60 * 60)


if __name__ == '__main__':
    print("start")
    do_sth()
    print("end")






