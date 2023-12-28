# scrapy_parser_pep

Парсер документов PEP на базе фреймворка Scrapy.

## Стек

Python 3.9
Scrapy

## Описание

"Паук" собирает документы PEP с ресурса [https://peps.python.org/](https://peps.python.org/) и записывает результаты в файлы в папке results:

* pep_{datetime}.csv - список всех PEP (номер, название и статус)
* status_summary_{datetime}.csv - сводка по статусам PEP, сколько найдено документов в каждом статусе (статус, количество)


## Как запустить проект

1. Клонировать репозиторий:

```python
git clone git@github.com:SGERx/scrapy_parser_pep.git
```

2. Создать виртуальное окружение:

```python
python -m venv venv
```

3. Активировать виртуальное окружение, обновить версию ```pip``` и установить зависимости из ```requirements.txt```:

```python
source venv/Scripts/activate
```

```python
python -m pip install -–upgrade pip.
```

```python
pip install -r requirements.txt
```

4. Запустить "паука":

```python
scrapy crawl pep
```
