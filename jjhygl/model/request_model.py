from common.constants import HTTP_METHOND, HTTP_HEADER


class RequestModel:

    def __init__(self):
        self.headers = {
            "User-Agent": HTTP_HEADER.USER_AGENT,
            "Host": "jjhygl.hzfc.gov.cn",
        }
        self.url = "http://jjhygl.hzfc.gov.cn/webty/gpfy/gpfySelectlist.jsp"
        self.mothod = HTTP_METHOND.GET