import streamlit as st
import clear
import home
import register
import login

homeTab, registerTab, loginTab, clear_tab = st.tabs(["Home", "Register Student", "Student Login","Clear"])


with homeTab:
     home.home()
with registerTab:
    register.register()
with loginTab:
    login.login()
with clear_tab:
    clear.clear()