# Домашнее задание к занятию "`Создание REST API на FastApi часть 1`" - `Дёмин Максим`


### Задание 1

Что нужно сделать:

Вам нужно написать на fastapi и докеризировать сервис объявлений купли/продажи.

У объявлений должны быть следующие поля:

заголовок

описание

цена

автор

дата создания

Должны быть реализованы следующе методы:

Создание: POST /advertisement

Обновление: PATCH /advertisement/{advertisement_id}

Удаление: DELETE /advertisement/{advertisement_id}

Получение по id: GET  /advertisement/{advertisement_id}

Поиск по полям: GET /advertisement?{query_string}

Авторизацию и аутентификацию реализовывать не нужно

### Решение:
Запускаем в docker
```
docker compose up --build
```
<img width="1719" height="740" alt="inst" src="https://github.com/user-attachments/assets/4383e02c-ec46-41fa-a8e5-db894af2b663" />

После запуска сервис будет доступен на:
```
http://localhost:8000
```

Интерактивная документация:
```
http://localhost:8000/docs
```
Примеры запросов
Создание объявления
```
curl -X POST "http://localhost:8000/advertisement" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Сделаю домашку",        
    "description": "Сделаю свою домашку, быстро и качественно",
    "price": 3500000,
    "author": "Максим"
  }'
```
<img width="1554" height="261" alt="add" src="https://github.com/user-attachments/assets/97c0206e-be60-45e8-894a-aca98c6566f7" />

Получение по id
```
curl "http://localhost:8000/advertisement/1"
```
Обновление объявления
```
curl -X PATCH "http://localhost:8000/advertisement/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 32000,
    "description": "Сделаю свою домашку, быстро и качественно, торг не уместен, только хардкор"
 }'
```
<img width="1841" height="218" alt="re" src="https://github.com/user-attachments/assets/ef8c9438-b97c-4342-b3db-bd57e9fc47e3" />

Удаление объявления
```
curl -X DELETE "http://localhost:8000/advertisement/1"
```
<img width="1129" height="90" alt="del" src="https://github.com/user-attachments/assets/d496341c-f1b9-4642-a890-aa9ca2f7caa3" />

Поиск по полям

По автору
```
curl --get "http://localhost:8000/advertisement" \
  --data-urlencode "author=Максим"
```
По заголовку
```
curl --get "http://localhost:8000/advertisement" \
  --data-urlencode "title=домашку"
```
По диапазону цены
```
curl "http://localhost:8000/advertisement?min_price=10000&max_price=50000"
```
Комбинированный поиск
```
curl --get "http://localhost:8000/advertisement" \
  --data-urlencode "author=Максим" \
  --data-urlencode "title=домашку" \
  --data-urlencode "min_price=10000" \
  --data-urlencode "max_price=40000"
```

<img width="1849" height="207" alt="search" src="https://github.com/user-attachments/assets/40896452-74da-46cc-b24b-5834cca6c942" />
<img width="1849" height="207" alt="search2" src="https://github.com/user-attachments/assets/0da3fbe0-422a-45cb-8345-d3ad5932f77d" />

