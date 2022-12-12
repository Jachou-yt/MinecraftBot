from urllib.error import HTTPError
from urllib.request import Request, urlopen


def request_site(url):
    return Request(url, headers={"User-Agent": "Mozilla/5.0"})


def statuts(ip, port):
    url = f"https://minecraft-api.com/api/ping/status/{ip}/{port}"
    try:
        webpage = urlopen(request_site(url)).read()
        print(webpage)
        return webpage
    except HTTPError as e:
        x = e.read()
        print(x)
        return x


def player_to_uuid(player_name):
    url = f"https://minecraft-api.com/api/uuid/{player_name}/json"
    try:
        webpage = urlopen(request_site(url)).read()
        print(webpage)
        return webpage
    except HTTPError as e:
        x = e.read()
        print(x)
        return x


def uuid_to_player(uuid):
    url = f"https://minecraft-api.com/api/pseudo/{uuid}/json"
    try:
        webpage = urlopen(request_site(url)).read()
        print(webpage)
        return webpage
    except HTTPError as e:
        x = e.read()
        print(x)
        return x