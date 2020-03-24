import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

YEAR_DAYS = 366
MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
GOAL = 250


def prepare_ideal_burndown():
    months = [datetime.strptime(f'{d} 2020', '%m %Y').strftime('%B %Y') for d in range(1, 13)]
    goal = [m * GOAL / YEAR_DAYS for m in reversed(range(YEAR_DAYS))]

    plt.figure(figsize=(10, 7))

    plt.plot(range(YEAR_DAYS), goal, label='Kurs i ścieżka')

    plt.xticks(rotation=45)

    axes = plt.gca()
    tick_days = [0]
    tick_days.extend(MONTH_DAYS[:12])
    axes.set_xticks(np.cumsum(tick_days))
    axes.set_xticklabels(months)

    axes.set_xlim([0, YEAR_DAYS - 1])
    axes.set_ylim([0, GOAL])


if __name__ == '__main__':
    prepare_ideal_burndown()

    read_days_january = [1, 1, 3, 4, 4, 9, 10, 11, 12, 15, 15, 16, 18, 20,
                         22, 23, 24, 24, 24, 24, 28, 30, 30, 30, 31, 31]
    read_days_january = np.array(read_days_january) - 1
    read_days_january = read_days_january.tolist()

    read_days_february = [10, 12, 12, 13, 15, 15, 15, 19, 20, 21, 22, 26, 27]
    read_days_february = np.array(read_days_february) - 1 + 31
    read_days_february = read_days_february.tolist()

    read_days_march = [1, 2, 6, 6, 7, 9, 13, 13, 13, 16, 16, 23, 24, 24]
    read_days_march = np.array(read_days_march) - 1 + 31 + 29
    read_days_march = read_days_march.tolist()

    read = read_days_january + read_days_february + read_days_march
    passed_days = 31 + 29 + 24

    read_plot = []
    for i in range(passed_days):
        read_plot.append(GOAL - len([el for el in read if el <= i]))

    plt.plot(range(passed_days), read_plot, label='Przeczytane')

    plt.legend()
    plt.show()
