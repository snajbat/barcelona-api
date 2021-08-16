import streamlit as st
import requests
import pandas as pd
import json

@st.cache
def age_neigh(neighborhood):
    age_n = requests.get(f"https://bcn-api.herokuapp.com/neighborhood/{neighborhood}").json()
    age_n = json.dumps(age_n)
    return pd.read_json(age_n)



@st.cache
def df_neigh():
    total_neigh = [requests.get(f"https://bcn-api.herokuapp.com/neighborhood/{i}?group=gender").json() for i in range(1,74)]

    lst = [el for n in total_neigh for el in n]
    lst = json.dumps(lst)

    return pd.read_json(lst)