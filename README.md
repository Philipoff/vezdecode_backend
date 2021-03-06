# FTIT - Вездекод-2022

## Vk Mini Apps

----

Это - решение в виде мини-прилождния для ВК (категория Vk Mini Apps)

### Демо - https://backend.vcode.flint3s.online
Для теста можно использовать ключ доступа `testkey`

### Что реализовано?
- Вывод загруженных фото - *10*
- Лайк и скип мемов через консольное приложение - *20*
- Алгоритм выдачи мемов с настройками выдачи - *30*
- Большое пополнение коллекции (>12000 мемов) - *40*
- Дашборд с небольшой аналитикой и ТОП-ом мемов - *50*
---

## Инструкция:
- Задания на 10, 20, 30 и 40 баллов можно протестировать в консольном приложении "./console-client (40)" - оно запускается
командой `python3 ./main.py` *(при условии, что все зависимости установлены)*. 
Приложение поддерживает опции получения мемов, их оценки (лайк или скип) и установки глобальных параметров 
для алгоритма выдачи мемов (эти данные хранятся в БД). Для установки настроек следует запустить файл `python3 ./edit_settings`
и следовать инструкции в нём. Остальные папки (`console-client(20)` и `show-pictures(10)`) оставлены в проекте для общего понимания :)

- Задание на 50 баллов выполнено в виде веб-приложения (клиент и сервер), общающихся по API. 
Ссылка на демо указана в начале этого README файла. Дашборд поддерживает функции просмотра топовых мемов и 
общей статистики по ним, а так же требует аутентификации для входа в него.

Для локального запуска нужно выполнить установку зависимостей для сервера/консольного клиента:
```shell
pip install -r requirements.txt
```

И зависимостей для дашборда со статистикой:
```shell
cd dashboard && npm i
```

После чего запустить проект:

- console client - `cd console-client && python3 ./main.py`

Дашборд запускается в 2 этапа:
1. Билд фронтенда - `cd dashboard && npm run build`. Появившуюся папку dist нужно переместить внутрь директории `./server`
2. Запуск дашборда - `cd dashboard && python3 ./flask_app.py`

Приложение запустится локально и будет доступно по адресам: 
- Дашборд - `localhost:3000`
- Cервер со статистикой - `localhost:5000`
- Консоль - из конcоли :)




created by FTIT (https://vk.com/ftitdev)
