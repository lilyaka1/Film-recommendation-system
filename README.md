Наша команда представляет решение поставленной задачи на языке программирования Python.
В папке Recommendatiom system находятся файлы: config.py, database.py, start.py, system.py, uni_recomend.py и user_indentificate.py. 


Вспомогательные файлы:
1. config.py является конфигом с заданными значиями определённых параметров, от которых зависит вывод всего скрипта. Смысл того или иного параметра расписан также в самой конфигурации.
2. database.py - совокупность баз данных, которые хранят в себе определённые значения. Например, скрипт может брать ту или иную информацию либо о пользователе, либо о фильме из database.py.
3. system.py содержит в себе дополнительные функции для рассчёта коэффицентов релевантностей и по отсеиванию жанров для рекомендации.

Основные файлы:
1. user_indentificate.py - в данной секции скрипта происходит авторизация пользователя и полный сбор информации о нём, включающей в себя просмотренные фильмы, поставленные к ним рейтиги, учитывая дату и тому подобное. На основе этого происходит сортирование любимых жанров в порядке убывания относильно значения релевантности и других не менее важных факторов.
2. uni_recomend.py - заключительная часть скрипта, в которой расписан итоговый алгоритм рекомендательной системы. В нём (в скрипте) сортируется список всех фильмов из файла movies.csv в порядке убывания относительно среднего рейтинга, среднего значения TimeStamps (с англ. временная метка) и количества оценок к данному фильму. После этого происходят определённые вычисления для алгоритма рекомендации фильмов, учитывая все параметры из config.py. Более подробный принцип работы можно расписан в самом файле (см. строчку 110). 

Как запустить файл?
1. Важно в config.py указать пути к movies.csv и ratings.csv.
2. Запустить файл start.py

P.S. Так как изначальная база данных с пользователями была очень объёмной и её обработка занимала немало времени, было принято решение сократить её до 100.000 строчек. В нашем случае это файл ratings_A.csv
