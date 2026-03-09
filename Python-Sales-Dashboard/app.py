import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")

st.title("🛒 Supermarket Sales Dashboard")
st.markdown("Analyze supermarket sales data interactively with Python & Streamlit")

# File uploader
file = st.file_uploader("Upload Supermarket Sales dataset (CSV)", type="csv")

if file:
    df = pd.read_csv(file)
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Basic stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Sales by Branch
    if 'Branch' in df.columns and 'Total' in df.columns:
        st.subheader("Total Sales by Branch")
        branch_sales = df.groupby('Branch')['Total'].sum()
        st.bar_chart(branch_sales)

    # Gender distribution
    if 'Gender' in df.columns:
        st.subheader("Customer Gender Distribution")
        gender_count = df['Gender'].value_counts()
        st.bar_chart(gender_count)

    # Payment method distribution
    if 'Payment' in df.columns:
        st.subheader("Payment Method Distribution")
        payment_count = df['Payment'].value_counts()
        st.bar_chart(payment_count)

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
