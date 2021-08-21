import streamlit as st
import plotly.express as px
from data.all_data import *
from data.district import *
from data.neigh import *

st.title("My Barcelona population dashboard")
st.subheader("This dashboard shows information about the population of Barcelona in 2017.")

st.text("")
st.text("Here's a sample of the dataset.")
st.dataframe(df_show.head())
st.text("")
st.plotly_chart(px.bar(df, x="s_age", y="Number", color="Gender", labels={"s_age": "Quinquenal ages", "Number":"Inhabitants"},title="Population by gender and quinquenal ages"),use_container_width=True)
st.text("")
st.header("Barcelona districts")
col1, col2 = st.columns(2)
with col1:
    st.text("")
    st.text("")
    st.text("")
    st.plotly_chart(px.pie(df_dist(), values="Number", names="District_Name", title="Population by District"),use_container_width=True)

with col2:
    selection = st.selectbox("Select a district to see population by gender", ["Ciutat Vella","Eixample","Sants-Montjuïc","Les Corts","Sarrià-Sant Gervasi","Gràcia","Horta-Guinardó","Nou Barris","Sant Andreu","Sant Martí"])
    st.plotly_chart(px.pie(gend_dist(selection), values="Number", names="Gender"), use_container_width=True)

st.header("Barcelona neighborhoods")
st.plotly_chart(px.bar(df_neigh(), x="Neighborhood_Name", y="Number", color="Gender",labels={"Number":"Inhabitants", "Neighborhood_Name":""}, title=f"Population by neighborhood", orientation="v", height=650), use_container_width=True)

st.text("")
st.subheader("Neighborhood Codes")
st.dataframe(df_neigh()[["Neighborhood_Name", "Neighborhood_Code"]].drop_duplicates())
st.text("")

slid = st.slider("Select a code to see the corresponding neighborhood", 1, 73)
neigh_df = age_neigh(slid)
name = neigh_df["Neighborhood_Name"].unique()[0]
c_orders = {"Age": ages} 
st.plotly_chart(px.bar(neigh_df, x="Number", y="Age", color="Gender",labels={"Age": "Quinquenal ages", "Number":"Inhabitants"}, title=f"Population by gender and quinquenal ages of {name}", category_orders=c_orders, orientation="h", height=500),use_container_width=True)