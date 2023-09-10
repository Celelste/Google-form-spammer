import requests
import random
from bs4 import BeautifulSoup
from faker import Faker
import json
import ast

fake = Faker('en_IN')


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


def faker_input(_type):
    if _type == "name":
        return fake.name()
    if _type == "number":
        return '9' + fake.msisdn()[4:]
    if _type == "word":
        return fake.word()
    if _type == "sentence":
        return fake.sentence()
    if _type == "email":
        return fake.email()
    else:
        return _type


def prepare_payload(response):
    fields = ast.literal_eval(response['fields'])
    link = "https://docs.google.com/forms/d/e/{}/formResponse".format(fields['link'].split("/")[6])
    response['fields'] = fields['items']
    response['link'] = link
    response.pop("submit", None)

    return response


def parse_payload(payload):

    fields = payload['fields']
    items = {}

    for field in fields:
        options_list = []
        for option in field['options']:
            if not option['type']:
                options_list.append(option['option'])
        items[field['id']] = options_list

    parsed_payload = {}

    for key, value in payload.items():
        if value.startswith("!cgpa."):
            parsed_payload[key] = str(random.randrange(int(value[6:]) * 10, 100, 1) / 10)
        elif value.startswith("!roll."):
            parsed_payload[key] = value[6:] + str(random.randrange(10000, 99999, 1))
        elif value.startswith("!fake."):
            parsed_payload[key] = faker_input(value[6:])
        elif value == "!random":
            parsed_payload[key] = random.choice(items[key])
        else:
            parsed_payload[key] = value
    return parsed_payload, payload['link'], payload['num']
