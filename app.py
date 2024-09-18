import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import pyarrow as pa

df=pd.read_csv('vehicles_us_utf8.csv',encoding='utf-8-sig')



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
    st.table(df.dtypes)
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df = df.dropna(subset=['price'])
    # Explicitly convert to np.float64
    df['price'] = df['price'].astype(np.float64)
    df['model_year'] = df['model_year'].astype(str)  # Convert any mixed type column to string
    df['cylinders'] = df['model_year'].astype(str)
    df['is_4wd'] = df['is_4wd'].astype(str)
    st.table(df.describe(include='all'))  # Show a summary of the data
