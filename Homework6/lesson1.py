class ClientBase:

    def __init__(self,fio, passport_information, age):

        self.verify_fio(fio)
        self.verify_passport_information(passport_information)
        self.verify_age(age)

        self.__fio = fio
        self.__passport_information = passport_information
        self.__age = age

    # Проверка корректности ФИО
    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должны быть строкой")

        y = fio.split()
        if len(y) != 3:
            raise TypeError("Неверный формат ФИО")
        for n in y:
            if len(n) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")

    # Проверка паспортных данных
    @classmethod
    def verify_passport_information(cls, passport_information):
        if type(passport_information) != str:
            raise TypeError ("Паспорт должен быть строкой")

        p = passport_information.split()
        if len(p) != 2 or len(p[0]) != 2 or len(p[1]) != 8:
            raise TypeError("Неверный формат паспорта")

        for x in p:
            if not x.isdigit():
                raise TypeError("Серия и номер паспорта должен содержать только цифры")

    # Проверка возраста
    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 18 or age > 80:
            raise TypeError("Возраст должен быть целым числом в диапазоне [18, 80] лет")

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.verify_fio(fio)
        self.__fio = fio

    @property
    def passport_information(self):
        return self.__passport_information

    @passport_information.setter
    def passport_information(self, passport_information):
        self.verify_passport_information(passport_information)
        self.__passport_information = passport_information

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

class ClientFinancialActivities:

    def __init__(self, transaction, savings_account, deposit_account, credit):

        self.verify_transaction(transaction)
        self.verify_savings_account(savings_account)
        self.verify_deposit_account(deposit_account)
        self.verify_credit(credit)

        self.__transaction = transaction
        self.__savings_account = savings_account
        self.__deposit_account = deposit_account
        self.__credit = credit

    # Проверка корректности введения суммы транзакции
    @classmethod
    def verify_transaction(cls, transaction):
        if type(transaction) != int or transaction > 300:
            raise TypeError ("Транзакция должна быть целым числом и не превышать 300 рублей ")

    # Проверка корректности введения суммы сберегательного счета
    @classmethod
    def verify_savings_account(cls, savings_account):
        if type(savings_account) != int or savings_account <= 500:
            raise TypeError ("Сберегательный счет должен быть целым числом и минимальная сумма должна быть 500 рублей")

    # Проверка корректности введения суммы депозитного счета
    @classmethod
    def verify_deposit_account(cls, deposit_account):
        if type(deposit_account) != int or deposit_account <= 1000:
            raise TypeError ("Депозитный счет должен быть целым числом и минимальная сумма должна быть 1000 рублей")

    # Проверка корректности введения суммы кредита
    @classmethod
    def verify_credit(cls, credit):
        if type(credit) != int or credit > 1000:
            raise TypeError ("Сумма кредита должна быть целым числом и не превышать сумму 1000 рублей")


    @property
    def transaction(self):
        return self.__transaction

    @transaction.setter
    def transaction(self, transaction):
        self.verify_transaction(transaction)
        self.__transaction = transaction

    @property
    def savings_account(self):
        return self.__savings_account

    @savings_account.setter
    def savings_account(self, savings_account):
        self.verify_savings_account(savings_account)
        self.__savings_account = savings_account

    @property
    def deposit_account(self):
        return self.__deposit_account

    @savings_account.setter
    def savings_account(self, deposit_account):
        self.verify_savings_account(deposit_account)
        self.__savings_account = deposit_account

    @property
    def credit(self):
        return self.__credit

    @credit.setter
    def credit(self, credit):
        self.verify_credit(credit)
        self.__credit = credit

class Client(ClientBase):

    def __init__(self,fio, passport_information, age ):
        super().__init__(fio, passport_information, age)

    def __str__(self):
        return f"КЛИЕНТ: ФИО: {self.fio}, паспорт №: {self.passport_information}, возраст: {self.age} года"


class ClientBankReport(ClientFinancialActivities):

    def __init__(self, transaction, savings_account, deposit_account, credit):
        super().__init__(transaction, savings_account, deposit_account, credit)

    def __str__(self):
        return (f"БАНКОВСКИЙ ОТЧЕТ КЛИЕНТА: транзакция составляет {self.transaction} рублей,"
                f"сберегательный счет равен {self.savings_account} рублей,"
                f" депозитный счет равен {self.deposit_account} рублей, сумма кредита составляет {self.credit} рублей")

v = Client("Kalenchyts Vasili Vasiljevich","12 12345678", 44 )
c = ClientBankReport (300, 690, 1007, 1000)

print(v)
print(c)