import getpass
import random


class Password_Generation:
    def __init__(self):
        self.__Amount_Simbols = 8
        self.__Generation_type = 1
        self.__Passwords_amount = 1
        self.__passwords_array = []
        self.get_param_info()

    def change_amount_simbols(self):
        new_amnt = input("Введите необходимое количество символов в пароле >>> ")
        if new_amnt.isdigit():
            if int(new_amnt) >= 6:
                self.__Amount_Simbols = int(new_amnt)
            else:
                print("Пароль короче 6 символов?! Меняй!")
                self.change_amount_simbols()
        else:
            print("Введите целое число")
            self.change_amount_simbols()

    def change_generation_type(self):
        new_gen_type = input('Выберите тип генерации \n1 - Буквы верхнего и нижнего регистра\n2 - Буквы и цифры\n'
                             '3 - Буквы, цифры и спец.символы\n')
        if new_gen_type.isdigit():
            self.__Generation_type = int(new_gen_type)
        else:
            print("Введите целое число")
            self.change_generation_type()

    def change_passwords_amount(self):
        new_amnt = input("Введите количество генерируемых паролей >>> ")
        if new_amnt.isdigit():
            self.__Passwords_amount = int(new_amnt)
        else:
            print("Введите целое число")
            self.change_passwords_amount()

    def change_parameters(self):
        self.change_amount_simbols()
        self.change_generation_type()
        self.change_passwords_amount()

    def get_param_info(self):
        print(f'Текущие параметры генерации:\n'
              f'Количество символов - {self.__Amount_Simbols}\n'
              f'Генерируется паролей - {self.__Passwords_amount}\n'
              f'Тип генерации - {self.get_gen_type()}')

    def get_gen_type(self):
        if self.__Generation_type == 1:
            return 'Буквы верхнего и нижнего регистра'
        if self.__Generation_type == 2:
            return 'Буквы и цифры'
        if self.__Generation_type == 3:
            return 'Буквы, цифры и спец.символы'

    def pass_generation(self):
        match self.__Generation_type:
            case 1:
                alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
                for i in range(0, self.__Passwords_amount, 1):
                    new_pass = ''
                    for j in range(0, self.__Amount_Simbols, 1):
                        new_pass += random.choice(alphabet)
                    self.__passwords_array.append(new_pass)
            case 2:
                alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"
                for i in range(0, self.__Passwords_amount, 1):
                    new_pass = ''
                    for j in range(0, self.__Amount_Simbols, 1):
                        x = random.randint(0, 1)
                        if x == 0:
                            new_pass += random.choice(alphabet[0:52])
                        else:
                            new_pass += random.choice(alphabet[52:])
                    self.__passwords_array.append(new_pass)
            case 3:
                alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#$%&'()*+,-./:;<=>?@[]_{}~`"
                for i in range(0, self.__Passwords_amount, 1):
                    new_pass = ''
                    for j in range(0, self.__Amount_Simbols, 1):
                        x = random.randint(0, 2)
                        if x == 0:
                            new_pass += random.choice(alphabet[0:52])
                        elif x == 1:
                            new_pass += random.choice(alphabet[52:62])
                        else:
                            new_pass += random.choice(alphabet[62:])

                    self.__passwords_array.append(new_pass)
            case _:
                print('Если бы мы знали, что это такое. Мы не знаем, что это такое.')

    def show_passwords(self):
        print('Сгенерированные пароли:')
        for i in range(0, len(self.__passwords_array), 1):
            print(f"{self.__passwords_array[i]}")

    def save_passwords(self):
        desktop_path = "C:\\Users\\{username}\\Desktop\\GeneratedPasswords.txt".format(username=getpass.getuser())

        with open(desktop_path, "w") as file:
            for i in range(0, len(self.__passwords_array), 1):
                file.writelines(f"{self.__passwords_array[i]}\n")

        print("Пароли сохранены на рабочий стол. Путь до файла\n"+
              "C:\\Users\\{username}\\Desktop\\GeneratedPasswords.txt".format(username=getpass.getuser()))
