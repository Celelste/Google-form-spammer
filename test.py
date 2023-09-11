from form_requests import get_fields
from requests import post

link = 'https://docs.google.com/forms/d/e/1FAIpQLScC_1y31mRUfJLKDBtK100WMzFTwJHdtqCuHdA41rnasIWG9A/viewform?usp=sf_link'

fields = get_fields(link)
fields.pop('title')
fields.pop('desc')

link = fields['link']
fields['response'] = []

for item in fields['items']:
    _id = item['id']
    question = item['question']
    if len(item['options']) != 0:
        for idx, option in enumerate(item['options']):
            option = option['option']
            print(f'{idx}: {option}')
        response = int(input(f'{question}\n: '))
        while not (0 < response <= len(item['options'])):
            response = int(input(f'{question}\n: '))

        response = item['options'][response - 1]['option']
    else:
        response = input(f'{question}\n: ')
    fields['response'].append({'id': _id, 'response': response})

link = f'https://docs.google.com/forms/d/e/{fields["link"].split("/")[6]}/formResponse'

data = {}
for response in fields['response']:
    data[response['id']] = response['response']

post(link, data=data)
