import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

def phi(x):
    return np.sin(x) + 2* np.sin(x/2) - 2* np.sin(x/3)

# The controls
st.title("Ecuacion de onda")
c1, c2 = st.columns(2)
v = c1.slider("v", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
dt = c2.slider("Δt", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

# The image
x = np.arange(-10, 10, 0.01)
fig = plt.figure(figsize=(10, 5))
plt.plot(x, phi(x), 'b', label='$u(x,t) = \Phi(x - v t)$')
plt.plot(x, phi(x-v*dt), 'r--', label='$u(x, t + \Delta t) = \Phi(x - v t - v\Delta t)$')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ecuación de onda")
plt.legend()
plt.grid(True)
st.pyplot(fig)
