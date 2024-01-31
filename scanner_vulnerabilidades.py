import requests
from bs4 import BeautifulSoup

def scanner(url):
    try:
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://' + url
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            server_version_tag = soup.find('meta', {'name': 'generator'})
        if server_version_tag:
            server_version = server_version_tag.get('content')
            print("Versao do servidor web em {url}: {server_version}")
        else:
            print("Nenhuma informacao de versao do servidor encontrada")
    except Exception as e:
        print(f"Erro ao escanear {url}: {str(e)}")

if __name__ == "__main__":

    target_url = "www.google.com.br"
    scanner(target_url)