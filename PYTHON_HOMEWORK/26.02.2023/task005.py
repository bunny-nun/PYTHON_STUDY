"""
Задание 5:
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import chardet
import subprocess

ping_list = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for attempt in range(len(ping_list)):
    ping = subprocess.Popen(ping_list[attempt], stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('UTF-8').decode('UTF-8')
        print(line)
