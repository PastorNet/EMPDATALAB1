from funcitons import mx, disp, histogram, np, plt, p, find_broken_data
from scipy.stats import chisquare


def rasp(data, namehist):
    mx_r = mx(data)
    p_r = p(data)
    disp_r = disp(data, mx_r)
    sigma_r = disp_r ** (1 / 2)
    count_broken_data, clear_data = find_broken_data(data, sigma_r)
    if count_broken_data > 0:
        rasp(clear_data, namehist)
    plt.figure()
    hist_obj = histogram(data)
    hist_obj.plot()
    plt.xlabel(xlabel='X')
    plt.ylabel(ylabel='Y')
    plt.title('LR 1 Histogram')
    plt.savefig(namehist)
    plt.show()
    hi = chisquare(data)
    print('X: ' + str(data) + 'Count:' + str(data.size))
    print('Вибіркове середнє:   ' + str(mx_r))
    print('Густина ймовірності (P):   ' + str(p_r))
    print('Вибіркова дисперсія:   ' + str(disp_r))
    print('Точкова оцінка середнього квадратичного:   ' + str(sigma_r))
    print('Xi^2 ( Критерій Пірсена ): ' + str(hi))
    print('Знайдено викидів:' + str(count_broken_data))
    pass


print('======================================================================================')
print('=============================NORMAL===================================================')
print('======================================================================================')
rasp(np.random.normal(size=52), 'normalhist')
print('======================================================================================')
print('===================================REAL===============================================')
print('======================================================================================')
rasp(np.loadtxt("data.txt", delimiter='\b', dtype=np.float), 'realhist')
