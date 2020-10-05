from funcitons import mx, disp, histogram, np, plt, p
from scipy.stats import chisquare


def rasp(data, namehist):
    mx_r = mx(data)
    p_r = p(data)
    disp_r = disp(data, mx_r)
    sigma_r = disp_r ** (1 / 2)
    plt.figure()
    hist_obj = histogram(data)
    hist_obj.plot()
    plt.xlabel(xlabel='X')
    plt.ylabel(ylabel='Fj/ΔX')
    plt.savefig(namehist)
    plt.show()
    hi = chisquare(data)
    print('X: ' + str(data) + 'Count:' + str(data.size))
    print('Вибіркове середнє:   ' + str(mx_r))
    print('Густина ймовірності (P):   ' + str(p_r))
    print('Вибіркова дисперсія:   ' + str(disp_r))
    print('Точкова оцінка середнього квадратичного:   ' + str(sigma_r))
    print('Xi^2 ( Критерій Пірсена ): ' + str(hi))


rasp(np.loadtxt("data.txt", delimiter='\b', dtype=np.float), 'realhist')
