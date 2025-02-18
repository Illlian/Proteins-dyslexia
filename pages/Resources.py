import streamlit as st
import random
import pandas as pd
import random


st.set_page_config(page_title="Resources", page_icon="📖")
st.title("Resources")
st.sidebar.success("Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Datasets")
    st.page_link("https://www.uniprot.org/uniprotkb?query=%28cc_disease%3ADI-01511%29&facets=existence%3A1%2Cproteins_with%3A1", 
                 label="Proteins", icon="📗")
    
with col2:
    st.header("Materials")
    st.page_link(
        "https://maayanlab.cloud/Harmonizome/gene_set/Dyslexia/CTD+Gene-Disease+Associations",
        label="Dyslexia", icon="📘")
    
with col3:
    st.header("Discussions")
    st.page_link("https://www.nature.com/articles/s41380-024-02649-8",
                 label="Genetic neurodevelopmental clustering and dyslexia", icon="📙")
    st.page_link("https://academic.oup.com/cercor/article/34/4/bhae144/7644534", 
                 label="Developmental dyslexia susceptibility genes", icon="📙")
    
