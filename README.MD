# LOAD TEST apache superset

Проект нагрузки для superset

#### Стэк
- язык программирования - [Python 3.8](https://www.python.org/downloads/)
- фреймворк нагрузки - [locust](https://locust.io/)

#### Структура
```bash
.
├── core
│   ├── api                 # описание api-классов
│   ├── data                # тестовые данные
├── locustfile.py             # нагрузка 
└── requirements.txt        # подключение внешних библиотек
```
