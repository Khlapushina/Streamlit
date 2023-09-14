import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
# path = '../learning/datasets/tips.csv'

tips = pd.read_csv(path)

st.write("""
# Гистограмма общего счета
""")
num_orders = st.sidebar.slider('Выберите количество заказов', 1, len(tips), 100)
selected_tips = tips.head(num_orders)

f1 = px.histogram(selected_tips, x='total_bill', nbins=20, title='Гистограмма общего счета')
st.plotly_chart(f1)

st.write("""
## Связь между общим счетом и чаевыми
""")

f2 = px.scatter(selected_tips, x='total_bill', y='tip', title='Связь между общим счетом и чаевыми')
st.plotly_chart(f2)

st.write("""
## График, связывающий общий счет, чаевые и размер
""")
df04_7_total_bill = tips.groupby('size', as_index=False)['total_bill'].mean()
df04_7_total_bill
df04_7_tip = tips.groupby('size', as_index=False)['tip'].mean()
df04_7_tip

f3 = px.scatter(selected_tips, x=df04_7_total_bill['total_bill'], y=df04_7_tip['tip'], title='График, связывающий общий счет, чаевые и размер')
st.plotly_chart(f3)
st.write("""
## Связь между днем недели и размером счета
""")
         

days = selected_tips.groupby('day')['total_bill'].sum()

f4 = px.bar(days, x=days.index, y='total_bill', title='Связь дня недели и размера счета')
st.plotly_chart(f4)

st.write("""
## График с днем недели по оси У, чаевыми по оси Х и цветом по полу
""")
f5 = px.scatter(selected_tips, x='tip', y='day', color='sex', title='График чаевых по дню недели относительно пола')
st.plotly_chart(f5)


st.write("""
## Сумма всех счетов за каждый день по времени
""")
f6 = px.box(selected_tips, x='day', y='total_bill', color='time', title='Box Plot: Сумма счетов по дням и времени')
st.plotly_chart(f6)

st.write("""
## Гистограммы чаевых на обед и ужин
""")
df_dinner = tips[tips['time']=='Dinner']
df_lunch = tips[tips['time']=='Lunch']
f7 = plt.figure()
sns.histplot(df_dinner['tip'], alpha=0.5, label='Чаевые на обед')
sns.histplot(df_lunch['tip'], alpha=0.5, label='Чаевые на ужин')
st.pyplot(f7)


st.write("""
## Связь размера счета и чаевых для курящих и некурящих
""")
dfm_12 = tips[tips['sex']=='Male']
dff_12 = tips[tips['sex']=='Female']
dfm_12_0 = dfm_12[dfm_12['smoker']=='No']
dfm_12_1 = dfm_12[dfm_12['smoker']=='Yes']
dff_12_0 = dff_12[dff_12['smoker']=='No']
dff_12_1 = dff_12[dff_12['smoker']=='Yes']

f8 = plt.figure(figsize=(20, 5))
plt.subplot(1, 2, 1)
plt.title('Male')
plt.scatter(dfm_12_0['total_bill'], dfm_12_0['tip'], c='lightblue', label = 'No smoker')
plt.scatter(dfm_12_1['total_bill'], dfm_12_1['tip'], c='grey', label = 'Smoker')
plt.xlabel('Total bill')
plt.ylabel('Tips')
plt.legend()
plt.subplot(1, 2, 2)
plt.title('Female')
plt.scatter(dff_12_0['total_bill'], dff_12_0['tip'], c='lightblue', label = 'No smoker')
plt.scatter(dff_12_1['total_bill'], dff_12_1['tip'], c='grey', label = 'Smoker')
plt.xlabel('Total bill')
plt.ylabel('Tips')
plt.legend()
st.pyplot(f8)




