import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

YEAR_DAYS = 366
MONTH_DAYS = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
GOAL = 250


def prepare_ideal_burndown():
    months = [datetime.strptime(f'{d} 2020', '%m %Y').strftime('%B %Y') for d in range(1, 13)]
    goal = [m * GOAL / YEAR_DAYS for m in reversed(range(YEAR_DAYS))]

    plt.figure(figsize=(10, 7))

    plt.plot(range(YEAR_DAYS), goal, label='Cel')

    plt.xticks(rotation=45)

    axes = plt.gca()
    tick_days = [0]
    tick_days.extend(MONTH_DAYS)
    axes.set_xticks(np.cumsum(tick_days))
    axes.set_xticklabels(months)

    axes.set_xlim([0, YEAR_DAYS - 1])
    axes.set_ylim([0, GOAL])


if __name__ == '__main__':
    read_days_diary = {
        'january': [1, 1, 3, 4, 4, 9, 10, 11, 12, 15, 15, 16, 18, 20, 22, 23, 24, 24, 24, 24, 28, 30, 30, 30, 31, 31],
        'february': [10, 12, 12, 13, 15, 15, 15, 19, 20, 21, 22, 26, 27],
        'march': [1, 2, 6, 6, 7, 9, 13, 13, 13, 16, 16, 23, 24, 24, 24]
    }

    read_days = []
    for month_number, month_read_days in enumerate(read_days_diary.values()):
        day_shift = sum([MONTH_DAYS[i] for i in range(month_number)])
        corrected_month_days = np.array(month_read_days) - 1 + day_shift
        read_days.extend(corrected_month_days.tolist())

    prepare_ideal_burndown()
    days_passed = time.localtime().tm_yday

    read_plot = []
    for i in range(days_passed):
        read_plot.append(GOAL - len([el for el in read_days if el <= i]))

    plt.plot(range(days_passed), read_plot, label='Przeczytane')

    plt.legend()
    plt.show()
