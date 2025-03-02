import altair as alt
import pandas as pd
import streamlit as st


# Show the page title and description.
st.title(" All you need to know about dyslexia")
st.sidebar.success("Dyslexia genes/proteins")

st.write(
    """
    This website contains information about dyslexia.
    
    What is dyslexia? A learning disability that affects reading/writing. 
    People with dyslexia have higher rates of attention deficit hyperactivity disorder (ADHD), 
    developmental language disorders, and difficulties with numbers.
    """
)


# deseases
st.divider()
st.header('Involvement in diseases. ')
st.markdown('Disease susceptibility may be associated with variants affecting the gene represented in this entry')
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    agree_1 = st.checkbox("DYX1")
with col2:
    agree_2 = st.checkbox("DYX2")
with col3:
    agree_3 = st.checkbox("DYX3")
with col4:
    agree_4 = st.checkbox("DYX5")
with col5:
    agree_5 = st.checkbox("DYX6")
with col6:
    agree_6 = st.checkbox("DYX8")
with col7:
    agree_7 = st.checkbox("DYX9")
    
if agree_1:
    st.divider()
    st.subheader('Dyslexia 1 (DYX1)')
    st.subheader("Alternative names: Congenital word - blindness")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Dyslexia 1 uniprot", "https://www.uniprot.org/diseases/DI-02608")
    with col2:
        st.link_button("Dyslexia 1 malacards", "https://www.malacards.org/card/dyslexia_1#Overview")  
        
if agree_2:
    st.divider()
    st.subheader('Dyslexia 2 (DYX2). ')
    st.subheader("Alternative names: Specific reading disability type 2")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Dyslexia 2 uniprot", "https://www.uniprot.org/diseases/DI-01511")
    with col2:
        st.link_button("Dyslexia 1 malacards", "https://www.malacards.org/card/dyslexia_1#Overview")
                
if agree_3:
    st.divider()
    st.subheader('Dyslexia 3 (DYX3). ')
    st.subheader("Also known as: Dyslexia, Susceptibility To, 3 ")

    st.link_button("Dyslexia 3 malacards", "https://www.malacards.org/card/dyslexia_3")
    
if agree_4:
    st.divider()
    st.subheader('Dyslexia 5 (DYX5). ')
    st.subheader("Also known as: Dyslexia, Susceptibility To, 5 ")

    st.link_button("Dyslexia 5 malacards", "https://www.malacards.org/card/dyslexia_5")    
    
if agree_5:
    st.divider()
    st.subheader('Dyslexia 6 (DYX6). ')
    st.subheader("Also known as: Dyslexia, Susceptibility To, 6 ")

    st.link_button("Dyslexia 6 malacards", "https://www.malacards.org/card/dyslexia_6")
    
if agree_6:
    st.divider()
    st.subheader('Dyslexia 8 (DYX8). ')
    st.subheader("Also known as: Dyslexia, Susceptibility To, 8 ")

    st.link_button("Dyslexia 8 malacards", "https://www.malacards.org/card/dyslexia_8")
 
if agree_7:
    st.divider()
    st.subheader('Dyslexia 9 (DYX9). ')
    st.subheader("Also known as: Dyslexia, Susceptibility To, 9 ")

    st.link_button("Dyslexia 9 malacards", "https://www.malacards.org/card/dyslexia_9")
          
st.divider()            
st.write(
    """
    Causes: Exact causes are not clear, but the disorder is likely hereditary. 
    There are currently 88 genes linked to possibly causing dyslexia. 
    
    The main 9 and their characteristics are displayed below.
    
    """
)



