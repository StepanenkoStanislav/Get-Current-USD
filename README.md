
# Проект Get-Current-USD

## Описание проекта
Проект отображает актуальный курс доллара к рублю по адресу /get-current-usd/ в формате json.
Дополнительно показываются 10 последних запросов. Запросы кэшируются, пауза между запросами 10 секунд.

## Запуск проекта с помощью Docker
В корневой директории проекта необходимо создать файл `".env"`, в котором необходимо указать SECRET_KEY. Пример находится в файле `example.env`
```python
# В корневой директории проекта
docker-compose up --build
```

После запуска проекта, посмотреть текущий курс доллара можно по адресу http://127.0.0.1:8000/get-current-usd/

## Технологии

<div>
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="python" alt="python" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" title="django" alt="django" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original.svg" title="docker" alt="docker" width="40" height="40"/>&nbsp
  <img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original.svg" title="redis" alt="redis" width="40" height="40"/>&nbsp
</div>

В проекте используются следующие технологии:
- python 3.9
- Django 4.0
- Redis 5.0.1
- Docker 20.10.24


## Автор

[Степаненко Станислав](https://t.me/tme_zoom)

[![Telegram Badge](https://img.shields.io/badge/StepanenkoStanislav-blue?logo=telegram&logoColor=white)](https://t.me/tme_zoom) [![Gmail Badge](https://img.shields.io/badge/-Gmail-red?style=flat&logo=Gmail&logoColor=white)](mailto:stepanenko.s.a.dev@gmail.com)
