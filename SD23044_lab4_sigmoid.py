import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Sigmoid Activation Function")

# Define sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate input values
x = np.linspace(-10, 10, 100)
y = sigmoid(x)

# Plot the sigmoid function
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel("Input")
ax.set_ylabel("Output")
ax.set_title("Sigmoid Function")

# Display plot in Streamlit
st.pyplot(fig)
