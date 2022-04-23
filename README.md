# FTIT - Вездекод-2022

## Vk Mini Apps

----

Это - решение в виде мини-прилождния для ВК (категория Vk Mini Apps)

### Демо - https://backend.vcode2022.flint3s.online
Для теста можно использовать ключ доступа `testkey`

### Что реализовано?
- Вывод загруженных фото __(show-pictures)__ - *10*
- Лайк и скип мемов через консольное приложение __(console-client)__ - *20*

---


Для локального запуска нужно выполнить установку зависимостей для сервера/консольного клиента:
```shell
pip install -r requirements.txt
```

И зависимостей для дашборда со статистикой:
```shell
cd dashboard && npm i
```

После чего запустить проект:

- server - `cd server && python ./app.py`

- console client - `cd console-client && python3 ./main.py`

- dashboard - `cd dashboard && npm run serve`

Приложение запустится локально и будет доступно по адресам: 
- Дашборд - `localhost:3000`
- Cервер со статистикой - `localhost:5000`
- Консоль - из конмоли :)




created by FTIT (https://vk.com/ftitdev)
