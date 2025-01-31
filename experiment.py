import numpy as np

import matplotlib.pyplot as plt


def simulate_auto_strategy(
    total_items=36,
    initial_collected=0,
    switch_threshold=7,
    num_trials=10000
):
    """
    Симуляція процесу збору речей з автоматичним вибором між випадковими ящиками (2000 од.)
    і гарантованими (10000 од.) за заданою стратегією.
    switch_threshold: при досягненні цієї кількості речей, переходимо на гарантовані ящики.
    num_trials: кількість симуляцій для усереднення результату.
    """
    total_costs = []  # Список для збереження витрат по кожній симуляції

    for _ in range(num_trials):
        remaining_items = total_items - initial_collected  # Скільки ще потрібно зібрати
        total_spent = 0  # Витрачені кошти

        while remaining_items > 0:
            if remaining_items <= switch_threshold:
                # Купуємо гарантований ящик
                total_spent += 10000
                remaining_items -= 1
            else:
                # Купуємо випадковий ящик за 2000
                p_new_item = remaining_items / total_items  # Ймовірність отримати нову річ
                new_item = np.random.rand() < p_new_item  # Чи випала нова річ
                total_spent += 2000

                if new_item:
                    remaining_items -= 1

        total_costs.append(total_spent)
    return np.array(total_costs)  # Повертаємо масив витрат для кожної симуляції

# Запускаємо симуляції для двох стратегій: зміна на 7 речах і на 20 речах

num_trials = 100000

strategy_1_costs = simulate_auto_strategy(switch_threshold=7, num_trials=num_trials)
strategy_2_costs = simulate_auto_strategy(switch_threshold=1, num_trials=num_trials)
strategy_3_costs = simulate_auto_strategy(switch_threshold=10, num_trials=num_trials)

# Побудова графіків для обох стратегій
plt.figure(figsize=(10, 6))
plt.hist(strategy_1_costs, bins=50, alpha=0.6, color='blue', label='Перехід на 7 речах')
plt.hist(strategy_2_costs, bins=50, alpha=0.6, color='red', label='Перехід на 1 речах')
plt.hist(strategy_3_costs, bins=50, alpha=0.6, color='green', label='Перехід на 10 речах')
plt.xlabel("Загальні витрати (од.)")
plt.ylabel("Частота")
plt.title("Порівняння вартості стратегій для різних порогів переходу")
plt.legend()
plt.grid(True)
plt.savefig("experiment_results.png")
