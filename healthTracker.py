import streamlit as st
import helper_health_tracker

st.title("Health tracker")
question = st.sidebar.text_area("Ask your question!")



if question:
    response= helper_health_tracker.generate_response(question)
    st.header('This is what you should eat today!')
    st.write(response)