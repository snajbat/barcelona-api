import streamlit as st
import requests
import pandas as pd
import json

@st.cache
def df_dist():
    total_dist = [requests.get(f"https://bcn-api.herokuapp.com/district/{i}?group=total").json() for i in range(1,11)]

    lst = [el for n in total_dist for el in n]
    lst = json.dumps(lst)

    return pd.read_json(lst)

@st.cache
def gend_dist(district):
    gender_dist = requests.get(f"https://bcn-api.herokuapp.com/district/{district}?group=gender").json()
    gender_dist = json.dumps(gender_dist)
    return pd.read_json(gender_dist)