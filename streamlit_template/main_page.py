import streamlit as st
import pandas as pd

st.markdown("# Welcome to my Website!")
st.sidebar.markdown("# Main Page")

st.write("Click on a page to see racer stats")

link = '[To my Github Pages Site](https://kohlerjr.github.io/github_assignment/)'
st.markdown(link, unsafe_allow_html=True)

