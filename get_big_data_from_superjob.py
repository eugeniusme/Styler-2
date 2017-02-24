import requests
import json

def get_api_from_superjob(api):
    header = {'X-Api-App-Id': api}
    try:
        parametrs = {'count':1, 'catalogue_id':48}
        reqest = requests.get('https://api.superjob.ru/2.0/%s' % api, headers=header, params=parametrs)
    except KeyError:
        print('Api key is wrong')
        return {}
    return header

def get_data_from_superjob(object_of_search, count, header):
    parametrs = {'keyword' : 'программист', 'town': 'Москва', 
                 'count': count, 'no_agreement': 1}
    return requests.get('https://api.superjob.ru/2.0/%s' % object_of_search, headers=header, params=parametrs)

def save_in_file(data):
    file_title = 'vacancies.json'
    with open(file_title, mode='w', encoding='utf-8') as file:
        json.dump(data, file)
 
if __name__ == '__main__':
    api_key = input('Please, input your api key:')
    header = get_api_from_superjob(api_key)
    if header is not None:
        object_of_search = 'vacancies'
        count = 100
        data = get_data_from_superjob(object_of_search, count, header).json()
        save_in_file(data)
