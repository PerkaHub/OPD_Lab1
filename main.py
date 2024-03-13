from bs4 import BeautifulSoup
import requests

def parse():
    requests.packages.urllib3.disable_warnings()
   # proxies = {
     #   'http': 'http://proxy.omgtu:8080',
     #   'https': 'http://proxy.omgtu:8080'
   # }
    url = 'https://omgtu.ru/general_information/faculties/'
    page = requests.get(url, verify=False)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")

    block = soup.findAll('div', id='pagecontent')
    description = ''
    for data in block:
        if data.find('a'):
            text = data.text.strip()
            if text:
                description += text

    with open('ogog.txt', 'w', encoding='utf-8') as f:
        f.write(description)


def remove_extra_newlines(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')  # Удаляем переход на новую строку в конце строки
            if line:  # Пропускаем пустые строки
                lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))


parse()
remove_extra_newlines('ogog.txt')