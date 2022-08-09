import streamlit as st
st.set_page_config(layout="wide", page_title="BBVA Supeposición", 
                    page_icon="💥", initial_sidebar_state="expanded")
import numpy as np
from matplotlib import pyplot as plt
import time

def phi(x):
    m = np.logical_and(0<=x, x<1)
    return np.sin(2*np.pi * x) * m 

# The controls
st.title("Superposición constructiva y destructiva de ondas")
st.caption("Parámetros pueden modificarse en menu lateral izquierdo")

st.sidebar.subheader("Ondas")
st.sidebar.write("$u_1(t,x) = \phi (x - t)$")
st.sidebar.write("$u_2(t,x) = - A * \phi ( x - v (t - t_i))$")
st.sidebar.subheader("Parámetros")
A = st.sidebar.slider("Amplitud: A", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
#l = st.sidebar.slider("l", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
v = st.sidebar.slider("Velocidad: v", min_value=-2.0, max_value=2.0, value=1.0, step=0.1)
ti = st.sidebar.slider("Tiempo iniciacion: t_i", min_value=-1.0, max_value=1.0, value=0.0, step=0.1)

if False:
    # Plot x
    x = np.arange(-2, 2, 0.01)
    phi_x = phi(x)
    fig = plt.figure(figsize=(12,5))
    plt.plot(x, phi_x, 'b', label='$\phi(x)$')
    plt.ylim([-1.1, 1.1])
    plt.legend()
    plt.xlabel("x")
    plt.grid(True)
    st.pyplot(fig)

if False:
    # Plot x
    x = np.arange(-2, 2, 0.01)
    phi_x = 1.3 * phi(x+0.33)
    fig = plt.figure(figsize=(12,5))
    plt.plot(x, phi_x, 'b', label='$\phi(x)$')
    plt.ylim([-2, 2])
    plt.yticks([-1,0,1], [])
    plt.legend()
    plt.xlabel("x - vt")
    plt.grid(True)
    st.pyplot(fig)

# The selection of the plot
SEL_T = "Seleccion de t"
SHOT3 = "3 instantes"
ANIM = "Animación"
st.sidebar.subheader("Visualización")
radio_sel = st.sidebar.radio("Selección de gráfico", [SEL_T, SHOT3, ANIM])

# Range of x
x = np.arange(0, 4, 0.01)
t_max = 3.0
dt = 0.1

if radio_sel==SEL_T:
    # The data
    t = st.slider("Tiempo: t", min_value=0.0, max_value=t_max, value=0.0, step=dt)
    u1 = phi(x-t)
    u2 = -A*phi(x-v*(t-ti))
    ylims = [-3, 3]
    # The plots
    fig = plt.figure(figsize=(12,5))
    ax = fig.subplots(3, 1, sharex=True, sharey=True)

    ax[0].plot(x, u1, 'b', label='$u_1(t,x)$')
    ax[0].set_ylim(ylims)
    ax[0].legend()
    ax[0].grid(True)

    ax[1].plot(x, u2, 'g', label='$u_2(t,x)$')
    ax[1].set_ylim(ylims)
    ax[1].legend()
    ax[1].grid(True)

    ax[2].plot(x, u1+u2, 'r--', label='$u_1(t,x) + u_2(t,x)$')
    ax[2].set_ylim(ylims)
    plt.xlabel("x")
    plt.legend()
    plt.grid(True)
    plt.suptitle(f"t = {t:.1f} [seg]")
    st.pyplot(fig)

if radio_sel==SHOT3:
    # The data
    t_vec = [0.0, 1.0, 2.0]
    for t, c_i in zip(t_vec, st.columns(3)):
        u1 = phi(x-t)
        u2 = -A*phi(x-v*(t-ti))
        ylims = [-3, 3]
        # The plots
        fig = plt.figure(figsize=(5,8))
        ax = fig.subplots(3, 1, sharex=True, sharey=True)
        ax[0].plot(x, u1, 'b', label='$u_1(t,x)$')
        ax[0].set_ylim(ylims)
        ax[0].legend()
        ax[0].grid(True)
        ax[1].plot(x, u2, 'g', label='$u_2(t,x)$')
        ax[1].set_ylim(ylims)
        ax[1].legend()
        ax[1].grid(True)
        ax[2].plot(x, u1+u2, 'r--', label='$u_1(t,x) + u_2(t,x)$')
        ax[2].set_ylim(ylims)
        plt.xlabel("x")
        plt.legend()
        plt.grid(True)
        plt.suptitle(f"t = {t:.1f} [seg]")
        c_i.pyplot(fig)

if radio_sel==ANIM:
    # Animación
    t = 0
    u1 = phi(x-t)
    u2 = -A*phi(x-v*(t-ti))
    ylims = [-3, 3]
    # The plots
    fig = plt.figure(figsize=(10,5))
    ax = fig.subplots(3, 1, sharex=True, sharey=True)

    line_1, = ax[0].plot(x, u1, 'b', label='$u_1(t,x)$')
    ax[0].set_ylim(ylims)
    ax[0].legend()
    ax[0].grid(True)

    line_2, = ax[1].plot(x, u2, 'g', label='$u_2(t,x)$')
    ax[1].set_ylim(ylims)
    ax[1].legend()
    ax[1].grid(True)

    line_12, = ax[2].plot(x, u1+u2, 'r--', label='$u_1(t,x) + u_2(t,x)$')
    ax[2].set_ylim(ylims)
    plt.xlabel("x")
    plt.legend()
    plt.grid(True)
    plt.suptitle(f"t = {t:.1f} [seg]")
    plot = st.pyplot(fig)

    # Update animation
    for t in np.arange(0, t_max+dt, dt):
        u1 = phi(x-t)
        u2 = -A*phi(x-v*(t-ti))
        line_1.set_ydata(u1)
        line_2.set_ydata(u2)
        line_12.set_ydata(u1+u2)
        plt.suptitle(f"t = {t:.1f} [seg]")
        plot.pyplot(fig)
        #time.sleep(dt)