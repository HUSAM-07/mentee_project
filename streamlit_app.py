import streamlit as st
import pandas as pd

# Sample data for demonstration purposes
data = {
    'Store': ['Store A', 'Store B', 'Store C'],
    'Product Name': ['Product X', 'Product Y', 'Product Z'],
    'Placement Date': ['2023-09-01', '2023-09-02', '2023-09-03'],
    'Retailer Rating': [4, 5, 3],
    'Distributor Rating': [4, 3, 5]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Streamlit app
st.title("Product Placement Tracking Dashboard")

# Sidebar for Retailer and Distributor selection
user_type = st.sidebar.radio("Select User Type:", ("Retailer", "Distributor"))

# Filter data based on user type
if user_type == "Retailer":
    st.header("Retailer Dashboard")
    st.write("Welcome, Retailer!")
    st.write("Here's the product placement data for your stores:")
    st.table(df[['Store', 'Product Name', 'Placement Date', 'Retailer Rating']])
else:
    st.header("Distributor Dashboard")
    st.write("Welcome, Distributor!")
    st.write("Here's the product placement data for your distribution:")
    st.table(df[['Store', 'Product Name', 'Placement Date', 'Distributor Rating']])
