import streamlit as st
import numpy as np
from matplotlib import pyplot as plt

def phi(x):
    m = np.logical_and(0<=x, x<1)
    return np.sin(2*np.pi * x) * m 

# The controls
st.title("Superposición de ondas")
c1, c2, c3, c4 = st.columns(4)
c1.write("")
c1.write("")
c1.write("$v_1(x,t) = + A_1 * \phi (x - v_1 t - t_1)$")
v1 = c2.slider("v1", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
A1 = c3.slider("A1", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
t1 = c4.slider("t1", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
c1, c2, c3, c4 = st.columns(4)
c1.write("")
c1.write("")
c1.write("$v_2(x,t) = - A_2 * \phi (x - v_2 t - t_2)$")
v2 = c2.slider("v2", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
A2 = c3.slider("A2", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
t2 = c4.slider("t2", min_value=0.0, max_value=3.0, value=1.0, step=0.1)

# The data
x = np.arange(0, 4, 0.01)
A = 1.0
v = 1.0
c1, c2, c3 = st.columns([1, 1, 1])
#ph = c2.empty()
#t = c2.slider("t", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
figsize = (5,5)


t = 0.0
u1 = A1*phi(x-v1*t-t1)
u2 = -A2*phi(x-v2*t-t2)
ylims = [-3, 3]
# The plots
fig = plt.figure(figsize=figsize)
ax = fig.subplots(3, 1, sharex=True, sharey=True)

ax[0].plot(x, u1, 'b', label='$u_1(x,t)$')
ax[0].set_ylim(ylims)
ax[0].legend()
ax[0].grid(True)

ax[1].plot(x, u2, 'g', label='$u_2(x,t)$')
ax[1].set_ylim(ylims)
ax[1].legend()
ax[1].grid(True)

ax[2].plot(x, u1+u2, 'r--', label='$u_1(x,t) + u_2(x,t)$')
ax[2].set_ylim(ylims)
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.suptitle(f"t = {t} [seg]")
c1.pyplot(fig)


t = 0.5
u1 = A1*phi(x-v1*t-t1)
u2 = -A2*phi(x-v2*t-t2)
ylims = [-3, 3]

# The plots
fig = plt.figure(figsize=figsize)

ax = fig.subplots(3, 1, sharex=True, sharey=True)

ax[0].plot(x, u1, 'b', label='$u_1(x,t)$')
ax[0].set_ylim(ylims)
ax[0].legend()
ax[0].grid(True)

ax[1].plot(x, u2, 'g', label='$u_2(x,t)$')
ax[1].set_ylim(ylims)
ax[1].legend()
ax[1].grid(True)

ax[2].plot(x, u1+u2, 'r--', label='$u_1(x,t) + u_2(x,t)$')
ax[2].set_ylim(ylims)
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.suptitle(f"t = {t} [seg]")
c2.pyplot(fig)

# 1 seg
t = 1.0
u1 = A1*phi(x-v1*t-t1)
u2 = -A2*phi(x-v2*t-t2)
ylims = [-3, 3]
# The plots
fig = plt.figure(figsize=figsize)
ax = fig.subplots(3, 1, sharex=True, sharey=True)

ax[0].plot(x, u1, 'b', label='$u_1(x,t)$')
ax[0].set_ylim(ylims)
ax[0].legend()
ax[0].grid(True)

ax[1].plot(x, u2, 'g', label='$u_2(x,t)$')
ax[1].set_ylim(ylims)
ax[1].legend()
ax[1].grid(True)

ax[2].plot(x, u1+u2, 'r--', label='$u_1(x,t) + u_2(x,t)$')
ax[2].set_ylim(ylims)
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.suptitle(f"t = {t} [seg]")
c3.pyplot(fig)
