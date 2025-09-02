import streamlit as st
import pandas as pd
import numpy as np

# Title and text
st.title("📊 Simple Streamlit App")
st.write("This is a basic demo of Streamlit!")

# User input
name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello, {name}! 👋")

# Slider
num_points = st.slider("Number of data points", 10, 100, 50)

# Random data
data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=['x', 'y']
)

# Show dataframe
st.dataframe(data)

# Line chart
st.line_chart(data)

# Checkbox
if st.checkbox("Show raw data"):
    st.write(data)
