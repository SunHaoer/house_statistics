import datetime


class HeyaxuanLeft:
    # num: 今日剩余房源
    # sell_num: 今日出售量
    # date: 当天日期
    def __init__(self, num, last_num):
        self.num = num
        self.sell_num = num - last_num
        self.date = datetime.date.today()