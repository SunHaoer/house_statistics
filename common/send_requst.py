from urllib import request


def send_requst(url, headers, methond):
    req = request.Request(url, headers=headers, method=methond)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    return html