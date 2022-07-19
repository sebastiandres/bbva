import streamlit as st
st.set_page_config(layout="wide", page_title="BBVA PPV", 
                    page_icon="💥", initial_sidebar_state="expanded")

import numpy as np
from matplotlib import pyplot as plt

def phi(x):
    return np.sin(x) + 2* np.sin(x/2) - 2* np.sin(x/3)

# The controls
st.title("Modelos PPV")
st.caption("Parámetros pueden modificarse en menu lateral izquierdo")

DEVINE = "Devine"
HYP = "Holmberg y Persson"
st.sidebar.subheader("Modelo PPV")
radio_sel = st.sidebar.radio("Seleccionar modelo", [DEVINE, HYP])

if radio_sel==DEVINE:
     c1, c2, _ = st.columns([1,1,2])
     c1.subheader(f"Ecuación {DEVINE}")
     c2.latex(r"PPV = H \left( \frac{D}{W^{0.6}} \right)^{-\beta}")
     st.sidebar.subheader("Variables físicas")
     D = st.sidebar.slider("D", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
     W = st.sidebar.slider("W", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
     st.sidebar.subheader("Coeficientes experimentales:")
     H = st.sidebar.slider("H", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
     alpha = st.sidebar.slider("$\\beta$", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
     D_vector = np.linspace(0, 3, 100)
     PPV = H * (D_vector/W**0.6)**(-alpha)
     fig = plt.figure(figsize=(12,5))
     plt.plot(D_vector, PPV, 'b', label='$PPV$')
     plt.ylim([0,30])
     plt.xlabel("Distance: D (m)")
     plt.ylabel("Peak Particle Velocity: PPV (m/s)")
     st.pyplot(fig)
elif radio_sel==HYP:
     c1, c2, _ = st.columns([2,2,1])
     c1.subheader(f"Ecuación {HYP}")
     c2.latex(r"PPV = K \left( \frac{q}{R_9} \right)^{\alpha} \left( \tan^{-1}(z/R_0) - \tan^{-1}((z - h)/R_0)\right)")
     st.sidebar.subheader("Variables físicas")
     H = st.sidebar.slider("R", min_value=-3.0, max_value=3.0, value=1.0, step=0.1)
     H = st.sidebar.slider("h", min_value=-3.0, max_value=3.0, value=1.0, step=0.1)
     H = st.sidebar.slider("q", min_value=-3.0, max_value=3.0, value=1.0, step=0.1)
     st.sidebar.subheader("Coeficientes experimentales:")
     K = st.sidebar.slider("K", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
     alpha = st.sidebar.slider("$\\alpha$", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
else:
     st.write("No seleccionó ningún modelo")   
      