import streamlit as st
import pandas as pd

st.header("Exoplanet explorer!")
st.subheader("Select a station to view the data")
st.divider()

raw_data = pd.read_csv('data/PSCompPars_2023.09.06_16.02.03.csv')
stations = raw_data['disc_facility'].sort_values().unique()

option = st.selectbox("Choose a station", stations)

st.write("You selected:", option)

# pl_bmasse, sy_dist

st.write("This is a Streamlit app created by a Python script.")
filtered_df = raw_data.query("disc_facility == @option")
st.write(filtered_df)
#st.scatter_chart(filtered_df['pl_bmasse'], filtered_df['sy_dist'])
#st_mass
st.scatter_chart(
    filtered_df,
    x='sy_dist',
    y='st_logg',
    size='pl_bmasse'
)

st.subheader("What is an exoplanet?")
st.video("https://www.youtube.com/watch?v=0ZOhJe_7GrE")
