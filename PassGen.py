class Password_Generation:
    def __init__(self):
        self.__Amount_Simbols = 8
        self.__Generation_type = 1
        self.__Passwords_amount = 1
        self.get_param_info()


    def change_amount_simbols(self):
        new_amnt = int(input("Введите необходимое количество символов в пароле >>> "))
        if isinstance(new_amnt, int):
            self.__Amount_Simbols = new_amnt
        else:
            print("Введите целое число")
            self.change_amount_simbols()
    def change_generation_type(self):
        new_gen_type = int(input('Выберите тип генерации \n1 - Буквы верхнего и нижнего регистра\n2 - Буквы и цифры\n'
            '3 - Буквы, цифры и спец.символы\n'))
        if isinstance(new_gen_type, int):
            self.__Generation_type = new_gen_type
        else:
            print("Введите целое число")
            self.change_generation_type()

    def change_passwords_amount(self):
        new_amnt = int(input("Введите количество генерируемых паролей >>> "))
        if isinstance(new_amnt, int):
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