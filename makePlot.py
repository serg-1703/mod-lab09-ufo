import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LogLocator


def read_data(filename):
    n_values = []
    err_values = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                n = int(parts[0])
                err = float(parts[1].replace(',', '.'))
                n_values.append(n)
                err_values.append(err)
    return n_values, err_values


def plot_err_vs_n(n_values, err_values, output_file='plot_enhanced.png'):
    plt.figure(figsize=(12, 8), facecolor='#f5f5f5')
    ax = plt.subplot(111)
    ax.set_facecolor('#fafafa')

    # Основной график с улучшенным стилем
    plt.plot(n_values, err_values,
             color='#e63946',
             marker='D',
             markersize=8,
             markerfacecolor='#1d3557',
             markeredgewidth=1.5,
             markeredgecolor='#1d3557',
             linewidth=2.5,
             linestyle='--',
             label='Ошибка аппроксимации',
             zorder=3)

    # Закрашенная область под кривой
    plt.fill_between(n_values, err_values,
                     color='#a8dadc',
                     alpha=0.4,
                     zorder=1)

    # Горизонтальная линия для минимальной ошибки
    min_err = min(err_values)
    plt.axhline(y=min_err,
                color='#457b9d',
                linestyle='-.',
                linewidth=1.5,
                label=f'Минимум: {min_err:.2e}')

    # Аннотация для точки с минимальной ошибкой
    min_index = err_values.index(min_err)
    plt.annotate(f'Лучшее значение: n={n_values[min_index]}\nОшибка={min_err:.2e}',
                 xy=(n_values[min_index], err_values[min_index]),
                 xytext=(n_values[min_index] + 0.5, err_values[min_index] * 3),
                 arrowprops=dict(facecolor='#1d3557', shrink=0.05, width=1.5),
                 bbox=dict(boxstyle="round,pad=0.5", fc="#f1faee", ec="#1d3557", lw=1.5))

    # Настройка осей и шкал
    plt.yscale('log')
    plt.xlabel('Количество членов ряда (n)', fontsize=12, fontweight='bold')
    plt.ylabel('Ошибка аппроксимации (log scale)', fontsize=12, fontweight='bold')
    plt.title('Зависимость ошибки аппроксимации от количества членов ряда',
              fontsize=14,
              fontweight='bold',
              pad=20)

    # Настройка сетки и пределов
    plt.grid(True, which="both", linestyle='--', alpha=0.7, color='#c7d5e0')
    plt.xlim(min(n_values) - 0.5, max(n_values) + 0.5)

    # Улучшенная легенда
    plt.legend(loc='upper right', frameon=True, framealpha=0.9,
               facecolor='#edf2f4', edgecolor='#2b2d42')

    # Настройка тиков
    plt.xticks(np.arange(min(n_values), max(n_values) + 1, step=1), fontsize=10)
    ax.yaxis.set_major_locator(LogLocator(numticks=15))
    ax.yaxis.set_minor_locator(LogLocator(subs=np.arange(1.0, 10.0) * 0.1, numticks=50))

    # Сохранение 
    plt.savefig(output_file, dpi=350, bbox_inches='tight', facecolor='#f5f5f5')
    plt.close()


if __name__ == "__main__":
    input_filename = 'result/data.txt'
    output_filename = 'result/plot.png'

    n_values, err_values = read_data(input_filename)
    plot_err_vs_n(n_values, err_values, output_filename)

    print(f"Улучшенный график сохранен как {output_filename}")