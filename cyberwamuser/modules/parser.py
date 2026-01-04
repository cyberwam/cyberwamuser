import requests
from modules.header import header

def parser_result(url:str) -> str:
    status = False
    try:
        head = header()
        response = requests.get(url, headers=head)
        status_code = response.status_code
        if str(status_code) == '200':
            status = True
        return status
    except Exception as err:
        if 'SSLCertVerificationError' in str(err):
            return False
        return err
