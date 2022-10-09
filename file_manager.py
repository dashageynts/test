import os
import shutil as sh
#Создаем файл
def create_file(name, text = None):
    with open(name, 'w', encoding = 'utf-8') as f:
        if text:
            f.write(text)
    print(f'File {name} was created')
#печатаем содержимое файла
def open_file(name):
    print(f'File {name} was opened')
    with open(name, 'r') as f:
        for line in f:
            print(line)

#Создаем папку
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('This folder is already exists')
    print(f'Folder {name} was created')

#Удаляем файл/папку
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)
    print(f'File {name} was deleted')

#Копируем файл/папку
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            sh.copytree(name, new_name)
        except FileExistsError:
            print('This folder already exists')
    else:
        sh.copy(name, new_name)
    print(f'File {name} was copied with name {new_name}')

#Переименовываем файл/папку
def rename_file(name, new_name):
    os.rename(name, new_name)
    print(f'File {name} was renamed as {new_name}')

def return_indirectory():
    pass



# проверка необходимых действий с папкой/файлом
if __name__ == '__main__':
    create_file('text.txt')
    create_file('test.txt', 'some text')
    create_folder('new_folder')
    create_folder('other_folder')
    delete_file('other_folder')
    delete_file('text.txt')
    delete_file('somefolder')
    open_file('test.txt')
    rename_file('text.txt','super_text.txt')
    copy_file('test.txt','est.txt')
