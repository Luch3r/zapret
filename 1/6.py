def atm_simulation():
    balance = 10000
    transactions = []
    
    print("Добро пожаловать в банкомат!")
    
    while True:
        print("\nДоступные операции:")
        print("1. Проверить баланс")
        print("2. Снять деньги")
        print("3. Пополнить счет")
        print("4. История операций")
        print("5. Выйти")
        
        choice = input("Выберите операцию (1-5): ")
        
        if choice == '1':
            print(f"Ваш текущий баланс: {balance} руб.")
            
        elif choice == '2':
            try:
                amount = float(input("Введите сумму для снятия: "))
                
                if amount <= 0:
                    print("Ошибка: Сумма должна быть положительной!")
                elif amount > 10000:
                    print("Ошибка: Максимальная сумма для снятия - 10000 руб.")
                elif amount > balance:
                    print("Ошибка: Недостаточно средств на счете!")
                else:
                    balance -= amount
                    transactions.append(f"Снятие: -{amount} руб.")
                    print(f"Операция успешна! Снято: {amount} руб.")
                    print(f"Остаток на счете: {balance} руб.")
                    
            except ValueError:
                print("Ошибка: Введите числовое значение!")
                
        elif choice == '3':
            try:
                amount = float(input("Введите сумму для пополнения: "))
                
                if amount <= 0:
                    print("Ошибка: Сумма должна быть положительной!")
                elif amount > 50000:
                    print("Ошибка: Максимальная сумма для пополнения - 50000 руб.")
                else:
                    balance += amount
                    transactions.append(f"Пополнение: +{amount} руб.")
                    print(f"Операция успешна! Зачислено: {amount} руб.")
                    print(f"Остаток на счете: {balance} руб.")
                    
            except ValueError:
                print("Ошибка: Введите числовое значение!")
                
        elif choice == '4':
            if transactions:
                print("История операций:")
                for transaction in transactions[-5:]: 
                    print(f"  {transaction}")
                print(f"Итоговый баланс: {balance} руб.")
            else:
                print("Операций еще не было.")
                
        elif choice == '5':
            print("Спасибо за использование банкомата!")
            print(f"Ваш итоговый баланс: {balance} руб.")
            break
            
        else:
            print("Ошибка: Выберите операцию от 1 до 5!")


atm_simulation()
