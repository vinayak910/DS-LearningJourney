import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import matplotlib.pyplot as plt

db = DB() # obj of DB class

st.sidebar.title("Flights Analytics")
user_option = st.sidebar.selectbox('Menu' , ['Check Flights','Analytics'])
if user_option == 'Check Flights':
    st.title('Check Flights')

    col1 , col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source' ,sorted(city))
    with col2:
        destination = st.selectbox('Destination' ,sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(source , destination)
        st.dataframe(results)
else:
    st.title("Analytics")

     # pie chart of airlines flight
    airlines , frequency = db.fetch_airline_info()

    fig = go.Figure(
        go.Pie(labels = airlines,
               values = frequency,
               hoverinfo= "label+percent",
               textinfo = "value")
    )
    st.header("Pie Chart")
    st.plotly_chart(fig)



