import streamlit as st
st.set_page_config(layout="wide", page_title="BBVA", 
                    page_icon="馃挜", initial_sidebar_state="expanded")


st.title("BBVA")
st.caption("Buffer Blasting for Vibration Attenuation")

mkd = """
La presente webapp presenta de manera interactiva algunas ecuaciones utilizadas en el contexto del proyecto BBVA - Buffer Blasting for Vibration Attenuation. 


La pregunta que origina y motiva la investigaci贸n es determinar si es posible 
encontrar una secuencia 贸ptima de iniciaci贸n de pozos de tronadura que permita cumplir los siguientes objetivos:
* Maximizar la fragmentaci贸n al interior del pol铆gono de tronadura, utilizando interferencia constructiva de ondas.
* Minimizar la propagaci贸n de vibraciones hacia el exterior del pol铆gono, en particular en la cara orientada hacia el talud, utilizando interferencia destructiva de ondas.

Simulaciones: 
* [Simulador de ondas](https://bbva-enaex.streamlitapp.com/Ecuacion_Onda)
* [Superposicion Constructiva/Destructiva](https://bbva-enaex.streamlitapp.com/Superposicion)
* [Modelos PPV](https://bbva-enaex.streamlitapp.com/PPV)
"""
c1, c2 = st.columns(2)
c1.write(mkd)
c2.image("images/enaex.png", width=350)