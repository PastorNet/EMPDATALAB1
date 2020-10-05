import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import simps


def find_broken_data(data, sigma):
    i = 0
    j = 0
    srx = 0.0
    anomalies = []
    clear_data = []
    while i < len(data):
        srx += data[i]
        i += 1
    srx_r = (1 / len(data) * srx)
    lower_lim = srx_r - sigma * 3
    upper_lim = srx_r + sigma * 3
    while j < len(data):
        if data[j] > upper_lim or data[j] < lower_lim:
            anomalies.append(data[j])
        else:
            clear_data.append(data[j])
        j += 1
    return len(anomalies), np.array(clear_data)


def p(data):
    p_r_raw = norm.pdf(data)
    return simps(p_r_raw)


def mx(data):
    mx_ = 0.0
    i = 0
    while i < len(data):
        mx_ += data[i]
        i += 1
    return (1 / i) * mx_


def disp(data, mx_):
    i = 0
    disp_ = 0.0
    while i < len(data):
        disp_ += (data[i] - mx_) ** 2
        i += 1
    return (1 / i) * disp_


def histogram(data):
    sns.set_theme()
    ax = sns.distplot(data, kde=True, kde_kws={'kernel':'gau'})
    return ax
