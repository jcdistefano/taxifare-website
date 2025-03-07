import streamlit as st
import datetime
import requests

st.markdown('# Welcome to <font color="ff9333">Taxifarinou</font> 🦘',unsafe_allow_html=True)

'''
## Let's travel to a fair price !
'''
cols1=st.columns(2)
with cols1[0]:
    date = st.date_input("When ?",datetime.date(2025, 3, 7))
with cols1[1]:
    time = st.time_input(' ', datetime.time(12, 15))

cols2=st.columns(2)
with cols2[0]:
    pickup_lon = st.number_input('From where lon ?',-73.950655)
with cols2[1]:
    pickup_lat = st.number_input('From where lat ?',40.783282)

cols3=st.columns(2)
with cols3[0]:
    dropoff_lon = st.number_input('Where to lon ?',-73.984365)
with cols3[1]:
    dropoff_lat = st.number_input('Where to lat ?',40.769802)

passenger_count = st.number_input('How many passenger ?',value=1)



url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# 2. Let's build a dictionary containing the parameters for our API...
query = {'pickup_datetime':f"{date} {time}",
         'pickup_longitude':pickup_lon,
         'pickup_latitude':pickup_lat,
         'dropoff_longitude':dropoff_lon,
         'dropoff_latitude':dropoff_lat,
         'passenger_count':passenger_count
         }


# 3. Let's call our API using the `requests` package...
if st.button("Let's go"):
    response = requests.get(url,query).json()
    fare = response['fare']
    # with st.echo():
    #     st.write(type(fare))
    fare = round(float(response['fare']),2)
    st.success(f"Your course will cost €{fare}. Hurry up, go grab your taxi 🦘 and bisous")
