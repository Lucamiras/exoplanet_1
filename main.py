import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

raw_data = pd.read_csv('data/exo_data.csv')
df1 = raw_data.copy()
df1 = df1.dropna(subset=['st_teff','pl_bmasse'])

# --- APP SPACE --#

st.header("Exoplanet Exploration")
st.divider()
st.subheader("Select a star to view its planets")

unique_facilities = raw_data['disc_facility'].sort_values().unique()

facility_option = st.selectbox("Choose a station", unique_facilities)
df = raw_data.query("disc_facility == @facility_option")

st.write("You selected:", facility_option)

st.write("Below you can see all exoplanets discovered by this station.")

chart = px.scatter(
    df.query("st_teff < 10000"),
    x='disc_year',
    y='sy_dist',
    color='st_teff',
    color_continuous_scale=px.colors.sequential.Bluered_r,
    size='pl_bmasse',
)

st.plotly_chart(chart)

st.subheader("What is an exoplanet?")
st.video("https://www.youtube.com/watch?v=0ZOhJe_7GrE")
