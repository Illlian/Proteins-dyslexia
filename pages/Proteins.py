import streamlit as st
import pandas as pd
import json

from stmol import showmol
import py3Dmol


st.title("Proteins")
st.sidebar.success("Proteins")

st.write(
    """
    Here is some extra information about specific proteins and genes assosiated with the development of dyslexia.
    """
)

# Info about K0319_HUMAN protein
st.divider()
st.header('K0319_HUMAN')
st.subheader('Protein Dyslexia-associated protein KIAA0319')
st.subheader('Gene KIAA0319')
st.link_button("Q5VV43", "https://www.uniprot.org/uniprotkb/Q5VV43/entry")

st.markdown("""
Involved in neuronal migration during development of the cerebral neocortex.
May function in a cell autonomous and a non-cell autonomous manner and play a role in appropriate adhesion between migrating neurons and radial glial fibers.
May also regulate growth and differentiation of dendrites.
""")

ko319 = pd.read_json("pages/ko319_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q5VV43/variant-viewer")
# uniprotkb_cc_disease_DI_01511_AND_model_2025_02_09.json
st.dataframe(ko319)


# 3d model
on = st.toggle("View K0319_HUMAN")
if on:
    st.write("Dyslexia-associated protein KIAA0319x")
    st.link_button("pdbe", "https://www.ebi.ac.uk/pdbe/pdbe-kb/proteins/Q5VV43")
    # Structure of protein by pdb
    with st.container(border=True):
        xyzview = py3Dmol.view(query='pdb:2e7m')
        xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
        showmol(xyzview, height=500, width=800)
 
 
 
 # DCDC2_HUMAN       
st.divider()
st.header('DCDC2_HUMAN')
st.subheader('Doublecortin domain-containing protein 2')
st.subheader('Gene DCDC2')
st.link_button("Q9UHG0", "https://www.uniprot.org/uniprotkb/Q9UHG0/entry")

st.markdown("""
Protein that plays a role in the inhibition of canonical Wnt signaling pathway (PubMed:25557784).
May be involved in neuronal migration during development of the cerebral neocortex (By similarity).
Involved in the control of ciliogenesis and ciliary length (PubMed:25601850, PubMed:27319779).
""")

dcdc2 = pd.read_json("pages/dcdc2_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q9UHG0/variant-viewer")
st.dataframe(dcdc2, use_container_width=True)

on = st.toggle("View DCDC2_HUMAN")
if on:
    st.write("Doublecortin domain-containing protein 2")
    st.link_button("pdbe", "https://www.ebi.ac.uk/pdbe/pdbe-kb/proteins/Q9UHG0")
    with st.container(border=True):
        xyzview = py3Dmol.view(query='pdb:2dnf')
        xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
        showmol(xyzview, height=500, width=800)




#DAAF4_HUMAN
st.divider()
st.header('DAAF4_HUMAN')
st.subheader('Dynein axonemal assembly factor 4')
st.subheader('Gene DNAAF4')
st.link_button("Q8WXU2", "https://www.uniprot.org/uniprotkb/Q8WXU2/entry")

st.markdown("""
Axonemal dynein assembly factor required for ciliary motility. Involved in neuronal migration during development of the cerebral neocortex. May regulate the stability and proteasomal degradation of the estrogen receptors that play an important role in neuronal differentiation, survival and plasticity.
""")

daaf4 = pd.read_json("pages/daaf4_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q8WXU2/variant-viewer")
st.dataframe(daaf4, use_container_width=True)




# NRSN1_HUMAN
st.divider()
st.header('NRSN1_HUMAN')
st.subheader('Neurensin-1')
st.subheader('Gene NRSN1')
st.link_button("Q8IZ57", "https://www.uniprot.org/uniprotkb/Q8IZ57/entry")

st.markdown("""
May play an important role in neural organelle transport, and in transduction of nerve signals or in nerve growth. May play a role in neurite extension. May play a role in memory consolidation (By similarity).
""")

nrsn1 = pd.read_json("pages/nrsn1_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q8IZ57/variant-viewer")
st.dataframe(nrsn1, use_container_width=True)



