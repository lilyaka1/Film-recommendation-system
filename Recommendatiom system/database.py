import csv
import config

existedUsers = {
    
    
}
existedMovies = {

}

analyzedstrings = 0

with open(config.path_to_users, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0

    for row in file_reader:
        if count == 0:
            if config.debug == True:
                print(f'Файл содержит столбцы: {", ".join(row)}')
            print("Идёт анализ пользователей базы данных... Подождите немного.")
        else:
            if row[0] not in existedUsers:
                existedUsers[row[0]] = {
                'movieIds': [],
                'raitings': [],
                'movieGengres': '',
                'raitingGengres': '',

            }

            existedUsers[row[0]]['movieIds'].append(row[1])
            existedUsers[row[0]]['raitings'].append(row[2])
        count += 1
        if count % 10000 == 0 and config.debug == True:
            analyzedstrings += 100000
            print(f'Проанализировано {analyzedstrings} строк')
    if config.debug == True:
        print(f'Всего в файле {count} строк.')
        # print(f'Найдены пользователи с id от {userIds[0]} до {userIds[-1]}')


with open(config.path_to_movies, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count_1 = 0 #считает количество строк в .csv
    for row in file_reader:
        if count_1 == 0:
            if config.debug == True:
                print(f'Файл movies.csv содержит столбцы: {", ".join(row)}')
        else:
            year = row[1][-5] + row[1][-4] + row[1][-3] + row[1][-2] if row[1][-1] == ')' else 0000
            existedMovies[row[0]] = {
                'title' : row[1],
                'gengre' : [row[2].split("|")],
                'year' : year
            }



        count_1 += 1

if config.debug == True:
    print(f'Всего в файле {count_1} строк.\n')


