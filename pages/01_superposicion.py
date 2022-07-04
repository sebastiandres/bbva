import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

def phi(x):
    m = np.logical_and(0<=x, x<1)
    return np.sin(2*np.pi * x) * m 

# The controls
st.title("Superposición de ondas")
st.write("$v_1(x,t) = + A_1 * \phi (x - v_1 t - t_1)$")
c1, c2, c3 = st.columns(3)
v1 = c1.slider("v1", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
A1 = c2.slider("A1", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
t1 = c3.slider("t1", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
st.write("$v_2(x,t) = - A_2 * \phi (x - v_2 t - t_2)$")
c1, c2, c3 = st.columns(3)
v2 = c1.slider("v2", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
A2 = c2.slider("A2", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
t2 = c3.slider("t2", min_value=0.0, max_value=3.0, value=1.0, step=0.1)

# The image
x = np.arange(0, 4, 0.01)
fig = plt.figure(figsize=(10, 5))
ax = fig.subplots(3, 1, sharex=True, sharey=True)
A = 1.0
v = 1.0
t = 1.0
c1, c2 = st.columns([1, 3])
t = c1.slider("t", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
u1 = A1*phi(x-v1*t-t1)
u2 = -A2*phi(x-v2*t-t2)
ax[0].plot(x, u1, 'b', label='$u_1(x,t)$')
plt.ylim([-2.5, 2.5])
plt.legend()
ax[0].grid(True)

ax[1].plot(x, u2, 'g', label='$u_2(x,t)$')
ax[1].grid(True)
plt.ylim([-2.5, 2.5])
plt.legend()
plt.grid(True)

ax[2].plot(x, u1+u2, 'r--', label='$u_1(x,t) + u_2(x,t)$')
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([-2.5, 2.5])
plt.legend()
plt.grid(True)
plt.suptitle("Ecuación de onda")
c2.pyplot(fig)