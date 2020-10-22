import datetime


class DayTotal:
    # total: 今日总量
    # increase: 相比昨日增长量
    # date: 当天日期
    def __init__(self, total, last_total):
        self.total = total
        self.increase = total - last_total
        self.date = datetime.date.today()
