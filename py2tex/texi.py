import os
import pandas as pd
import numpy as np
from scipy.stats import t

def texi(files):
    data = pd.read_csv(os.getcwd() + '/' + files)
    # sep = ["&"] * len(data)
    # col_num = 1
    #
    # while col_num <= len(data.columns):
    #
    #     data.insert(col_num, "&", sep)
    #     col_num += 3

    data = data.rename(columns={data.columns[0]: '',
                                data.columns[1]: 'Time without Mom',
                                data.columns[2]: 'Center Based Care',
                                data.columns[3]: 'Goods and Services',
                                data.columns[4]: 'Total'})

    # remove the 'dot' in odd rows of the first column
    odd_row = [row for row in range(len(data.iloc[:, 0])) if row%2 != 0]
    for row in odd_row:
        data.iloc[row, 0] = ''

    col_num = list(range(len(data.columns)-1))

    def pval(x, standard_error, df=800, tail=2):
        pval = t.sf(np.abs((x-0)/standard_error), df) * tail
        return pval

    p_store = odd_row

    # add brackets and stars to all the standard errors
    for col in col_num:
    #    for col in data.iloc[1, 1:]:
         for row in odd_row:

             p_store = pval(data.iloc[row-1, col+1], data.iloc[row, col+1])

             if p_store < 0.01:
                data.iloc[row-1, col+1] = str(round(data.iloc[row-1, col+1], 3)) + '***'
             elif p_store < 0.05:
                data.iloc[row-1, col+1] = str(round(data.iloc[row-1, col+1], 3)) + '**'
             elif p_store < 0.1:
                data.iloc[row-1, col+1] = str(round(data.iloc[row-1, col+1], 3)) + '*'
             else:
                data.iloc[row-1, col+1] = round(data.iloc[row-1, col+1], 3)

             data.iloc[row, col+1] = '(' + str(round(data.iloc[row, col+1], 3)) + ')'

    # col = 1
    # row = 1
    # while col < len(data.columns):
    #     while row < len(data):
    #         a_str = '(' + str(data.iloc[row, col+1]) + ')'
    #         data.iloc[row, col+1] = a_str
    #         row += 2
    #     col += 1

    data.to_latex(os.getcwd() + '/' + files.split('.')[0] + '_output.tex', index=False)

files = [f for f in os.listdir('.') if 'csv' in f.split('.')]
for f in files:
    texi(f)