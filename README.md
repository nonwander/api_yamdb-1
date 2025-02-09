# API YaMDb (Django Rest Framework)

Проект YaMDb представляет собой блог-платформу для сбора отзывов пользователей на ресурсы медиатеки, обращение к ресурсам выполняется посредством запросов к API проекта.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
<br /> Проект создавался для практики создания сервиса API в команде, синхронизируясь через Git.
##
Проект YaMDb включает в себя основные приложения: <br />
• .api — модели, view, эндпойнты для отзывов (Review) и комментариев (Comments), права доступа для запросов к ресурсам; определение средней оценки произведения;<br />
• .api_users_auth — система регистрации и аутентификации, определение прав доступа, работа с токеном, система подтверждения по e-mail;<br />
• .titles — модели, view и эндпойнты для категорий (Categories), жанров (Genres) и произведениий (Titles).<br />
##
Для API проекта YaMDb доступны ресурсы:<br />
    • Ресурс AUTH: аутентификация.<br />
    • Ресурс USERS: пользователи.<br />
    • Ресурс TITLES: произведения, к которым пишут отзывы (определённый фильм, книга или песня).<br />
    • Ресурс CATEGORIES: категории (типы) произведений («Фильмы», «Книги», «Музыка»).<br />
    • Ресурс GENRES: жанры произведений; одно произведение может быть привязано к нескольким жанрам.<br />
    • Ресурс REVIEWS: отзывы на произведения; отзыв привязан к определённому произведению.<br />
    • Ресурс COMMENTS: комментарии к отзывам; комментарий привязан к определённому отзыву.<br />
    
Полная документация API YaMDb хранится в *Redoc*, также будет доступна на локальной машине после запуска проекта по адресу:
http://localhost:8000/redoc/
___

## Установка.

### Cистемные требования и технологии:
    python==3.8.6
    Django==3.0.5
    djangorestframework==3.11.0
    djangorestframework-simplejwt==4.6.0
    PyJWT==2.1.0

### Порядок установки:
1) Клонировать репозиторий
2) Установить зависимости из requirements.txt
3) Запустить проект

```python
git clone https://github.com/nonwander/api_yamdb-1
pip install -r requirements.txt
python manage.py runserver
```
В завершении установки, перед тем, как развернуть проект, необходио создать профиль администратора сети YaMDb:
```python
python manage.py createsuperuser
```

### Особенности.
Проект не имеет части Frontend.<br />
Проект запускается сервере разработчика Django на «внутреннем» IP-адресе 127.0.0.1 на порте 8000.<br />
Проект хранит данные в предустановленной базе SQLite.<br />

### Перспективные доработки проекта.
В проекте не предусмотрено использование переменных окружения.<br />
В перспективе вынести из *.api_yamdb/settings.py* переменную *ADMIN_EMAIL*, на данный момент являющейся системной константой.

### Примеры запросов к API.

Запросы к API начинаются с «/api/v1/»

1) Получение JWT-токена в обмен на *email* и *confirmation_code*:
<br /> (content type: aplication/json)

POST-запрос: auth/token/
<br /> *Request sample:*
```python
{
    «email»: «string»,
    «conformation_code»: «string»
}
```
*Response sample (200):*
```python
{
    «token»: «string»
}
```
*Response sample (400):*
```python
{
    «field_name»: [
      «string»
    ]
}
```
2) Отправление __confirmation_code__ на переданный *email*:
<br />POST-запрос:  auth/email/
```python
{
    «email»: «string»
}
```

### <br /> Авторы проекта:
Немыкин Евгений — приложение «api_users_auth»;<br />
Тимофей Тарасов — приложение «api»;<br />
Никита Максимов — приложение «titles».
