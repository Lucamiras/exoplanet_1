import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

raw_data = pd.read_csv('data/exo_data.csv')
df_pre = raw_data.copy()
df_pre = df_pre.dropna(subset=['st_teff','pl_bmasse'])

# --- APP SPACE --#

st.header("Exoplanet Exploration")
st.divider()
st.subheader("Select an observatory to view planets it discovered.")

unique_facilities = raw_data['disc_facility'].sort_values().unique()

facility_option = st.selectbox("Choose a station", unique_facilities)
df = df_pre.query("disc_facility == @facility_option")

st.write("You selected:", facility_option)

st.write("Below you can see all exoplanets discovered by this station.")

chart = px.scatter(
    df,
    x='disc_year',
    y='sy_dist',
    color='st_teff',
    color_continuous_scale=px.colors.sequential.Bluered_r,
    size='pl_bmasse',
)
#.layout( 
#    title="Exoplanets discovered by " + facility_option,
#    xaxis_title="Discovery Year",
#    yaxis_title="Distance from star",
#    coloraxis_colorbar_title="Temperature (K)",
#)

st.plotly_chart(chart)

st.subheader("What is an exoplanet?")
st.video("https://www.youtube.com/watch?v=0ZOhJe_7GrE")
