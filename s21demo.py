import pandas as pd
import streamlit as st
import plotly.express as px
# import matplotlib.pyplot as plt
# import clickhouse_driver


def cluster_info(name, data):
    time = list(set(data[data['cluster'] == name]['timestamp']))
    for i1 in range(len(time)):
        data_time_local = time[i1]
        space1 = time[i1].rfind(' ')
        time[i1] = data_time_local[space1 + 1:]
        space1 = time[i1].rfind('.')
        time[i1] = time[i1][:space1]
    output = data[data['cluster'] == name]['visitors_count']
    fig = px.scatter(data, x=time, y=output)
    st.plotly_chart(fig)
    return


def campus_info(name, data, book, campus_book):
    num = campus_book.index(name)
    time = list(set(data[data['campus'] == name]['timestamp']))
    for i1 in range(len(time)):
        data_time_local = time[i1]
        space1 = time[i1].rfind(' ')
        time[i1] = data_time_local[space1 + 1:]
    time = sorted(time)
    time = time[::len(book[num])]
    for i1 in range(len(time)):
        data_time_local = time[i1]
        space1 = time[i1].rfind('.')
        time[i1] = data_time_local[:space1]
    output = [0] * len(data[data['campus'] == name])
    for i1 in book[num]:
        inp = list(data[data['cluster'] == i1]['visitors_count'])
        for j1 in range(len(inp)):
            output[j1] += inp[j1]
    output = [item for item in output if item != 0]
    fig = px.scatter(data, x=time, y=output)
    st.plotly_chart(fig)
    return


def all_cluster_stat(book1, df1, campus1):
    for i1 in range(len(book1)):
        for j1 in range(len(book1[i1])):
            temp_clus = book1[i1][j1]
            st.write(f' студентов в среднем  = '
                  f'{round(df1[df1['cluster'] == temp_clus]['visitors_count'].sum() 
                           / data_cluster.count(temp_clus), 1)}'
                  f', кампус - {campus1[i1]}, кластер - {temp_clus}')
    return


def all_campus_stat(campus1, df1):
    for i1 in range(len(campus1)):
        st.write(f' студентов в среднем = '
            f'{round(df1[df1['campus'] == campus1[i1]]['visitors_count'].sum() 
                     / data_campus.count(campus1[i1]), 1)}'
            f', кампус - {campus1[i1]}')
    return


df = pd.read_csv(r"D:\visitors_log (2).csv", delimiter=',')
data_campus = list(df.iloc[:, 2])
campus = sorted(list(set(data_campus)))
data_cluster = list(df.iloc[:, 3])
cluster = list(set(data_cluster))
data_student = list(df.iloc[:, 4])
TEST = sorted(list(set(df.iloc[:, 2] + ' ' + df.iloc[:, 3])))
BOOK = []
counter2 = 0
for i in campus:
    counter1 = 0
    row = []
    for j in TEST:
        if i in j:
            space = j.rfind(' ')
            cluster_name = j[space + 1:]
            row.append(cluster_name)
            counter1 += 1
    BOOK.append(row)
    counter2 += 1
selected_calculation = st.selectbox('choose data:', ('mean cluster', 'mean campus', 'exact cluster', 'exact campus'))
if selected_calculation == 'mean cluster':
    all_cluster_stat(BOOK, df, campus)
elif selected_calculation == 'mean campus':
    all_campus_stat(campus, df)
elif selected_calculation == 'exact cluster':
    selected_cluster = st.selectbox('choose cluster:', sorted(cluster))
    cluster_info(selected_cluster, df)
elif selected_calculation == 'exact campus':
    selected_campus = st.selectbox('choose  campus:', sorted(campus))
    campus_info(selected_campus, df, BOOK, campus)
