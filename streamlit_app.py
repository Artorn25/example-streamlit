import streamlit as st
import pandas as pd

st.title('🎈 App Name')
st.subheader("Input")
option = st.selectbox(
   "How would you like to be method input data?",
   ("URL", "Upload"),
   index=None,
   placeholder="Select method input data",
)

st.write("You selected:", option)
# st.write('Hello world!')
if option == "URL":
    url_input = st.text_input("URL", "")
    if url_input:
        st.info(f"The URL of your data is: {url_input}")
        df = pd.read_csv(url_input)
        st.write(df)
        column_names = df.columns
    else:
     st.error("Awaiting your input:")

elif option == "Upload":
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        # df = pd.read_csv(bytes_data)
        # st.write(df)