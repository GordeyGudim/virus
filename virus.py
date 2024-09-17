#непосредственно засоряет

#Импорт нужных модулей

import os
import shutil

#Задание колличества папок в корневой папке

count = 5

#создание папок и закидываение в них фалов

for i in range(count):

#создание папки

    os.mkdir(f'coren/{str(i)}')

#копирование в нее исходного файла

    shutil.copy2('text.txt', f'coren/{str(i)}')


