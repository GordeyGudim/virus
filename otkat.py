#возвращает все к начальному состоянию

#импорт модулей

import shutil
import os

#удаление корневой папки

shutil.rmtree('coren')

#создание корневой папки

os.mkdir('coren')