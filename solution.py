import pandas as pd
import numpy as np


chat_id = 407415686 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    flag = False
    if ttest_ind(x, y, equal_var=False, alternative=alternative).pvalue >= 0.01:
        flag = True
    return flag # Ваш ответ, True или False
