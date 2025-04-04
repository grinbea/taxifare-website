import streamlit as st
import requests
import datetime

st.title("Taxifare Model")

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
from = st.text_input("Pickup location")
to   = st.text_input("Dropoff location")
date = st.date_input("Time", datetime.date(2019, 7, 6))
nper = st.number_input('Persons')

# Your Mapbox Access Token
access_token = 'your_mapbox_access_token'

# Define the search text and endpoint
search_text = "New York, USA"
url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{search_text}.json"

# Parameters for the request
params = {
    'access_token': access_token,
    'limit': 5,  # Limit the number of results returned
    'country': 'us'  # Limit search to the USA
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    for feature in data['features']:
        st.markdown(f"Place Name: {feature['place_name']}")
        st.markdown(f"Coordinates: {feature['geometry']['coordinates']}")
    else:
        st.markdown("Error:", response.status_code)


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

