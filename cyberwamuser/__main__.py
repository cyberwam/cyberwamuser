import sys
from modules.core import init_tool, get_social_list
from modules.colors import GREEN, RESET, RED, BLUE, BOLD
from modules.parser import parser_result
from modules.header import header
from modules.helper import helper

def social_list_processing(check_response:bool=False, username:str=None):
    service_dict = get_social_list()
    number_service = 0
    for service in service_dict:
        number_service+=1
        service_name = service['service']
        service_url = service['url']
        if username:
            service_url = service_url.replace('[username]', username)
        
        text = f'{service_name}\t{service_url}'
        if check_response:
            status = parser_result(url=service_url)

            if status:
                full_text = (
                        f'[{number_service}] {GREEN}USER DETECTED '
                        f'({username}:{service_name})'
                        f'{RESET} {text}'
                        )
            else:
                full_text = f'[{number_service}] {RED}USER NOT DETECTED:{RESET} {text}'
            print(full_text)
        else:
            full_text = f'[{number_service}] {text}'
            print(full_text)

def main():
    # Создает в директории ~/.config свою директорию,
    # перемещает в нее agent.json для генерирования 
    # user-agent`ов для запросов
    init_tool()
    params = sys.argv
    if len(params) > 1:
        if len(params) == 3 and '--user' in params[1]:
            username = params[2]
            print(f'search by username: {BOLD}{username}{RESET}')
            social_list_processing(check_response=True, username=username)
        elif len(params) == 3 and '--url' in params[1] and 'http' in params[2]:
            url = params[2]
            result = parser_result(url=url)
            print(result)
        elif '--social-list' in params[1]:
            social_list_processing()
        else:
            helper()
    else:
        helper()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(f'{RED}Exit...{RESET}')
    except Exception as err:
        print(err)
