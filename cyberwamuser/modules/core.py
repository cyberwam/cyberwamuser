import os
import shutil

def get_user_name() -> str:
    user_name = os.getlogin()
    return user_name

def get_config_path() -> str:
    user_name = get_user_name()
    config_dir = f'/home/{user_name}/.config'
    return config_dir

def init_tool():
    agent = 'agent.json'
    agent_path = f'tmp/{agent}'

    
    config_dir = get_config_path()
    
    utils_name = 'cyberwamuser'
    config_dir_path = f'{config_dir}/{utils_name}'
    if not os.path.exists(config_dir_path):
        os.makedirs(f'{config_dir_path}')
        print(f'Create config dir: {config_dir_path}')

    if os.path.exists(agent_path):
        shutil.move(agent_path, f'{config_dir_path}/{agent}')
        print(f'Move {agent_path} -> {config_dir_path}/{agent}')
        os.removedirs(f'{agent_path.split('/')[0]}')
    
