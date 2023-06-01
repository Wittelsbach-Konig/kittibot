# kittibot
Kitti telegram bot

## Структура файлов проекта:

```shell
├── LICENSE
├── Makefile
├── README.md
├── kittybot.py
├── main.log
└── requirements.txt
```

## Описание:

Телеграмм бот присылающий фото котиков по команде.

https://api.thecatapi.com/v1/images/search

## Команды:

```shell
$ make venv
```
Создание виртуального окружения и установка необходимых зависимостей requirements.txt

```shell
$ make lint
```
Проверка flake8

```shell
$ make isort
``` 
Исправление кода isort

```shell
$ make run
```
Запуск бота

```shell
$ make clean
```
Удаление кеша и очистка виртуального окружения
