# cyberwamUser

**Инструмент автоматизирует поиск пользователей по username по различным сайтам и сервисам** 

## Установка
Клонируем репозиторий
```sh
git clone https://github.com/cyberwam/cyberwamuser
```
Установим необходимые пакеты
```sh
cd cyberwamuser && python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
```

## Запуск утилиты
При первом запуске утилиты будет создана директория для конфигов и необходимых данных, туда будет скопированы заголовке для генерации user-agent и т.д. Путь конфигов:
```sh
~/.config/cyberwamuser/  
```

Активируем окружение
```sh
source venv/bin/activate
```
Запуск без параметров - будет выведена подсказка по командам
```sh
python3 cyberwamuser
```

## Запуск в контейнере Podman
Базовый образ основан на archlinux. Он более тяжеловесный, чем ubuntu, но при установки утилит в убунту - в любом случае раздуется до таких же +/- размеров, поэтому не идем по пути наименьшего сопротивления, использую archlinux и его пакетный менеджер  
Соберем образ
```sh
podman build -t cyberwam -f Containerfile
```
Запустим с последуюзим удаление контейнера
```sh
podman run --rm -it cyberwam
```
Если нужно будет работать в том же контейнере
```sh
podman run -it --name cyber_1 cyberwam
```
