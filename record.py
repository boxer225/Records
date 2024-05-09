import os
import datetime

class Record:
    records: list = []
    file_name: str = ''

    def __init__(self, file_name) -> None:
        """
            Add records from file
        """
        self.file_name: str = file_name
        if os.path.exists(self.file_name):
            date: datetime.datetime = None
            category: str = None
            amount: float = None
            description: str = None
            with open(file=self.file_name, mode="r", encoding="utf-8") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    if 'дата' in lines[i].lower():
                        date = datetime.datetime.strptime(lines[i].split(': ')[1].strip(), "%Y-%m-%d")
                    if 'категория' in lines[i+1].lower():
                        category = lines[i+1].split(': ')[1].strip()
                    if 'сумма' in lines[i+2].lower():
                        amount = float(lines[i+2].split(': ')[1].strip())
                    if 'описание' in lines[i+3].lower():
                        description = lines[i+3].split(': ')[1].strip()
                    record: dict = {
                        'date': date,
                        'category': category,
                        'amount': amount,
                        'description': description
                        }
                    self.records.append(record)
            print(self.records)

    def save_records(self) -> None:
        """
            Save record to file
        """
        with open(self.file_name, "w") as file:
            for record in self.records:
                file.write(f"Дата: {record['date'].strftime('%Y-%m-%d')}\n")
                file.write(f"Категория: {record['category']}\n")
                file.write(f"Сумма: {record['amount']}\n")
                file.write(f"Описание: {record['description']}\n\n")

    def show_balance(self) -> None:
        """
            Show balance, income and expense
        """
        total_income: float = sum(record['amount'] for record in self.records if record['category'].lower() == "доход")
        total_expense: float = sum(record['amount'] for record in self.records if record['category'].lower() == "расход")
        balance: float = total_income - total_expense
        print(f"Текущий баланс: {balance}")
        print(f"Доходы: {total_income}")
        print(f"Расходы: {total_expense}")

    def add_record(self) -> None:
        """
            Add new record to file
        """
        new_date: str = input("Введите дату (гггг-мм-дд): ")
        date: datetime.datetime = datetime.datetime.strptime(new_date, "%Y-%m-%d")
        category: str = input("Введите категорию (Доход/Расход): ")
        amount: float = float(input("Введите сумму: "))
        description: str = input("Введите описание: ")
        record: dict = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
            }
        self.records.append(record)
        self.save_records()
        print("Запись добавлена успешно.")

    def edit_record(self) -> None:
        """
            Edit one record from file by index
        """
        index: int = int(input("Введите номер записи для редактирования: "))
        if index < 1 or index > len(self.records):
            print("Неверный номер записи.")
            return
        record: dict = self.records[index - 1]
        print(f"Дата: {record['date'].strftime('%Y-%m-%d')}")
        print(f"Категория: {record['category']}")
        print(f"Сумма: {record['amount']}")
        print(f"Описание: {record['description']}")
    
        field: str = input("Введите поле для редактирования (дата/категория/сумма/описание): ").lower()
        if field.lower() == "дата":
            new_date : str= input("Введите новую дату (гггг-мм-дд): ")
            record['date'] = datetime.datetime.strptime(new_date, "%Y-%m-%d")
        elif field.lower() == "категория":
            record['category'] = input("Введите новую категорию (Доход/Расход): ")
        elif field.lower() == "сумма":
            record['amount'] = float(input("Введите новую сумму: "))
        elif field.lower() == "описание":
            record['description'] = input("Введите новое описание: ")
    
        self.save_records()
        print("Запись успешно отредактирована.")

    def search_records(self) -> None:
        """
            Search records by filter
        """
        filtered_records: list = []
        search: str = input("Введите, по какому параметру необходимо искать (Категория/Дата/Сумма): ")
        if search.lower() == 'категория':
            category: str = input("Введите категорию для поиска (Доход/Расход): ")
            filtered_records = [record for record in self.records if record['category'] == category]
        if search.lower() == 'дата':
            date: str = input("Введите дату (гггг-мм-дд): ")
            filtered_records = [record for record in self.records if record['date'] == datetime.datetime.strptime(date, "%Y-%m-%d")]
        if search.lower() == 'сумма':
            amount: float = float(input("Введите сумму: "))
            filtered_records = [record for record in self.records if record['amount'] == amount]
        else:
            print('такого фильтра не существует')
    
        for record in filtered_records:
            print(f"Дата: {record['date'].strftime('%Y-%m-%d')}")
            print(f"Категория: {record['category']}")
            print(f"Сумма: {record['amount']}")
            print(f"Описание: {record['description']}\\n")
