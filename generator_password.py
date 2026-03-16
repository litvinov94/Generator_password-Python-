import random
import string
import pyperclip
import time
import json


def generate_password(lenght, use_digits, use_uppercase, use_lower, use_punctuation):
    """Генерирует пароль на основе заданных параметров."""
    characters = ''

    if use_digits:
        characters += string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        print('Ошибка: не выбран ни один тип символов!')
        return None
    

    # Генерируем пароль, выбирая случайные символы из пула
    password = ''.join(random.choice(characters) for _ in range(lenght))
    return password
    

def get_yes_no(prompt):
    """Запрашивает ответ да/нет, возвращает True/False."""
    while True:
        ans = input(prompt).strip().lower()

        if ans in ('да', 'lf', 'yes', 'y', 'д'):
            return True
        elif ans in ('нет', 'ytn', 'no', 'n', 'н'):
            return False
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

def main():
    while True:
        print('--- Генератор паролей ---')
        print('1. Сгенерировать новый пароль')
        print('2. Выход')
        print()

        choise = input('Выберите действие (цифру): ').strip()

        if choise == '1':
            try:
                # Запрашиваем длину
                length = int(input('Введите длину пароля (целое положительное число): '))
                if length <= 0:
                    print('Длина должна быть положительной.')
                    continue
            except ValueError:
                print('Ошибка: введите целое число.')
                continue

            # Запрашиваем типы символов
            use_digits = get_yes_no('Использовать цифры? (да/нет): ')
            use_uppercase = get_yes_no('Использовать заглавные буквы? (да/нет): ')
            use_lower = get_yes_no('Использовать строчные буквы? (да/нет): ')
            use_punctuation = get_yes_no('Использовать спецсимволы? (да/нет): ')

            print()

            # Проверяем, что выбран хотя бы один тип
            if not (use_digits or use_uppercase or use_lower or use_punctuation):
                print("Ошибка: нужно выбрать хотя бы один тип символов.")
                continue

            # Генерируем и выводим пароль
            password = generate_password(length, use_digits, use_uppercase, use_lower, use_punctuation)


            if password:
                print(f"Сгенерированный пароль: {password}")
                print()

            if get_yes_no('Скопировать пароль? (да/нет): '):
                pyperclip.copy(password)

                time.sleep(1)

                print('Пароль скопирован в буфер обмена!')
                print()

            if get_yes_no('Сохранить пароль? (да/нет): '):
                save_password = {}

                service = input('Введите сервис: ')
                login = input('Введите логин: ')
                password = password

                save_password['service'] = service
                save_password['login'] = login
                save_password['password'] = password

                
        elif choise == '2':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите 1 или 2.")


if __name__ == '__main__':
    main()