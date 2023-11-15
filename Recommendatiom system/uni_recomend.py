import csv
import config
import user_indentificate
print('Добро пожаловать!')

films = {

}

with open(config.path_to_movies, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    count_1 = 0 #считает количество строк в .csv
    for row in file_reader:
        if count_1 == 0:
            if config.debug == True:
                print(f'Файл movies.csv содержит столбцы: {", ".join(row)}')
        else:
            films[row[0]] = {
                'title' : row[1],
                'gengre' : ([row[2].split("|")]),
                'year' : 0000,
                "count": 0,
                "sum_of_all_ratings": 0,
                'average_rating': 0.0,
                "sum_of_all_timestamps" : 0,
                'average_timestamp' : 0.0
            }
        count_1 += 1
if config.debug == True:
    print(f'Всего в файле {count_1} строк.\n')

userIds = [] #будущая идея - чекать future_idea.txt и config.py

with open(config.path_to_users, encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count_2 = 0
    for row in file_reader:
        if count_2 == 0:
            if config.debug == True:
                print(f'Файл ratings.csv содержит столбцы: {", ".join(row)}')
        else:

            movieId = row[1]
            userRating = row[2]
            TimeStamp = row[3]

            films[movieId]['count'] += 1
            films[movieId]['sum_of_all_ratings'] += float(userRating)
            films[movieId]['sum_of_all_timestamps'] += int(TimeStamp)
        count_2 += 1
if config.debug == True:
    print(f'\nВсего в файле {count_2} строк.')

for key, values in films.items():
    try:
        films[key]['average_rating'] = float(values['sum_of_all_ratings'] / values['count'])
        films[key]['average_timestamp'] = float(values['sum_of_all_timestamps'] / values['count'])

        title = films[key]['title']
        reversed_title = title[::-1]
        year = reversed_title[4] + reversed_title[3] + reversed_title[2] + reversed_title[1] if reversed_title[0] == ')' else 0000
        films[key]['year'] = year
    except ZeroDivisionError:
        pass

top_films = dict(sorted(films.items(), key=lambda x: (x[1]['average_rating'], x[1]['average_timestamp'], x[1]['count']), reverse=True))

general_n = 0
ids = []
ratings = []
votes = []
years = []
gengres = []

for key, values in top_films.items():
    if general_n == config.general_n:
        break
    if values['count'] >= config.Quantity_of_Votes_of_Recommendation and config.start_year <= int(values['year']) <= config.end_year:
        ids.append(values['title'][:-7])
        ratings.append(round(values['average_rating'], 1))
        votes.append(values['count'])
        years.append(values['year'])
        gengres.extend(values['gengre'])
        general_n += 1

try:
    if votes or ids or ratings:
        print(f'Топ актуальных фильмов: ')
        if config.debug == True:
            print(f'CONFIG SETTINGS:\nQuantity_of_Votes_of_Recommendation = {config.Quantity_of_Votes_of_Recommendation}\nstart_year = {config.start_year}\nend_year = {config.end_year}\ngeneral_n = {general_n}')
        for number in range(config.general_n):
            print(f'{number+1}. {ids[number]} | Жанр: {", ".join(str(n) for n in (gengres[number]))} | Год: {years[number]} | Рейтинг: {ratings[number]} | Количество оценок: {votes[number]}')
    else:
        print("По заданной конфигурации не было найдено ни одного подходящего фильма!")
except IndexError:
    print('Больше фильмов не было найдено!')

if config.debug == True:
    print('\n')
    print(user_indentificate.topSortedGengres)
    print(user_indentificate.quantity_of_films)
    print(user_indentificate.type_of_films)

n = config.n

numeration = 1
haverecommended = []

print(f'\nСегодня мы можем порекомендовать Вам такие фильмы как: ')
#принцип работы алгоритма рекомендательной системы:
#1 условие: чтобы фильм был в предпочетаемом жанре; пользователь его не смотрел; количество оценок данного фильма больше значения, установленного в конфиге. Если всё подошло по условиям, запомним данный фильм, чтобы случайно система не прорекомендовала его ещё раз.
#2 условие: если количество современных фильмов, которые понравились пользователю, больше, чем количества старых фильмов, то выполняем #3 условие, иначе #4 условие
#3 условие: если год фильма находится в промежутке [среднее_значение_годов_современных_фильмов_данного_жанра - параметр_p; среднее_значение_годов_современных_фильмов_данного_жанра + параметр_p], то фильм нам подходит, иначе нет.
#3 условие: если год фильма находится в промежутке [среднее_значение_годов_старых_фильмов_данного_жанра - параметр_p; среднее_значение_годов_старых_фильмов_данного_жанра + параметр_p], то фильм нам подходит, иначе нет.
for count in range(len(user_indentificate.quantity_of_films)):
        for key, values in top_films.items():
            if user_indentificate.type_of_films[count] in top_films[key]['gengre'][0] and key not in user_indentificate.userInfo[user_indentificate.userId]['raitings'] and values['count'] >= config.Personal_Quantity_of_Votes_of_Recommendation and key not in haverecommended:
                if user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['count_NC'] >= user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['count_OC']:
                    if user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['average_NC'] - config.p <= int(top_films[key]['year']) <= user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['average_NC'] + config.p:
                        user_indentificate.quantity_of_films[count] -= 1
                        print(f"{numeration}. {top_films[key]['title']} | Жанр(-ы): {', '.join(top_films[key]['gengre'][0])} | Рейтинг: {round(top_films[key]['average_rating'], 2)}")
                        print(f"Потому что вы интересовались современными фильмами жанра: {user_indentificate.type_of_films[count].lower()}")
                        if config.debug == True:
                            print(f'Значение (коэффицент) релевантности: {user_indentificate.topSortedGengres[user_indentificate.type_of_films[count]]}')
                        haverecommended.append(key)
                        numeration += 1
                else:
                    if user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['average_OC'] - config.p <= int(top_films[key]['year']) <= user_indentificate.uniqueGenres[user_indentificate.type_of_films[count]]['average_OC'] + config.p:
                        user_indentificate.quantity_of_films[count] -= 1
                        print(f"{numeration}. {top_films[key]['title']} | Жанр(-ы): {', '.join(top_films[key]['gengre'][0])} | Рейтинг: {round(top_films[key]['average_rating'], 2)}")
                        print(f"Потому что вы интересовались старыми фильмами жанра: {user_indentificate.type_of_films[count].lower()}")
                        if config.debug == True:
                            print(f'Значение (коэффицент) релевантности: {user_indentificate.topSortedGengres[user_indentificate.type_of_films[count]]}')
                        haverecommended.append(key)
                        numeration += 1
            if user_indentificate.quantity_of_films[count] == 0:
                break
print(f'\nДанные рекомендации были составлены на основе ваших предпочтений. Больше всего вы интересовались фильмами в жанре(-ах): {", ".join(str(i).lower() for i in user_indentificate.type_of_films)}')


