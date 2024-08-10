import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_data = st.date_input("PickUp Date", value=datetime.datetime(2014, 7, 6, 19, 18, 00))
pickup_time = st.time_input('PickUp Time', value=datetime.datetime(2014, 7, 6, 19, 18, 00))
pickup_datetime = f'{pickup_data} {pickup_time}'
pickup_longitude = st.number_input('PickUp Longitude', value=-73.950655)
pickup_latitute = st.number_input('PickUp Latitude', value=40.783282)
dropoff_longitude = st.number_input('DropOff Longitude', value=-73.984365)
dropoff_latitute  = st.number_input('DropOff Latitude', value=40.769802)
passenger_count= st.selectbox('Passenger count', range(1, 8))


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'
# url = 'https://taxifare-2e7f3r3ina-uw.a.run.app/predict' #Meuy endereço que será deletado


if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API... '''
with st.echo():
    params = {
        "pickup_datetime":pickup_datetime ,
        "pickup_longitude":pickup_longitude,
        "pickup_latitude":pickup_latitute,
        "dropoff_longitude":dropoff_longitude,
        "dropoff_latitude":dropoff_latitute ,
        "passenger_count":passenger_count,
    }

# st.write(params)

'''
3. Let's call our API using the `requests` package...'''
with st.echo():
    test = requests.get(url, params=params)
    st.write(test.url)
    response = test.json()

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...'''


## Finally, we can display the prediction to the user
with st.echo():
    st.write(test.content.decode('utf-8'))
    st.write(response["fare"])

'''
5. Maps'''

df = pd.DataFrame([[pickup_latitute, pickup_longitude], [dropoff_latitute, dropoff_longitude]],  columns=['lat', 'lon'])
st.write(df)

st.map(df, size=40)

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()
