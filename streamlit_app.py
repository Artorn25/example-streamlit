import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🎈 Data Science & Visualization App")
st.subheader("Input")
option = st.selectbox(
    "How would you like to input data?",
    ("URL", "Upload"),
    placeholder="Select method to input data",
)

st.write("You selected:", option)

# Initialize a DataFrame
df = pd.DataFrame()

# Handle URL input
if option == "URL":
    url_input = st.text_input("URL", "")
    if url_input:
        try:
            df = pd.read_csv(url_input)
            st.info(f"The URL of your data is: {url_input}")
            st.write(df.head())
        except Exception as e:
            st.error(f"Error loading data: {e}")

# Handle file upload
elif option == "Upload":
    uploaded_files = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=False, type=["csv", "xlsx", "xls"]
    )
    if uploaded_files:
        try:
            if uploaded_files.name.endswith('.csv'):
                df = pd.read_csv(uploaded_files)
            else:
                df = pd.read_excel(uploaded_files)
            st.write("filename:", uploaded_files.name)
            # st.write(df)
        except Exception as e:
            st.error(f"Error loading data: {e}")

# If DataFrame is not empty, proceed
if not df.empty:
    # Display DataFrame information
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Data Cleaning Options
    st.subheader("Data Cleaning")
    if st.checkbox("Show missing values"):
        st.write(df.isnull().sum())

    # Visualization Options
    st.subheader("Data Visualization")
    columns = df.columns.tolist()

    plot_type = st.selectbox("Select plot type", ["Histogram", "Scatter Plot", "Line Chart"])

    if plot_type == "Histogram":
        column = st.selectbox("Select column for histogram", columns)
        bins = st.slider("Select number of bins", 5, 50, 10)
        plt.figure(figsize=(10, 5))
        plt.hist(df[column].dropna(), bins=bins)
        plt.title(f"Histogram of {column}")
        st.pyplot(plt)

    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("Select X axis column", columns)
        y_col = st.selectbox("Select Y axis column", columns)
        plt.figure(figsize=(10, 5))
        sns.scatterplot(x=df[x_col], y=df[y_col])
        plt.title(f"Scatter Plot of {x_col} vs {y_col}")
        st.pyplot(plt)

    elif plot_type == "Line Chart":
        x_col = st.selectbox("Select X axis column for line chart", columns)
        y_col = st.selectbox("Select Y axis column for line chart", columns)
        plt.figure(figsize=(10, 5))
        plt.plot(df[x_col], df[y_col])
        plt.title(f"Line Chart of {x_col} vs {y_col}")
        st.pyplot(plt)

    # Custom Query
    st.subheader("Custom Query")
    query = st.text_input("Enter your pandas query (e.g., df[df['column'] > value])")
    if query:
        try:
            query_result = eval(query)
            st.write(query_result)
        except Exception as e:
            st.error(f"Error in query: {e}")
