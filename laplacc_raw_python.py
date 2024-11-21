import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys
import time
def laplace_2d_python(grid, max_iter=1, tol=1e-5):
    """
    Решение уравнения Лапласа методом итераций Гаусса-Зейделя.
    
    :param grid: Начальная сетка (с граничными условиями).
    :param max_iter: Максимальное количество итераций.
    :param tol: Порог сходимости.
    :return: Модифицированная сетка после стабилизации.
    """
    rows, cols = len(grid), len(grid[0])
    for _ in range(max_iter):
        max_diff = 0  # Максимальное изменение за итерацию
        
        # Обновляем внутренние точки сетки
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                old_value = grid[i][j]
                grid[i][j] = 0.25 * (
                                  grid[i + 1][j] 
                                + grid[i - 1][j] 
                                + grid[i][j + 1] 
                                + grid[i][j - 1])
                
                max_diff = max(max_diff, abs(grid[i][j] - old_value))
        
        # Проверяем сходимость
        if max_diff < tol:
            break
    return grid


# Инициализация сетки с граничными условиями
N, M = 20, 20  # Размеры сетки
grid = [[0.0 for _ in range(M)] for _ in range(N)]

# Пример граничных условий: левая сторона = 100, остальные = 0
for i in range(N):
    grid[i][0] = 100.0

states = []
# Запускаем расчёт
result_python = laplace_2d_python(grid)
states.append(result_python)
# Возвращаем итоговое распределение
#for line in result_python:
#    for el in line:
#        print(f'{el:6.3f}', end=' ')
#    print()
# states.append(result_python)
for _ in range(100):
    # print(states)
    states.append(laplace_2d_python(states[-1]))
    time.sleep(0.5)
# print(states[-1])
# print(states[0])

fig, ax = plt.subplots()
for state in states:
    im = ax.imshow(state, cmap='hot', interpolation='nearest')
    plt.show()
# def update(frame):
#     im.set_array(frame)
#     return [im]


# ani = FuncAnimation(fig, update, frames=states, interval=1500, blit=True)
plt.colorbar(im, ax=ax)
plt.title("Динамика температуры")
plt.show()