df = pd.DataFrame(
    {
        "symbol": ["DYX5", "KIAA0319", "DCDC2", "DYX9", "DYX8", "DYX1C1","DYX1", "DYX3", "DYX6"],
        "url": [
            "https://maayanlab.cloud/Harmonizome/gene/DYX5",
            "https://maayanlab.cloud/Harmonizome/gene/KIAA0319",
            "https://maayanlab.cloud/Harmonizome/gene/DCDC2",
            "https://maayanlab.cloud/Harmonizome/gene/DYX9",
            "https://maayanlab.cloud/Harmonizome/gene/DYX8",
            "https://maayanlab.cloud/Harmonizome/gene/DYX1C1",
            "https://maayanlab.cloud/Harmonizome/gene/DYX1",
            "https://maayanlab.cloud/Harmonizome/gene/DYX3",
            "https://maayanlab.cloud/Harmonizome/gene/DYX6"
        ],
        "name": ["dyslexia susceptibility 5",
                 "KIAA0319",
                 "doublecortin domain containing 2",
                 "dyslexia susceptibility 9",
                 "dyslexia susceptibility 8",
                 "dyslexia susceptibility 1 candidate 1",
                 "dyslexia susceptibility 1",
                 "dyslexia susceptibility 3",
                 "dyslexia susceptibility 6"
                 ],
    }
)


st.dataframe(df)
st.write("""
         9 genes and proteins associated with the disease Dyslexia from the curated CTD Gene-Disease Associations dataset.
         
         Treatment: It is a lifelong condition with no specific treatment. 
         Though taking specialized classes and getting extra support will help a 
         person with dyslexia to lead a mostly “normal” life.
         """)

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/proteins_data.csv")
    return df


# genes table
st.divider() 
st.header("Genes associated with Dyslexia by malacards scores")
df = pd.DataFrame(
    {
        "disease": ["DYX2", "DYX2", "DYX2", "DYX1", "DYX1", "DYX3","DYX5", "DYX6", "DYX8", "DYX9"],
        "symbol": ["DCDC2", "KAAG1", "KIAA0319", "DNAAF4", "DNAAF4-CCPG1", "DYX3","DYX5", "DYX6", "DYX8", "DYX9"],
        "description": [
            "Doublecortin Domain Containing 2",
            "Kidney Associated DCDC2 Antisense RNA 1",
            "KIAA0319",
            "Dynein Axonemal Assembly Factor 4",
            "DNAAF4-CCPG1 Readthrough (NMD Candidate)",
            "Dyslexia Susceptibility 3",
            "Dyslexia Susceptibility 5",
            "Dyslexia Susceptibility 6",
            "Dyslexia Susceptibility 8",
            "Dyslexia Susceptibility 9",
        ],
        "category": [
                 "Protein Coding",
                 "RNA Gene",
                 "Protein Coding",
                 "Protein Coding",
                 "RNA Gene",
                 "Genetic Locus",
                 "Genetic Locus",
                 "Genetic Locus",
                 "Genetic Locus",
                 "Genetic Locus",
                 ],
        "score": [
                 407.43,
                 400,
                 182.43,
                 1107.42,
                 425,
                 57.48,
                 50,
                 50,
                 50,
                 50,
                 ],
        "variation": [
                 "Pathogenic",
                 "Pathogenic",
                 "Susceptibility factor",
                 "Pathogenic. Susceptibility factor. Likely pathogenic",
                 "Pathogenic. Likely pathogenic",
                 "Susceptibility factor",
                 "Susceptibility factor",
                 "Susceptibility factor",
                 "Susceptibility factor",
                 "Susceptibility factor",
                 ],
    }
)
st.dataframe(
    df,
    hide_index=True,
)

# MalaCard score bar
st.sidebar.header("Genes associated with Dyslexia by MalaCard score")
st.divider()
st.subheader(
    """Genes associated with Dyslexia Plot"""
)


plot_df=df[['disease', 'symbol', 'score']]
chart_data = pd.DataFrame(plot_df)
st.bar_chart(chart_data, x='symbol', y='score', color='disease')



# Genes/chromosome scatter plot
st.header("Genes associated with Dyslexia Genomic Location")
chart_data = pd.DataFrame(
    {
        "symbol": ["DYX8", "DYX3", "ROBO1", "DYX5", "DCDC2", "KAAG1", "KIAA0319", "FOXP2", "CNTNAP2", "DNAAF4", "DNAAF4-CCPG1", "CMIP", "ATP2C2", "DYX6"],
        "chromosome": [
            1,
            2,
            3,
            5,
            6,
            6,
            6,
            7,
            7,
            15,
            15,
            16,
            16,
            18,
        ],
    },
)
st.scatter_chart(chart_data, x='chromosome', color="symbol")