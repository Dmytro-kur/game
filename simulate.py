import numpy as np

def lootbox_simulation(
    total_items=36,
    initial_collected=None,
    # max_random_boxes=5,
    auto_strategy=True,
    switch_threshold=7
):
    """
    Симуляція процесу збору речей з автоматичним вибором між випадковими ящиками (2000 од.)
    і гарантованими (10000 од.) за заданою стратегією.
    switch_threshold: при досягненні цієї кількості речей, переходимо на гарантовані ящики.
    """
    if initial_collected is None:
        initial_collected = int(input("Введіть початкову кількість зібраних речей: "))
    
    remaining_items = total_items - initial_collected  # Скільки ще потрібно зібрати
    total_spent = 0  # Витрачені кошти
    
    print(f"Старт: потрібно зібрати ще {remaining_items} речей.")
    
    while remaining_items > 0:
        print(f"\nЗалишилося зібрати: {remaining_items} речей")

        if auto_strategy:
            if remaining_items <= switch_threshold:
                choice = "2"  # Купуємо гарантовано за 10000
            else:
                choice = "1"  # Купуємо випадковий ящик за 2000

        else:
            print("1 - Купити випадковий ящик за 2000 од.")
            print("2 - Купити гарантований ящик за 10000 од.")
            choice = input("Ваш вибір (1 або 2): ")
        
        if choice == "1":
            p_new_item = remaining_items / total_items  # Ймовірність отримати нову річ
            new_item = np.random.rand() < p_new_item  # Чи випала нова річ
            total_spent += 2000
            
            if new_item:
                remaining_items -= 1
                print("Ви отримали нову річ!")
            else:
                print("Ви отримали повторну річ.")
        
        elif choice == "2":
            total_spent += 10000
            remaining_items -= 1
            print("Ви гарантовано отримали нову річ!")
        
        else:
            print("Неправильний вибір, спробуйте ще раз.")
    
    print("\nВсі речі зібрані!")
    print(f"Загальні витрати: {total_spent} од.")
    return switch_threshold, total_spent


# Запуск симуляції
if __name__ == "__main__":
    lootbox_simulation(initial_collected=0, auto_strategy=True, switch_threshold=5)
