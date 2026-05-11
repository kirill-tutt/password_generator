# Модули для работы/Modules for work
import random as rd
from datetime import datetime
import os
# Список используемых символов/List of symbols used
sp1 = '!@#$%^&*()-_+=;:,./?[]{}~'
sp2_1 = 'qwertyuiopasdfghjklzxcvbnm'
sp2_2 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
sp3 = '0123456789'
all_chars = sp1 + sp2_1 + sp2_2 + sp3
# Считаем количество логинов, если файл существует, если нет, то создаётся автоматически/We count the number of logins if the file exists, if not, it is created automatically
n = 1
if os.path.exists('Anapa2000.txt'):
    with open('Anapa2000.txt', 'r', encoding='utf-8') as f:
        n = f.read().count('Логин') + 1
# Открываем файл для работы/Open the file for work
f = open('Anapa2000.txt', 'a', encoding='utf-8')
# Начало работы программы/Getting Started with the Program
print('Начало работы. Для завершения напишите: kill/Getting started. To finish, type: kill')
while True:
    # Ввода сайта; логина; пароля/Entering the website; login; password
    k0_0 = input('\nВведите название сайта/Enter the site name: ')
    if k0_0.lower() == 'kill': break
    k0 = input(f'Введите логин (или подписан будет как {n})/Enter your login (or it will be signed as {n}): ')
    if k0.lower() == 'kill': break
    k1 = input('Введите длину пароля (по умолчанию 12)/Enter the password length (default 12): ')
    if k1.lower() == 'kill': break
    try:
        # Переменная для длины пароля, по умолчанию 12/Variable for password length, default is 12
        length = int(k1) if k1 != '' else 12
        # Если k0 пустое, ставим номер n, иначе — то, что ввел пользователь/If k0 is empty, we put the number n, otherwise - what the user entered
        length_2 = k0 if k0 != '' else n
        # Генерируем итоговый пароль/Generating the final password
        password = ''.join(rd.choice(all_chars) for _ in range(length))
        # Берем время прямо сейчас на ПК/Let's take time right now on PC
        formatted_date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        # Записываем все данные в файл/We write all data to a file
        f.write(f'{formatted_date}\nНазвание сайта/Website name: {k0_0}\nЛогин/Login: {length_2}\nПароль/Password: {password}\n\n')
        f.flush()  # Сохраняем изменения в файл сразу/Save changes to the file immediately
        # Выводим данные которые только что ввели и записали в файл/We output the data that we just entered and wrote to the file.
        print(f'Ваш логин: {n}\t Ваш пароль: {password}\t Записан для сайта: {k0_0}\nYour login: {n}\t Your password: {password}\t Recorded for the site: {k0_0}')
        n += 1  # Увеличиваем счетчик для следующего раза/Increase the counter for next time
    # Обработка неправильного ввода числа/Handling invalid number input
    except ValueError:
        print('Пожалуйста, введите целое число или "kill"/Please enter an integer or "kill"')
# Закрытие файла и завершение программы/Closing the file and terminating the program
f.close()
print('Программа завершила работу!/The program has completed its work!')
