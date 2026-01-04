import os
import shutil

SERVICE_CONF = 'service'
UTILS_NAME = 'cyberwamuser'

def get_user_name() -> str:
    #user_name = os.getlogin()
    return os.environ.get('LOGNAME') or os.environ.get('USER') or 'user'
    

def get_config_path() -> str:
    user_name = get_user_name()
    config_dir = f'/home/{user_name}/.config'
    return config_dir

def init_tool():
    agent = 'agent.json'
    agent_path = f'tmp/{agent}'
    service_path = f'tmp/{SERVICE_CONF}'
    
    config_dir = get_config_path()
    
    config_dir_path = f'{config_dir}/{UTILS_NAME}'
    if not os.path.exists(config_dir_path):
        os.makedirs(f'{config_dir_path}')
        print(f'Create config dir: {config_dir_path}')

    if os.path.exists(agent_path):
        shutil.copy(agent_path, f'{config_dir_path}/{agent}')
        print(f'Copy {agent_path} -> {config_dir_path}/{agent}')
    if os.path.exists(service_path):
        shutil.copy(service_path, f'{config_dir_path}/{SERVICE_CONF}')
        print(f'Copy {service_path} -> {config_dir_path}/{SERVICE_CONF}')
        # Удаляем временную директорию для хранения стартовой инфы
        #os.removedirs(f'{agent_path.split('/')[0]}')
    

def get_social_list() -> list[dict[str]]:
    full_list_service = []
    config_dir = get_config_path()
    social_service_path = f'{config_dir}/{UTILS_NAME}/{SERVICE_CONF}'
    with open(social_service_path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            service_name, service_url = line.split('\t')
            data = {'service':service_name, 'url':service_url}
            full_list_service.append(data)
    
    return full_list_service
