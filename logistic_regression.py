# QBA LIU 2023 ------------------------------------------------------------------------------------------------------------------

import warnings
from itertools import combinations
import pandas as pd
import numpy as np
import statsmodels.api as sm

# reading the data --------------------------------------------------------------------------------------------------------------------
full_data = pd.read_csv("C:/Users/Lenovo/Desktop/STUDIA/BIOINFORMATYKA/METYLACJA/KLASYFIKACJA/full_data.csv")
full_data.drop(full_data.columns[0], axis = 1, inplace=True)
full_data = full_data.dropna()

# creating the dependent and independent variable vectors -------------------------------------------------------------
y = np.array(full_data['Match/MissMatch'])
X = full_data.drop(full_data.columns[[0,1]], axis=1)

# creating all possible independent variable vectors --------------------------------------------------------------------------
sample_list = X.columns
list_combinations = list()
for n in range(len(sample_list) + 1):
    list_combinations += list(combinations(sample_list, n))
combinations = list(list_combinations)

# choosing the model that has only significant variables --------------------------------------------------------
warnings.filterwarnings("ignore")
for i in combinations:
    X_new = X[X.columns.intersection(list(i))]
    model = sm.GLM(y, sm.add_constant(X_new), family=sm.families.Binomial())
    results = model.fit()
    values = []
    for i in range(0, len(results.pvalues)):
        if results.pvalues[i] <= 0.05:
            values.append(True)
        else:
            values.append(False)
    if all(values) == True:
        print(results.summary())
        print('_____________________________________')