import functools
import streamlit as st

tab_selected = st.sidebar.selectbox("Select a tab", ["Minuman", "Makanan", "Tab 3"])

if tab_selected == "Minuman":
    data = [
        {"nama": "Espresso", "harga": 15000, "rating": 4.5},
        {"nama": "Coffe Latte", "harga": 16000, "rating": 4.8},
        {"nama": "Cappuccino", "harga": 17000, "rating": 4.7},
        {"nama": "Mochachino", "harga": 18000, "rating": 4.6},
        {"nama": "American Coffee", "harga": 16000, "rating": 4.4},
        {"nama": "Red Velvet", "harga": 21000, "rating": 4.8},
        {"nama": "Thai Tea", "harga": 15000, "rating": 4.5},
        {"nama": "Juice Avacado", "harga": 14000, "rating": 4.4},
        {"nama": "Vanila Latte", "harga": 15000, "rating": 4.7},
        {"nama": "Lemon Tea", "harga": 7000, "rating": 4.7},
        {"nama": "Orange Blue", "harga": 18000, "rating": 4.8},
        {"nama": "Greentea Cookies Vanila", "harga": 20000, "rating": 5.0},
        {"nama": "Choco Oreo", "harga": 20000, "rating": 5.0},
    ]

    def filter_data(data, harga_minimum, harga_maksimum, rating_minimum):
        data_harga = list(filter(lambda x: harga_minimum <= x["harga"] <= harga_maksimum, data))
        data_rating = list(filter(lambda x: x["rating"] >= rating_minimum, data_harga))
        return data_rating

    def main():
        st.title("Amalia Diner Menu")
        st.write("Berikut adalah menu cafe Amalia Diner:")

        harga_minimum = st.number_input("Masukkan harga minimum:", value=5000, step=1000)
        harga_maksimum = st.number_input("Masukkan harga maksimum:", value=8000, step=1000)
        rating_minimum = st.number_input("Masukkan rating minimum:", value=4.5, step=0.1)

        filtered_data = filter_data(data, harga_minimum, harga_maksimum, rating_minimum)

        st.write("Hasil filter:")
        for item in filtered_data:
            st.write("-", item["nama"], "Rp", item["harga"], "rating", item["rating"])

    if __name__ == "__main__":
        main()
if tab_selected == "Makanan":
    data = [
        {"nama": "Rice Bowl Chicken Teriyaki", "harga": 30000, "rating": 4.7},
        {"nama": "Rice Bowl Chicken Sambel Matah", "harga": 30000, "rating": 4.7},
        {"nama": "Tokyo Savory Ramen", "harga": 32000, "rating": 4.8},
        {"nama": "Otsu Spicy Ramen", "harga": 32000, "rating": 4.8},
        {"nama": "Nara Sweet Ramen", "harga": 32000, "rating": 4.5},
        {"nama": "Spaghetti Carbonara", "harga": 28000, "rating": 4.8},
        {"nama": "Spaghetti Aglio Olio", "harga": 27000, "rating": 4.5},
        {"nama": "Spaghetti Bolognese", "harga": 28000, "rating": 4.8},
        {"nama": "Nasi Ayam Bakar", "harga": 16000, "rating": 4.8},
        {"nama": "Nasi Ayam Goreng Rendang", "harga": 22000, "rating": 4.7},
        {"nama": "Nasi Ayam Geprek Bakar", "harga": 18000, "rating": 4.8},
        {"nama": "Nasi Goreng Gila", "harga": 18000, "rating": 4.8},
        {"nama": "Mie Goreng Jawa", "harga": 16000, "rating": 4.7},
    ]

    def filter_data(data, harga_minimum, harga_maksimum, rating_minimum):
        data_harga = list(filter(lambda x: harga_minimum <= x["harga"] <= harga_maksimum, data))
        data_rating = list(filter(lambda x: x["rating"] >= rating_minimum, data_harga))
        return data_rating

    def main():
        st.title("Amalia Los Menu")
        st.write("Berikut adalah menu cafe Amalia Diner:")

        harga_minimum = st.number_input("Masukkan harga minimum:", value=5000, step=1000)
        harga_maksimum = st.number_input("Masukkan harga maksimum:", value=8000, step=1000)
        rating_minimum = st.number_input("Masukkan rating minimum:", value=4.5, step=0.1)

        filtered_data = filter_data(data, harga_minimum, harga_maksimum, rating_minimum)

        st.write("Hasil filter:")
        for item in filtered_data:
            st.write("-", item["nama"], "Rp", item["harga"], "rating", item["rating"])

    if __name__ == "__main__":
        main()
