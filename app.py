import streamlit as st
import pandas as pd

@st.cache
def load_data(file_name):
    return pd.read_csv(file_name)

file_name = "Book1.csv"
data = load_data(file_name)

def display_table(data, columns=None):
    if columns is None:
        columns = data.columns
    st.write("Tabel dari file CSV", data[columns])

def select_columns(data):
    columns = st.multiselect("Pilih kolom untuk ditampilkan", data.columns)
    display_table(data, columns)

select_columns(data)


# # Filter data
# if st.checkbox("Filter data"):
#     selected_column = st.selectbox("Pilih kolom", data.columns)
#     # min_value, max_value = st.slider("Batas nilai", data[selected_column].min(), data[selected_column].max())
#     data = data[(data[selected_column] >= min_value) & (data[selected_column] <= max_value)]

# Sort data
if st.checkbox("Sort data"):
    sort_by = st.selectbox("Sort by", data.columns)
    sort_order = st.selectbox("Sort order", ["Ascending", "Descending"])
    if sort_order == "Ascending":
        data = data.sort_values(by=sort_by)
    else:
        data = data.sort_values(by=sort_by, ascending=False)

st.write("Tabel dari file CSV", data)
