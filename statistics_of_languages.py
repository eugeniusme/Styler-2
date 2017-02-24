import json

def open_file_with_big_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.loads(file.read())['objects']
    except FileNotFoundError:
        print('Sorry, this file wasn\'t found')
        data = []
    return data

def make_statistics(data):
    languages_statistics = []
    languages_titles = {'C', 'C++', 'C#', 'PHP', 'Python', 'Java', 'JavaScript', 'Pascal', 'SQL', 'HTML', 'Matlab',
                        'Basic', 'Assembler', 'R', 'Ruby', 'Lisp'}
    for language in languages_titles:
        lst = ['', 0, 0]
        lst[0] = language
        languages_statistics.append(lst)
    
    for one_info in data:
        for language in languages_statistics:
            if one_info['candidat'].find(language[0]) != -1:
                language[1] += one_info['payment_to']
                language[2] += 1

if __name__ == '__main__':
    filename = 'vacancies.json'
    data = open_file_with_big_data(filename)
    stats = make_statistics(data)
    
    for one_language in languages_statistics:
        if one_language[2] != 0:
            print('Information about: %s \nNumber of vacancies: %d\nAverage salary: %d\n' %(one_language[0], 
                                                                                            one_language[2], 
                                                                                            one_language[1]/one_language[2]))
