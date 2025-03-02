import altair as alt
import pandas as pd
import streamlit as st

pg = st.navigation(
    [
st.Page("pages/Dyslexia.py"),
        st.Page("pages/Proteins.py"),
     st.Page("pages/Resources.py")])
pg.run()

