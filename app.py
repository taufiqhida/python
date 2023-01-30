import streamlit as st
import pandas as pd
import numpy as np

st.title('Ketuanya milik si cantik ferina')

dv = pd.read_csv('Book1.csv')

st.write(dv)

