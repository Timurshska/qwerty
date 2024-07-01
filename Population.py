import matplotlib.pyplot
import numpy as np
import pandas as pd


def corr(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(len(x)):
        sum1 += (x[i] - mean_x) * (y[i] - mean_y)
        sum2 += (x[i] - mean_x) ** 2
        sum3 += (y[i] - mean_y) ** 2
    r = sum1/(sum2 * sum3) ** 0.5
    return r

df = pd.read_csv("https://raw.githubusercontent.com/aiedu-courses/all_datasets/main/Population.csv", delimiter=';')
df.head()
years = df.columns[1:].astype(int)
population_Croatia = df[df['Country Name'] == 'Croatia'].values[0][1:]
population_Bulgaria = df[df['Country Name'] == 'Bulgaria'].values[0][1:]
matplotlib.pyplot.plot(years, population_Bulgaria)
matplotlib.pyplot.show()
maxi = []
r = 0
max_row = []
for country in df['Country Name']:
    if country != 'Bulgaria':
        population = df[df['Country Name'] == country].values[0][1:]
        r = corr(population_Bulgaria, population)
        max_row.append(country)
        maxi.append(r)
for i in range(len(maxi)):
    for j in range(i, len(maxi)):
        if maxi[i] < maxi[j]:
            c = maxi[i]
            maxi[i] = maxi[j]
            maxi[j] = c
            c = max_row[i]
            max_row[i] = max_row[j]
            max_row[j] = c
tuples = list(zip(maxi, max_row))
print(tuples)
