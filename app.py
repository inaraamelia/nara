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

import streamlit as st
import matplotlib.pyplot as plt

# Title
st.title("🍕 Pie Chart Example in Streamlit")

# Sample data (you can replace with your own)
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [25, 30, 20, 25]

# User can adjust values
st.subheader("Adjust Fruit Proportions")
sizes[0] = st.slider("Apples", 0, 100, sizes[0])
sizes[1] = st.slider("Bananas", 0, 100, sizes[1])
sizes[2] = st.slider("Cherries", 0, 100, sizes[2])
sizes[3] = st.slider("Dates", 0, 100, sizes[3])

# Normalize sizes so they sum to 100
total = sum(sizes)
sizes = [s / total * 100 for s in sizes]

# Create pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis("equal")  # Equal aspect ratio ensures pie is a circle

# Show in Streamlit
st.pyplot(fig)
