import streamlit as st
import random
import pandas as pd
import random


st.title("Resources 📖")
st.sidebar.success("Resources")
st.write(
    """
    This page contains some extra resoueces with information about dyslexia, 
    as well as all the data and references used when creating this project.
    
    """
)

st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Extra info")
    st.page_link("https://www.malacards.org/card/dyslexia?__cf_chl_tk=YTQCPxyEEIdzMZ3s.Z8kXDyj8RyZsM8eoNNlnK_pJvc-1732254251-1.0.1.1-.YtQwI1UbRUWaoXdcdeagg2SfzXU5eyBw.pTeCXkPX0#Overview", 
                 label="Dyslexia (General)", icon="📗")
    st.page_link("https://childmind.org/article/understanding-dyslexia/", 
                 label="Signs of dyslexia", icon="📗")
    st.page_link("https://www.cambridgeenglish.org/blog/ten-ways-to-support-learners-with-dyslexia/", 
                 label="Support", icon="📗")
    st.page_link("https://www.gemmlearning.com/blog/dyslexia/dyslexia-hacks/", 
                 label="Strategies", icon="📗")
    
with col2:
    st.header("Materials")
    st.page_link(
        "https://maayanlab.cloud/Harmonizome/gene_set/Dyslexia/CTD+Gene-Disease+Associations",
        label="Dyslexia dataset", icon="📘")
    st.page_link("https://www.uniprot.org/uniprotkb?query=%28cc_disease%3ADI-01511%29&facets=existence%3A1%2Cproteins_with%3A1", 
                 label="Proteins", icon="📘")
    st.page_link("https://www.genecards.org/cgi-bin/carddisp.pl?gene=KIAA0319&keywords=KIAA0319#proteins", 
                 label="KIAA0319", icon="📘")
    st.page_link("https://moldstud.com/articles/p-python-in-bioinformatics-analyzing-dna-and-protein-sequences", 
                 label="Bioinformatics", icon="📘")
    
with col3:
    st.header("Discussions")
    st.page_link("https://www.nature.com/articles/s41380-024-02649-8",
                 label="Genetic neurodevelopmental clustering and dyslexia", icon="📙")
    st.page_link("https://academic.oup.com/cercor/article/34/4/bhae144/7644534", 
                 label="Developmental dyslexia susceptibility genes", icon="📙")
    
