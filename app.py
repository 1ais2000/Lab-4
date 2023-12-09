import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from a CSV file in your folder
df = pd.read_csv('./data/iris1.csv')  # Adjust the path to your actual file location
# Title of the dashboard
st.title('Data Dashboard')
# Description of the dataset
st.write("""
The Iris dataset is a popular dataset in the field of machine learning and statistics.

The dataset consists of measurements of four features (attributes) of iris flowers, and these measurements were taken from three different species of iris:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

The three species of iris in the dataset are:
- Setosa
- Versicolor
- Virginia
""")

# Creating a scatter plot
st.subheader('Iris Dataset - Sepal Dimensions')

# Use the 'hue' parameter to color the points by species
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species', ax=ax)
st.pyplot(fig)

# Creating a pie chart for species distribution
st.subheader('Iris Species Distribution')
species_counts = df['Species'].value_counts()
fig, ax = plt.subplots()
ax.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
st.pyplot(fig)