
def substr_by_str(str, startSubStr, endSubStr):
    startIndex = str.find(startSubStr)
    endIndex = len(str)
    str = str[startIndex : endIndex]
    endIndex = str.find(endSubStr)
    str = str[len(startSubStr) : endIndex]

    return str