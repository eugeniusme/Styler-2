import json

def open_file_with_big_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.loads(file.read())['objects']
    except FileNotFoundError:
        print('Sorry, this file wasn\'t found')
        data = []
    return data

def make_new_data(data):
    edit_data = []
    required_information = {'payment', 'payment_to', 'payment_from', 'candidat', 'profession', 'education', 
                            'experience', 'languages', 'age_from', 'age_to', 'gender'}
    for vacancy in data:
        data_of_one_vacancy = dict()
        for required_data in diction:
            data_of_one_vacancy[required_data] = vacancy[required_data]
        edit_data.append(data_of_one_vacancy)
    return edit_data
    
def save_in_file(data):
    new_file_title = 'new_vacancies.json'
    with open(new_file_title, mode='w', encoding='utf-8') as file:
        json.dump(data, file)
    print('New file was created')

if __name__ == '__main__':
    #file_title = 'vacancies.json'
    file_title = input('Please input title of file')
    data = open_file_with_big_data(file_title)
    if data is not None:
        new_data = make_new_data(data)
        save_in_file(new_data)
