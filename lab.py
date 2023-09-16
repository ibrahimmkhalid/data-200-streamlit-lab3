import streamlit as st
import pandas as pd

st.write("Testing publishing with streamlit")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 5, 6],
  'second column': [10, 20, 30, 40, 50, 60]
})

st.write(df)
st.write("making changes to the script")