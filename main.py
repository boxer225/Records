from record import Record

DATA_FILE = "finances.txt"

def main() -> None:
    """
        Work with file and records
    """

    record: Record = Record(DATA_FILE)
    
    while True:
        print("\\nВыберите действие:")
        print("1. Вывод баланса")
        print("2. Добавление записи")
        print("3. Редактирование записи")
        print("4. Поиск по записям")
        print("5. Выход")
        
        choice: str = input("Ваш выбор: ")
        
        if choice == "1":
            record.show_balance()
        elif choice == "2":
            record.add_record()
        elif choice == "3":
            record.edit_record()
        elif choice == "4":
            record.search_records()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

#if __name__ == "main":
main()