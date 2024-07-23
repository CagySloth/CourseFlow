import streamlit as st
import datetime as date

def upcoming_lesson():
    if st.session_state.login != "Success":
        st.write("Please Login First!")
        return
    st.title("Welcome Back!")
    st.write(date.today().strftime("%B %d, %Y"))