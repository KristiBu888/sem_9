# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей
# от 0 до 500 (population)и сохранить ее в переменную avg.
# Используйте модуль pandas.

import pandas as pd
import warnings

warnings.filterwarnings('ignore')

file = 'california_housing_train.csv'
df = pd.read_csv(file)
avg = df[df['population'] < 500].median_house_value.mean()
print(avg)
