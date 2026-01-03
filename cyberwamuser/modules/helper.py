import textwrap
from modules.colors import RESET, RED, GREEN, BOLD
from __init__ import __author__, __version__

def helper():
    text = f"""\
    Author:     {BOLD}{__author__}{RESET}
    Version:    {BOLD}{__version__}{RESET}
    
    cyberwamuser:
    --user <string>         Поиск по никнейму
    """

    text = textwrap.dedent(text)
    print(text)
