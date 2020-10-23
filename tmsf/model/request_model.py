from common.constants import HTTP_METHOND, HTTP_HEADER


class RequestModel:

    def __init__(self):
        self.headers = {
            "User-Agent": HTTP_HEADER.USER_AGENT,
            "Host": "www.tmsf.com",
            "Cookie": "gr_user_id=3005213d-5479-48c0-b0f8-434c1f87ec87; grwng_uid=e4539a4c-bd21-4912-b000-f03aca4f9a22; bdshare_firstime=1573040595262; Hm_lvt_18f10d8299bec7ffdf82d66d10c93213=1574051412; Hm_lvt_5bbc90d068807d82c72909ecd298e11a=1587905233; UM_distinctid=17206b6bc1f82f-0a73c4cc5c1cd5-d373666-1fa400-17206b6bc209a5; br_access_code=Y+sLp1s+6NsAAAAAvJUaXwAAAABByJsM; X-BR-AntiSpider-Status=1; Hm_lvt_bbb8b9db5fbc7576fd868d7931c80ee1=1603069895,1603173095,1603244216,1603337100; b61f24991053b634_gr_session_id=bbf22a0d-33b3-47f2-b7a2-7b8c2a7edd10; b61f24991053b634_gr_session_id_bbf22a0d-33b3-47f2-b7a2-7b8c2a7edd10=true; BSFIT_EXPIRATION=1603483087805; BSFIT_DEVICEID=e9yTRO-BJtyYdGI0kEJjEyxQcHZSjs0MSX2E0-c4y6FTnoB4cXCsfruvGAoB6QuzRQWHfpG0OdgvIXTFRNtnxntgKiCQSLfkmq3o9jQG84FSGjnIjpAGVYYmkcuam06BsQBopx3sUkz7LVS-SQZOxmMK-Vbq_3zD; JSESSIONID=0400BDAD7BD2AE4D76DFBC1949327D97; CNZZDATA1253675216=1241644750-1576396375-%7C1603436065; __qc_wId=713; pgv_pvid=2240125425; BSFIT_k1w2l=; Hm_lpvt_bbb8b9db5fbc7576fd868d7931c80ee1=1603437865",
        }
        self.url = "http://www.tmsf.com/newhouse/property_searchall.htm?keytype=1&searchkeyword=%E4%B8%AD%E6%97%85%E5%90%8D%E9%97%A8%E5%BA%9C%C2%B7%E6%96%B0%E5%A2%83%28%E5%92%8C%E9%9B%85%E8%BD%A9%29&keyword=%25u4E2D%25u65C5%25u540D%25u95E8%25u5E9C%25B7%25u65B0%25u5883%2528%25u548C%25u96C5%25u8F69%2529"
        self.mothod = HTTP_METHOND.GET