import streamlit as st
import pandas as pd
df=pd.read_csv('Retail_Cleaned.csv')
st.title('Sales Dashboard')
city=df[['City_Bengaluru','City_Chennai','City_Delhi','City_Hyderabad','City_Jaipur','City_Kolkata','City_Lucknow','City_Mumbai','City_Pune']]
top_cities=city.sum().sort_values(ascending=False)
st.subheader('Top 10 Cities by Customer Count:')
st.bar_chart(top_cities)
st.subheader('Total Sales by Product Category:')
st.bar_chart(df.groupby('ProductCategory')['Quantity'].sum())
st.subheader('Monthly wise Product Sales:')
st.line_chart(df.groupby('Month')['TotalAmount'].sum())