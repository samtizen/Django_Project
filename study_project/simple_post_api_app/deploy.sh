pip install djangorestframework

pip install django-cors-headers

python manage.py makemigrations simple_post_api_app

python manage.py migrate simple_post_api_app

python manage.py runserver

http://127.0.0.1:8000/simple-post-api/api/v1/

sudo apt install httpie

1. Регистрация пользователя

http --print HBhb POST 127.0.0.1:8000/simple-post-api/api/v1/sign-up/ username=user1 password=1 first_name=ivan last_name=ivanov email=ivan@ivanov.ru

Запрос

POST /simple-post-api/api/v1/sign-up/ HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 110
Content-Type: application/json
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

{
    "email": "ivan@ivanov.ru",
    "first_name": "ivan",
    "last_name": "ivanov",
    "password": "1",
    "username": "user1"
}

Ответ

HTTP/1.1 200 OK
Allow: OPTIONS, POST
Content-Language: en
Content-Length: 15
Content-Type: application/json
Date: Mon, 21 May 2018 17:22:01 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

{
    "status": "OK"
}

2. Аутентификация

http --print HBhb POST 127.0.0.1:8000/simple-post-api/api/v1/sign-in/ username=user1 password=1

Запрос

POST /simple-post-api/api/v1/sign-in/ HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 38
Content-Type: application/json
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

{
    "password": "1",
    "username": "user1"
}

Ответ

HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Language: en
Content-Length: 52
Content-Type: application/json
Date: Mon, 21 May 2018 17:24:47 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

{
    "token": "c20eece335018fbaae2c91427d60d6e55351c5a7"
}

3. Создание заметки

http --print HBhb POST 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7" header="my post" content="content of my post" location=Москва

Запрос

POST /simple-post-api/api/v1/simple-posts/ HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Authorization:  Token c20eece335018fbaae2c91427d60d6e55351c5a7
Connection: keep-alive
Content-Length: 106
Content-Type: application/json
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

{
    "content": "content of my post",
    "header": "my post",
    "location": "Москва"
}

Ответ

HTTP/1.1 201 Created
Allow: GET, OPTIONS, POST
Content-Language: en
Content-Length: 164
Content-Type: application/json
Date: Mon, 21 May 2018 17:31:47 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

{
    "content": "content of my post",
    "created": "2018-05-21T17:31:47.799488Z",
    "header": "my post",
    "id": 1,
    "location": "Москва",
    "updated": "2018-05-21T17:31:47.799557Z"
}

4. Список заметок

http --print HBhb GET 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7"

Запрос

GET /simple-post-api/api/v1/simple-posts/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token c20eece335018fbaae2c91427d60d6e55351c5a7
Connection: keep-alive
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

Ответ

HTTP/1.1 200 OK
Allow: GET, OPTIONS, POST
Content-Language: en
Content-Length: 335
Content-Type: application/json
Date: Mon, 21 May 2018 17:33:57 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "content": "content of my post",
        "created": "2018-05-21T17:31:47.799488Z",
        "header": "my post",
        "id": 1,
        "location": "Москва",
        "updated": "2018-05-21T17:31:47.799557Z"
    },
    {
        "content": "content of my post 2",
        "created": "2018-05-21T17:33:53.806552Z",
        "header": "my post 2",
        "id": 2,
        "location": "Москва",
        "updated": "2018-05-21T17:33:53.806591Z"
    }
]

5. Детали заметки

http --print HBhb GET 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/2/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7"

Запрос

GET /simple-post-api/api/v1/simple-posts/2/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token c20eece335018fbaae2c91427d60d6e55351c5a7
Connection: keep-alive
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

Ответ

HTTP/1.1 200 OK
Allow: GET, OPTIONS, PUT, DELETE
Content-Language: en
Content-Length: 168
Content-Type: application/json
Date: Mon, 21 May 2018 17:36:03 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

{
    "content": "content of my post 2",
    "created": "2018-05-21T17:33:53.806552Z",
    "header": "my post 2",
    "id": 2,
    "location": "Москва",
    "updated": "2018-05-21T17:33:53.806591Z"
}

6. Изменение заметки

http --print HBhb PUT 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/2/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7" id=2 header="my post new" content="new content" location="Москва"

Запрос

PUT /simple-post-api/api/v1/simple-posts/2/ HTTP/1.1
Accept: application/json
Accept-Encoding: gzip, deflate
Authorization:  Token c20eece335018fbaae2c91427d60d6e55351c5a7
Connection: keep-alive
Content-Length: 114
Content-Type: application/json
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

{
    "content": "new content",
    "header": "my post new",
    "id": "2",
    "location": "Москва"
}

Ответ

HTTP/1.1 200 OK
Allow: GET, OPTIONS, PUT, DELETE
Content-Language: en
Content-Length: 0
Date: Mon, 21 May 2018 17:37:54 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

Проверка

http --print HBhb GET 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/2/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7"

Ответ

HTTP/1.1 200 OK
Allow: GET, OPTIONS, PUT, DELETE
Content-Language: en
Content-Length: 161
Content-Type: application/json
Date: Mon, 21 May 2018 17:39:16 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

{
    "content": "new content",
    "created": "2018-05-21T17:33:53.806552Z",
    "header": "my post new",
    "id": 2,
    "location": "Москва",
    "updated": "2018-05-21T17:37:54.336294Z"
}

7. Удаление поста

http --print HBhb DELETE 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/2/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7"

Запрос
DELETE /simple-post-api/api/v1/simple-posts/2/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Authorization:  Token c20eece335018fbaae2c91427d60d6e55351c5a7
Connection: keep-alive
Content-Length: 0
Host: 127.0.0.1:8000
User-Agent: HTTPie/0.9.2

Ответ

HTTP/1.1 204 No Content
Allow: GET, OPTIONS, PUT, DELETE
Content-Language: en
Content-Length: 0
Date: Mon, 21 May 2018 17:40:58 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

Проверка

http --print HBhb GET 127.0.0.1:8000/simple-post-api/api/v1/simple-posts/ "Authorization: Token c20eece335018fbaae2c91427d60d6e55351c5a7"

Ответ

HTTP/1.1 200 OK
Allow: GET, OPTIONS, POST
Content-Language: en
Content-Length: 166
Content-Type: application/json
Date: Mon, 21 May 2018 17:41:30 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Accept-Language, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "content": "content of my post",
        "created": "2018-05-21T17:31:47.799488Z",
        "header": "my post",
        "id": 1,
        "location": "Москва",
        "updated": "2018-05-21T17:31:47.799557Z"
    }
]
