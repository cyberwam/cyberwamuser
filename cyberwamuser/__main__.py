import sys
from modules.core import init_tool 
from modules.header import header
from modules.helper import helper

def parse_params() ->str:
    params = sys.argv
    if len(params) > 1:
        if len(params) == 3 and '--user' in params[1]:
            username = params[2]
            print(f'user: {username}')
            return username
        elif '--social-list' in params[1]:
            sys.exit('Будет выведен список сервисов')
    else:
        helper()

def main():
    # Создает в директории ~/.config свою директорию,
    # перемещает в нее agent.json для генерирования 
    # user-agent`ов для запросов
    #init_tool()
    params = parse_params()
    

if __name__ == '__main__':
    main()
