# Документація до симуляції витрат на лутбокси

## Опис проекту

Цей проект містить два основні скрипти для симуляції збору речей у випадкових ящиках (лутбоксах) за різними стратегіями. Він дозволяє проаналізувати загальні витрати гравця при використанні випадкових та гарантованих ящиків з певними порогами перемиканнями між ними.

## 1. lootbox\_simulation.py

### Функція `lootbox_simulation`

```python
import numpy as np

def lootbox_simulation(
    total_items=36,
    initial_collected=None,
    auto_strategy=True,
    switch_threshold=7
):
```

### Опис параметрів

- `total_items` (*int*): Загальна кількість унікальних речей, які необхідно зібрати.
- `initial_collected` (*int*, *optional*): Початкова кількість уже зібраних речей.
- `auto_strategy` (*bool*): Автоматичне вибирання між випадковими та гарантованими ящиками.
- `switch_threshold` (*int*): Поріг, при якому змінюється стратегія з випадкових ящиків на гарантовані.

### Опис логіки роботи

1. Якщо `auto_strategy=True`, вибір між випадковими та гарантованими ящиками відбувається автоматично на основі `switch_threshold`.
2. Якщо `auto_strategy=False`, користувач може самостійно вибирати між двома видами ящиків.
3. Випадковий ящик коштує 2000 од. і має ймовірність видачі нової речі, пропорційну залишку.
4. Гарантований ящик коштує 10000 од. і завжди додає нову річ.
5. Цикл триває, поки всі речі не будуть зібрані.
6. В кінці виводяться загальні витрати гравця.

### Приклад виклику

```python
if __name__ == "__main__":
    lootbox_simulation(initial_collected=0, auto_strategy=False, switch_threshold=16)
```

---

## 2. simulate\_auto\_strategy.py

### Функція `simulate_auto_strategy`

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_auto_strategy(
    total_items=36,
    initial_collected=0,
    switch_threshold=7,
    num_trials=10000
):
```

### Опис параметрів

- `total_items` (*int*): Загальна кількість унікальних речей.
- `initial_collected` (*int*): Початкова кількість зібраних речей.
- `switch_threshold` (*int*): Поріг зміни стратегії на гарантовані ящики.
- `num_trials` (*int*): Кількість ітерацій симуляції для збору статистичних даних.

### Опис логіки роботи

1. Запускається `num_trials` симуляцій збору речей.
2. Для кожної симуляції підраховуються загальні витрати гравця.
3. Всі отримані витрати зберігаються у вигляді масиву `total_costs`.

### Виконання симуляції для різних стратегій

```python
num_trials = 100000

strategy_1_costs = simulate_auto_strategy(switch_threshold=7, num_trials=num_trials)
strategy_2_costs = simulate_auto_strategy(switch_threshold=1, num_trials=num_trials)
strategy_3_costs = simulate_auto_strategy(switch_threshold=10, num_trials=num_trials)
```

### Візуалізація результатів

```python
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
```

### Опис графіку

- Відображає розподіл загальних витрат для трьох стратегій.
- Використовується гістограма для порівняння частоти витрат.
- Графік зберігається у файл `experiment_results.png`.

---

## Висновки

1. Автоматичний вибір між випадковими та гарантованими ящиками дозволяє мінімізувати витрати.
2. Поріг переходу між випадковими та гарантованими ящиками значно впливає на підсумкову вартість збору всіх речей.
3. Візуалізація допомагає зрозуміти оптимальні стратегії для різних випадків.

Цей проект може бути використаний для аналізу ефективності систем випадкових нагород у відеоіграх або азартних механіках.

