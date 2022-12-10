from urllib.error import HTTPError
from urllib.request import Request, urlopen


def statuts(ip, port):
    url = f"https://minecraft-api.com/api/ping/status/{ip}/{port}"
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        webpage = urlopen(request_site).read()
        print(webpage)
        return webpage
    except HTTPError as e:
        x = e.read()
        print(x)
        return x