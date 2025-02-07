import altair as alt
import pandas as pd
import streamlit as st

# st.markdown("# Dyslexia genes ")
# st.sidebar.markdown("# Dyslexia genes ")

# Show the page title and description.
st.set_page_config(page_title="Dyslexia proteins", page_icon="🎬")
st.title("Dyslexia genes/proteins")
st.sidebar.success("Dyslexia genes/proteins")
#st.title("Dyslexia proteins")
st.write(
    """
    This website contains information about dyslexia
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
st.write("9 genes/proteins associated with the disease Dyslexia from the curated CTD Gene-Disease Associations dataset.")
# [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/proteins_data.csv")
    return df


#df = load_data()

# Show a multiselect widget with the genres using `st.multiselect`.
# genres = st.multiselect(
#     "Genres",
#     df.genre.unique(),
#     ["Action", "Adventure", "Biography", "Comedy", "Drama", "Horror"],
# )

# Show a slider widget with the years using `st.slider`.
# years = st.slider("Years", 1986, 2006, (2000, 2016))

# # Filter the dataframe based on the widget input and reshape it.
# df_filtered = df[(df["genre"].isin(genres)) & (df["year"].between(years[0], years[1]))]
# df_reshaped = df_filtered.pivot_table(
#     index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0
# )
# df_reshaped = df_reshaped.sort_values(by="year", ascending=False)


# # Display the data as a table using `st.dataframe`.
# st.dataframe(
#     df_reshaped,
#     use_container_width=True,
#     column_config={"year": st.column_config.TextColumn("Year")},
# )

# # Display the data as an Altair chart using `st.altair_chart`.
# df_chart = pd.melt(
#     df_reshaped.reset_index(), id_vars="year", var_name="genre", value_name="gross"
# )
# chart = (
#     alt.Chart(df_chart)
#     .mark_line()
#     .encode(
#         x=alt.X("year:N", title="Year"),
#         y=alt.Y("gross:Q", title="Gross earnings ($)"),
#         color="genre:N",
#     )
#     .properties(height=320)
# )
# st.altair_chart(chart, use_container_width=True)
