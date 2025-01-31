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
        total_costs = np.zeros(num_trials)  # Масив для витрат

        for i in range(num_trials):
            remaining_items = total_items - initial_collected
            total_spent = 0

            while remaining_items > 0:
                if remaining_items <= switch_threshold:
                    total_spent += 10000  # Гарантований ящик
                    remaining_items -= 1
                else:
                    total_spent += 2000  # Випадковий ящик
                    remaining_items -= np.random.rand() < (remaining_items / total_items)

            total_costs[i] = total_spent
        return total_costs

# Параметри симуляцій
num_trials = 500000
switch_thresholds = [7, 6, 5]
colors = ['blue', 'red', 'green']

# Запуск симуляцій для різних стратегій
strategies = {
    f"Перехід на {t} речах": simulate_auto_strategy(switch_threshold=t, num_trials=num_trials)
    for t in switch_thresholds
}

# Побудова графіку
plt.figure(figsize=(10, 6))

for (label, costs), color in zip(strategies.items(), colors):
    median_value = np.median(costs)
    plt.hist(costs, bins=50, alpha=0.6, color=color, label=f'{label} (медіана: {median_value:.0f})')
    plt.axvline(median_value, color=color, linestyle='dashed', linewidth=2, label=f'Медіана {label}')

plt.xlabel("Загальні витрати (од.)")
plt.ylabel("Частота")
plt.title("Порівняння вартості стратегій для різних порогів переходу")
plt.legend()
plt.grid(True)
plt.savefig("experiment_results.png")
