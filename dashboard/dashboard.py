pip install streamlit plotly
import streamlit as st
import pandas as pd
import plotly.express as px

# Load the cleaned CSV files into Pandas DataFrames
day_df = pd.read_csv('day_clean.csv')
hour_df = pd.read_csv('hour_clean.csv')

# Set the title of the dashboard
st.title('Bike Sharing Dashboard')

# --- Overview Section ---
st.header('Overview')
col1, col2, col3 = st.columns(3)
col1.metric("Total Rentals (Day)", day_df['cnt'].sum())
col2.metric("Average Rentals (Day)", round(day_df['cnt'].mean(), 2))
col3.metric("Total Rentals (Hour)", hour_df['cnt'].sum())

# --- Charts Section ---
st.header('Charts')

# Line chart for rentals over time (day)
fig_time_day = px.line(day_df, x='dteday', y='cnt', title='Rentals Over Time (Day)')
st.plotly_chart(fig_time_day)

# Line chart for rentals over time (hour)
fig_time_hour = px.line(hour_df, x='hr', y='cnt', color='weekday', 
                        title='Rentals Over Time (Hour)', 
                        labels={'hr': 'Hour', 'cnt': 'Count', 'weekday': 'Weekday'})
st.plotly_chart(fig_time_hour)

# Scatter plot for rentals vs temperature (day)
fig_temp_day = px.scatter(day_df, x='temp', y='cnt', color='season', 
                          trendline='ols',
                          title='Rentals vs Temperature (Day)',
                          labels={'temp': 'Temperature', 'cnt': 'Count', 'season': 'Season'})
st.plotly_chart(fig_temp_day)

# Bar chart for rentals by season (day)
fig_season_day = px.bar(day_df, x='season', y='cnt', color='weathersit', 
                         title='Rentals by Season (Day)',
                         labels={'season': 'Season', 'cnt': 'Count', 'weathersit': 'Weather'})
st.plotly_chart(fig_season_day)

# --- Data Section ---
st.header('Data')
st.subheader('Day Data')
st.dataframe(day_df)

st.subheader('Hour Data')
st.dataframe(hour_df)