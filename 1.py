import requests

person = ['Hulk', 'Captain America', 'Thanos']
person_dict = {}

def find_name():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url).json()
    for info in resp:
        if info['name'] in person:
            person_dict[info['name']] = info['powerstats']['intelligence']

    print(max(person_dict))

find_name()

