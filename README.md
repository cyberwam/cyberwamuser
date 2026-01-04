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

**Примечание**  
Для эффективности рекомендуется использовать VPN, так как не все сайты смогут дать корректный ответ, особенно на территории РФ. Кроме этого, рекомендуется подправить /etc/resolv.conf
```sh
sudo vim /etc/resolv.conf
```
И добавить в него nameserver 1.1.1.1(Можете добавить другой)
```sh
nameserver 1.1.1.1
```
И перезагрузить сервис systemd
```sh
sudo systemctl restart systemd-resolved.service
```
При перезапуске системы, возможно, потребуется повторять действие

## Запуск в контейнере Podman
Базовый образ основан на archlinux. Он более тяжеловесный, чем ubuntu, но при установки утилит в убунту - в любом случае раздуется до таких же +/- размеров, поэтому идем по пути наименьшего сопротивления, использую archlinux и его пакетный менеджер  
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

## Локальная установка
Вместо локальной установки для себя я не стал заморачиваться. Добавил alias в конфиг fish, Вы может поступить аналогично или самостоятельно составить pyproject.toml или что-то в этом духе. Покажу, как выглядит мой alias(в директорию ~/project клонировал репозиторий для теста)
```sh
# ~/.config/fish/config.fish
alias cyberwamuser_="/home/max/project/cyberwamuser/venv/bin/python3 /home/max/project/cyberwamuser/cyberwamuser/__main__.py"
```
