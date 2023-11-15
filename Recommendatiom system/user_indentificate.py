import database
import config
import math

uniqueGenres = {
}
raitingGenres = {
}
averageRaitings = {
}
averageGengreYears = {
}

while True:
    userId = input('Введите ваш UserId: ')

    if userId in database.existedUsers:
        print('Успешный вход!')
        break
    else:
        print('Такой UserId найдено не было!')
        continue

userInfo = {
    userId : {
        'movieIds' : database.existedUsers[userId]['movieIds'],
        'raitings' : database.existedUsers[userId]['raitings'],
        'movieGengres' : '',
        'raitingGengres' : '',
    },

}

for action in "first", "second", "third", 'fourth':
    for number, MovieId in enumerate(userInfo[userId]['movieIds']):
        if action == 'first':
            for gengres in database.existedMovies[str(MovieId)]["gengre"]:
                for gengre in gengres:
                    raitingGenres[str(gengre)] = 0 #добавляем счётчик рейтинга для жанров
                    uniqueGenres[str(gengre)] = {
                        'count' : 0, #добавляем все уникальные жанры, которые просмотрел пользователь
                        'new_century' : [], #сюда будем добавлять годы просмотренных фильмов 21-го века
                        'old_century' : [], #сюда будем добавлять годы просмотренных фильмов 20-го века
                        'count_NC' : 0,
                        'count_OC' : 0,
                        'average_NC' : 0,
                        'average_OC' : 0
                    }
        elif action == 'second':
            for gengres in database.existedMovies[str(MovieId)]["gengre"]:
                for gengre in gengres:
                    uniqueGenres[str(gengre)]['count'] += 1 #считаем количество того или иного просмотренного жанра
        elif action == 'third':
            raiting = userInfo[userId]['raitings'][number] #вытаскиваем поставленный рейтинг к фильму от данного пользователя
            for gengres in database.existedMovies[str(MovieId)]['gengre']:
                for gengre in gengres:
                    raitingGenres[str(gengre)] += float(raiting) #добавляем к тому или иному жанру рейтинг этого пользователя
        elif action == 'fourth':
            raiting = userInfo[userId]['raitings'][number]
            for gengres in database.existedMovies[str(MovieId)]['gengre']:
                for gengre in gengres:
                    if float(raiting) >= 3.0:
                        if int(database.existedMovies[str(MovieId)]['year']) >= 2000:
                            uniqueGenres[str(gengre)]['new_century'].append(int(database.existedMovies[str(MovieId)]['year']))
                        else:
                            uniqueGenres[str(gengre)]['old_century'].append(int(database.existedMovies[str(MovieId)]['year']))


#Искали средние значения годов 21-ого и 20-ого веков
for key, values in uniqueGenres.items():
    try:
        uniqueGenres[key]['average_NC'] = math.floor(sum(values['new_century']) / len(values['new_century']))
        uniqueGenres[key]['count_NC'] = len(values['new_century'])
    except ZeroDivisionError:
        pass

    try:
        uniqueGenres[key]['average_OC'] = math.floor(sum(values['old_century']) / len(values['old_century']))
        uniqueGenres[key]['count_OC'] = len(values['old_century'])
    except ZeroDivisionError:
        pass

for key, values in uniqueGenres.items():
    averageGengreYears[key] = [values['average_NC'], values['average_OC']]

for genres in uniqueGenres:
    raiting = raitingGenres[genres]
    count = uniqueGenres[genres]['count']
    averageRaiting = raiting / count #ищем средний рейтинг определённого жанра
    averageRaitings[str(genres)] = averageRaiting #записываем его (рейтинг) в нашу БД (словарь)

#записываем информацию в пользователя
userInfo[userId]["raitingGengres"] = raitingGenres
userInfo[userId]["movieGengres"] = uniqueGenres
userInfo[userId]["averageRaitings"] = averageRaitings
gengresInformation = userInfo[userId]['averageRaitings']

SortedGengers = list(sorted(gengresInformation.items(), key=lambda x: x[1], reverse=True))

import system

topSortedGengres = {
}
type_of_films = []
quantity_of_films = []

count = 0
maxcoff = 0.0

for n, gengre in enumerate(SortedGengers):
    if config.debug == True:
        print(f'{n+1}. Жанр: {gengre[0]} | Средний рейтинг: {gengre[1]} | Коэффициент: {system.coff(gengre[1])}')
    maxcoff = max(maxcoff, system.coff(gengre[1]))
    if (maxcoff - config.r) <= system.coff(gengre[1]) <= maxcoff:
        count += 1

count_of_topCheckedGengers = system.check(count) #с помощью этого отбираем количество топовых жанров.

for gengre in SortedGengers:
    if count_of_topCheckedGengers == 0:
        break
    topSortedGengres[str(gengre[0])] = system.coff(gengre[1])
    type_of_films.append(str(gengre[0]))
    quantity_of_films.append(0)
    count_of_topCheckedGengers -= 1

n = config.n

while n > 0:
    for index in range(len(quantity_of_films)):
        if n <= 0:
            break
        quantity_of_films[index] += 1
        n -= 1



