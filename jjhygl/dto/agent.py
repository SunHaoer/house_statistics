import datetime

class Agent:

    # name: 中介名称
    # cnt: 当日挂牌量
    # date: 日期
    def __init__(self, name, cnt):
        self.name = name
        self.cnt = cnt
        self.date = datetime.date.today()