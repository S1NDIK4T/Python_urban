import random
from curses.ascii import isdigit


class Password_Generation:
    def __init__(self):
        self.__Amount_Simbols = 8
        self.__Generation_type = 1
        self.__Passwords_amount = 1
        self.__passwords_array = []
        self.get_param_info()
    def change_amount_simbols(self):
        new_amnt = input("Введите необходимое количество символов в пароле >>> ")
        if isdigit(new_amnt):
            self.__Amount_Simbols = new_amnt
        else:
            print("Введите целое число")
            self.change_amount_simbols()
    def change_generation_type(self):
        new_gen_type = input('Выберите тип генерации \n1 - Буквы верхнего и нижнего регистра\n2 - Буквы и цифры\n'
                                 '3 - Буквы, цифры и спец.символы\n')
        if isdigit(new_gen_type):
            self.__Generation_type = new_gen_type
        else:
            print("Введите целое число")
            self.change_generation_type()
    def change_passwords_amount(self):
        new_amnt = input("Введите количество генерируемых паролей >>> ")
        if isdigit(new_amnt):
            self.__Passwords_amount = new_amnt
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
                for i in range(0,self.__Passwords_amount,1):
                    new_pass = ''
                    for j in range(0,self.__Amount_Simbols,1):
                        new_pass += random.choice(alphabet)
                    self.__passwords_array.append(new_pass)
            case _:
                print('Если бы мы знали, что это такое. Мы не знаем, что это такое.')

    def show_passwords(self):
        print('Сгенерированные пароли:')
        for i in range(0,len(self.__passwords_array),1):
            print(f"{self.__passwords_array[i]}")