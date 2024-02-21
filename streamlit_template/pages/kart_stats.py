import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_karts = pd.read_csv('data/kart_stats.csv')

# st.dataframe(df_karts)

df_karts = df_karts[['Body','Ground Speed','Ground Handling','Acceleration','Mini-Turbo','Weight']]

st.dataframe(df_karts.style
             .highlight_max(color='lightgreen', axis=0,subset=['Ground Speed','Ground Handling','Acceleration','Mini-Turbo','Weight'])
             .highlight_min(color='red', axis=0,subset=['Ground Speed','Ground Handling','Acceleration','Mini-Turbo','Weight'])
)

st.line_chart(df_karts, x='Weight', y=['Ground Speed','Acceleration'])

st.bar_chart(df_karts, x='Body',y=['Ground Handling','Mini-Turbo'])

st.header('Individual Kart Stats')

chosen_kart = st.selectbox('Pick a Kart', df_karts['Body'])

df_single_kart = df_karts.loc[df_karts['Body'] == chosen_kart]

df_single_kart = df_single_kart.drop(columns=['Body'])

df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')

if st.checkbox('Show All Karts'):
    st.bar_chart(df_karts, x='Body',y=['Ground Speed','Ground Handling','Acceleration','Mini-Turbo','Weight'])