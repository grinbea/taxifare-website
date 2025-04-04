import streamlit as st
import requests
import datetime

st.title("Taxifare Model")

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
st.text_input("Pickup location")
st.text_input("Dropoff location")
st.date_input("Time", datetime.date(2019, 7, 6))
st.number_input('Persons')

if st.button('Submit'):
#    params = { "pickup_datetime":date,
#               "pickup_longitude":-73.950655,
#               "pickup_latitude": 40.783282,
#               "dropoff_longitude": -73.984365,
#               "dropoff_latitude": 40.769802,
#               "passenger_count":  npers}
    params = { "pickup_datetime":"2014-07-06 19:18:00",
               "pickup_longitude":-73.950655,
               "pickup_latitude": 40.783282,
               "dropoff_longitude": -73.984365,
               "dropoff_latitude": 40.769802,
               "passenger_count":  1}

    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url,params=params)

    if response.status_code == 200:
        st.markdown("Your fare is " + str(response.json()['fare']))

