# Styler-2


# get_big_data_from_superjob.py
Скрипт скачивает с сайта Superjob информацию о 100 вакансий программистов и сохраняет в файл.

Входные данные: API ключ.

Выходные данные: файл с информацией о сотне вакансий.


# edit_data.py
Скрипт обрабатывает информацию о вакансиях, которая была скачана с Superjob. Остаются следующие параметры: название, зарплата и требования (образование, возраст и т.д.).

Входные данные: файл с полной информацией о вакансиях (из предыдущего скрипта).

Выходные данные: файл с обработанной информацией о вакансиях (название, зарплата и требования).


# statistics_of_languages.py
Скрипт анализирует собранную информацию о вакансиях следующим образом: считает количество вакансий для каждого языка программирования и среднюю зарплату для них.

Входные данные: файл с информацией о вакансиях. 

Выходные данные: Количество вакансий и средняя зарплата для каждого языка программирования.

Information about: PHP 
Number of vacancies: 10
Average salary: 36500

Information about: SQL 
Number of vacancies: 32
Average salary: 64218

Information about: JavaScript 
Number of vacancies: 9
Average salary: 49444

Information about: HTML 
Number of vacancies: 14
Average salary: 46785

Information about: C 
Number of vacancies: 40
Average salary: 59187

Information about: C++ 
Number of vacancies: 3
Average salary: 86666

Information about: Java 
Number of vacancies: 14
Average salary: 56428

Information about: C# 
Number of vacancies: 5
Average salary: 22000

Information about: R 
Number of vacancies: 20
Average salary: 65750

Information about: Python 
Number of vacancies: 3
Average salary: 58333
