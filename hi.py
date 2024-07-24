import pandas as pd
import numpy as np
import streamlit as st


def corr(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for ite in range(len(x)):
        sum1 += (x[ite] - mean_x) * (y[ite] - mean_y)
        sum2 += (x[ite] - mean_x) ** 2
        sum3 += (y[ite] - mean_y) ** 2
    res = sum1 / (sum2 * sum3) ** 0.5
    return res


def button_func2(data):
    st.bar_chart(data.iloc[:, 1])
    # print(data.iloc[:, 1])
    return


# @st.cache_data(experimental_allow_widgets=True)
def button_func(names, data):
    options = names
    selected_options = []
    options = [option for option in options if option not in selected_options]
    selected_options = st.multiselect('Выберите два варианта:', options)
    st.write(selected_options)
    if len(selected_options) == 2:
        # selected_options = options[0], options[1]
        a = selected_options[0]
        b = selected_options[1]
        st.write(a, b)
        if isinstance(data[a][0], (int, float)) and isinstance(data[b][0], (int, float)):
            res = corr(data[a], data[b])
            # print(r)
            st.write(f'Вы выбрали {selected_options}, корреляция {res}')
    return


def button_func1(data, header):
    table = pd.DataFrame()
    for i in range(len(header)):
        tab = []
        x = data[header[i]].values[:]
        for j in range(len(header)):
            if i == j:
                tab.append(' - ')
            elif i > j:
                tab.append(table[header[j]][i])
            else:
                x1 = data[header[j]].values[:]
                res = corr(x, x1)
                tab.append(res)
        table[header[i]] = tab
    table.index = header
    print(table)
    st.table(table)
    # print(table)
    return


def sorted_by_value(item):
    return item[1]


df = pd.read_csv(r"C:\Users\Excalibur\Downloads\lung_cancer_data.csv", delimiter=',')
df.head()
Survival_Months = df['Survival_Months']
ans = []
max_corr = []
for i in df.columns:
    if i != 'Survival_Months':
        param = df[i]
        if isinstance(param[0], (int, float)):
            r = corr(Survival_Months, param)
            max_corr.append(i)
            ans.append(r)
    else:
        max_corr.append('Survival_Months')
data_out = dict(zip(max_corr, ans))
items = list(data_out.items())
sorted_items = sorted(items, key=sorted_by_value, reverse=True)
result_dict = {k: v for k, v in sorted_items}

selected_calculation = st.selectbox(
    'Выберите тип вычислений:',
    ('корреляция двух выбранных параметров', 'таблица корреляций', 'оба варианта', 'построение гистограмм')
)

if selected_calculation == 'корреляция двух выбранных параметров':
    button_func(max_corr, df)
elif selected_calculation == 'таблица корреляций':
    button_func1(df, max_corr)
elif selected_calculation == 'оба варианта':
    button_func(max_corr, df)
    button_func1(df, max_corr)
elif selected_calculation == 'построение гистограмм':
    button_func2(df)
