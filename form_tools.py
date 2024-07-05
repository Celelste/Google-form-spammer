import requests
from bs4 import BeautifulSoup
import json


def get_soup(link):
    req = requests.get(link)
    html = req.content
    soup = BeautifulSoup(html, "html.parser")
    return soup


def get_fields(link):
    soup = get_soup(link)
    data = soup.findAll("script", {"nonce": True})[3].string
    data = json.loads(data[27:-1])[1]
    # pprint(data)
    title = data[-9]
    desc = data[0]
    items = []
    for item in data[1]:
        try:
            _id = "entry." + str(item[4][0][0])
            question = item[1]
            _type = item[3]
            if item[4][0][2] == 1:
                req = "required"
            else:
                req = ""
            options = []
            if _type in [2, 3, 4]:
                for option in item[4][0][1]:
                    options.append({"option": option[0], "type": option[4]})
            items.append({"id": _id, "question": question, "type": _type, "req": req, "options": options})
        except:
            pass
    return {"title": title, "desc": desc, "items": items, "link": link}
