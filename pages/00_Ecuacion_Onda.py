import streamlit as st
st.set_page_config(layout="wide", page_title="BBVA Ecuacion de Onda", 
                    page_icon="💥", initial_sidebar_state="expanded")

import numpy as np
from matplotlib import pyplot as plt

def phi(x):
    return np.sin(x) + 2* np.sin(x/2) - 2* np.sin(x/3)

# The controls
st.title("Ecuacion de onda")
st.caption("Parámetros pueden modificarse en menu lateral izquierdo")
st.sidebar.title("Parámetros")
v = st.sidebar.slider("velocidad: v (m/s)", min_value=-3.0, max_value=3.0, value=1.0, step=0.1)
dt = st.sidebar.slider("intervalo temporal: Δt (s)", min_value=-3.0, max_value=3.0, value=1.0, step=0.1)

# The image
x = np.arange(-10, 10, 0.01)
fig = plt.figure(figsize=(10, 5))
plt.plot(x, phi(x), 'b', label='$u(t, x) = \Phi(x - v t)$')
plt.plot(x, phi(x-v*dt), 'r--', label='$u(t + \Delta t, x) = \Phi(x - v t - v\Delta t)$')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Ecuación de onda")
plt.legend()
plt.grid(True)
st.pyplot(fig)
