import pandas as pd


df = pd.read_json("https://bcn-api.herokuapp.com/")

ages = ['0-4','5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '>=95']

df_show = df.drop(columns=["location", "s_age"])

