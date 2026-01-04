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
~/.config/cyberwamuser/  

Активируем окружение
```sh
source venv/bin/activate
```
Запуск без параметров - будет выведена подсказка по командам
```sh
python3 cyberwamuser
```
