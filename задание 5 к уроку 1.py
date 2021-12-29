# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый
#    (предварительно определив кодировку выводимых сообщений).
import locale
import platform
import subprocess

import chardet

default_encoding = locale.getpreferredencoding()

domains = [
    'yandex.ru',
    'youtube.com'
]

param = '-n' if platform.system().lower() == 'windows' else '-c'

for domain in domains:
    args = ['ping', param, '2', domain]
    result = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in result.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode(default_encoding)
        print(line.decode(default_encoding))
