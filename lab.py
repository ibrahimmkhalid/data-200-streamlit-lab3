import streamlit as st
import pandas as pd

st.write("Testing publishing with streamlit")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5],
  'second column': [10, 20, 30, 40, 50]
})

st.write(df)