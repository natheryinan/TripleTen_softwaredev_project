import streamlit as st
import pandas as pd
import plotly.express as px

df=pd.read_csv('C:/Users/yangy/TripleTen_softwaredev_project/vehicles_us.csv')


# Set the title of the app
st.title("Car Analysis")

# Header
st.header("Exploratory Data Analysis of Car")

# Histogram
st.subheader("Distribution of Car Prices")
price_hist = px.histogram(df, x='price', nbins=30, title='Distribution of Car Prices')
st.plotly_chart(price_hist)

# Scatter Plot
st.subheader("Price vs. Mileage")
scatter_plot = px.scatter(df, x='odometer', y='price', 
                           title='Price vs. Mileage', 
                           hover_data=['model_year', 'model'])
st.plotly_chart(scatter_plot)

# Checkbox for showing additional details
show_details = st.checkbox("Show Details")
if show_details:
    st.subheader("Data Overview")
    st.write(df.describe())  # Show a summary of the data