#ROBO1_HUMAN
st.divider()
st.header('ROBO1_HUMAN')
st.subheader('Roundabout homolog 1')
st.subheader('Gene ROBO1')
st.link_button("Q9Y6N7", "https://www.uniprot.org/uniprotkb/Q9Y6N7/entry")

st.markdown("""
Receptor for SLIT1 and SLIT2 that mediates cellular responses to molecular guidance cues in cellular migration, including axonal navigation at the ventral midline of the neural tube and projection of axons to different regions during neuronal development (PubMed:10102268, PubMed:24560577).
Interaction with the intracellular domain of FLRT3 mediates axon attraction towards cells expressing NTN1 (PubMed:24560577).
In axon growth cones, the silencing of the attractive effect of NTN1 by SLIT2 may require the formation of a ROBO1-DCC complex (By similarity).
Plays a role in the regulation of cell migration via its interaction with MYO9B; inhibits MYO9B-mediated stimulation of RHOA GTPase activity, and thereby leads to increased levels of active, GTP-bound RHOA (PubMed:26529257).
May be required for lung development (By similarity).
""")

# 3d model
robo1 = pd.read_json("pages/robo1_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q9Y6N7/variant-viewer")
st.dataframe(robo1, use_container_width=True)

on = st.toggle("View ROBO1_HUMAN")
if on:
    st.write("Roundabout homolog 1")
    st.link_button("pdbe", "https://www.ebi.ac.uk/pdbe/pdbe-kb/proteins/Q9Y6N7")
    with st.container(border=True):
        xyzview = py3Dmol.view(query='pdb:2v9q')
        xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
        showmol(xyzview, height=500, width=800)
        


#FOXP2_HUMAN         
st.divider()
st.header('FOXP2_HUMAN')
st.subheader('Forkhead box protein P2')
st.subheader('Gene FOXP2')
st.link_button("O15409", "https://www.uniprot.org/uniprotkb/O15409/entry")

st.markdown("""
Transcriptional repressor that may play a role in the specification and differentiation of lung epithelium. May also play a role in developing neural, gastrointestinal and cardiovascular tissues. Can act with CTBP1 to synergistically repress transcription but CTPBP1 is not essential. Plays a role in synapse formation by regulating SRPX2 levels. Involved in neural mechanisms mediating the development of speech and language.
""")

foxp2 = pd.read_json("pages/foxp2_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/O15409/variant-viewer")
st.dataframe(foxp2, use_container_width=True)


# 3d model
on = st.toggle("View FOXP2_HUMAN")
if on:
    st.write("Forkhead box protein P2")
    st.link_button("pdbe", "https://www.ebi.ac.uk/pdbe/pdbe-kb/proteins/O15409")
    with st.container(border=True):
        xyzview = py3Dmol.view(query='pdb:2a07')
        xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
        showmol(xyzview, height=500, width=800)
        

#CNTP2_HUMAN        
st.divider()
st.header('CNTP2_HUMAN')
st.subheader('Contactin-associated protein-like 2')
st.subheader('Gene CNTNAP2')
st.link_button("Q9UHC6", "https://www.uniprot.org/uniprotkb/Q9UHC6/entry")

st.markdown("""
Required for gap junction formation (Probable). Required, with CNTNAP1, for radial and longitudinal organization of myelinated axons. Plays a role in the formation of functional distinct domains critical for saltatory conduction of nerve impulses in myelinated nerve fibers. Demarcates the juxtaparanodal region of the axo-glial junction.
""")

cntp2 = pd.read_json("pages/cntp2_variants.json")
st.subheader('Variants')
st.link_button("variant-viewer", "https://www.uniprot.org/uniprotkb/Q9UHC6/variant-viewer")
st.dataframe(cntp2, use_container_width=True)

# 3d model
on = st.toggle("View CNTP2_HUMAN")
if on:
    st.write("Contactin-associated protein-like 2")
    st.link_button("pdbe", "https://www.ebi.ac.uk/pdbe/pdbe-kb/proteins/Q9UHC6")
    with st.container(border=True):
        xyzview = py3Dmol.view(query='pdb:5y4m')
        xyzview.setStyle({'cartoon': {'color': 'spectrum'}})
        showmol(xyzview, height=500, width=800)