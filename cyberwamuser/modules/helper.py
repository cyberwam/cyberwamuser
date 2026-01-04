import textwrap
from modules.colors import RESET, RED, GREEN, BOLD
from __init__ import __author__, __version__

def helper():
    text = f"""\
    Author:     {BOLD}{__author__}{RESET}
    Version:    {BOLD}{__version__}{RESET}
    
    cyberwamuser:
    --user <username>       Поиск по никнейму
                            Пример использования:
                            {GREEN}cyberwamuser --user test_username{RESET}

    --url <test url>        Тестирование ответа сервиса. 
                            Пример использования:
                            {GREEN}cyberwamuser --url https://habr.com/ru/users/skfkdf/{RESET}

    --social-list           Вывод списка социальных сетей/сервисов
                            Пример использования:
                            {GREEN}cyberwamuser --social-list{RESET}
    """

    text = textwrap.dedent(text)
    print(text)
