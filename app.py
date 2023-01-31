import streamlit as st
import pandas as pd

# Create a selectbox in the sidebar to switch between tabs

@st.cache
def load_data(file_name):
    return pd.read_csv(file_name)

file_name = "Book1.csv"
data = load_data(file_name)



# # Filter data
# if st.checkbox("Filter data"):
#     selected_column = st.selectbox("Pilih kolom", data.columns)
#     # min_value, max_value = st.slider("Batas nilai", data[selected_column].min(), data[selected_column].max())
#     data = data[(data[selected_column] >= min_value) & (data[selected_column] <= max_value)]

# Sort data
tab_selected = st.sidebar.selectbox("Select a tab", ["Tab 1", "Tab 2", "Tab 3"])

# Show the selected tab using an if statement
if tab_selected == "Tab 1":
    st.write("This is Tab 1")
    if st.checkbox("Sort data"):
        sort_by = st.selectbox("Sort by", data.columns)
        sort_order = st.selectbox("Sort order", ["Ascending", "Descending"])
        if sort_order == "Ascending":
            data = data.sort_values(by=sort_by)
        else:
            data = data.sort_values(by=sort_by, ascending=False)

    st.write("Tabel dari file CSV", data)

if tab_selected == "Tab 2":
    st.write("This is Tab 2")
def display_table(data, columns=None):
    if columns is None:
        columns = data.columns
    st.write("Tabel dari file CSV", data[columns])

def select_columns(data):
    columns = st.multiselect("Pilih kolom untuk ditampilkan", data.columns)
    display_table(data, columns)

select_columns(data)

if tab_selected == "Tab 3":
    st.write("This is Tab 3")
