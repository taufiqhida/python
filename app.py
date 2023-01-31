import streamlit as st
import pandas as pd

# @st.cache
# def load_data(file_name):
#     return pd.read_csv(file_name)

# file_name = "Book1.csv"
# data = load_data(file_name)

# # Filter data
# if st.checkbox("Filter data"):
#     selected_column = st.selectbox("Pilih kolom", data.columns)
#     min_value, max_value = st.slider("Batas nilai", data[selected_column].min(), data[selected_column].max())
#     data = data[(data[selected_column] >= min_value) & (data[selected_column] <= max_value)]
# import streamlit as st

# Create a selectbox in the sidebar to switch between tabs
tab_selected = st.sidebar.selectbox("Select a tab", ["Tab 1", "Tab 2", "Tab 3"])

# Show the selected tab using an if statement
if tab_selected == "Tab 1":
    @st.cache
    def load_data(file_name):
        return pd.read_csv(file_name)

    file_name = "Book1.csv"
        data = load_data(file_name)
        st.write("This is Tab 1")if st.checkbox("Sort data"):
        sort_by = st.selectbox("Sort by", data.columns)
        sort_order = st.selectbox("Sort order", ["Ascending", "Descending"])
        if sort_order == "Ascending":
            data = data.sort_values(by=sort_by)
        else:
            data = data.sort_values(by=sort_by, ascending=False)
if tab_selected == "Tab 2":
    st.write("This is Tab 2")

if tab_selected == "Tab 3":
    st.write("This is Tab 3")
# Sort data

st.write("Tabel dari file CSV", data)
