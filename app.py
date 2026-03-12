import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Supermarket Sales Dashboard")

# Load data
df = pd.read_csv("data/supermarket_sales.csv")

# Show raw data
st.subheader("Raw Data")
st.write(df.head())

# Simple chart
st.subheader("Sales by Product Line")
fig, ax = plt.subplots()
df.groupby("Product line")["Total"].sum().plot(kind="bar", ax=ax)
st.pyplot(fig)
