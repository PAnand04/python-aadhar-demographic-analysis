import streamlit as st # type: ignore
import pandas as pd # type: ignore

# Load outputs
state_demo = pd.read_csv("state_demographic_summary.csv")
child_top = pd.read_csv("state_child_top10.csv")
adult_top = pd.read_csv("state_adult_top10.csv")

st.title("Aadhaar Demographic Intelligence Dashboard")

st.header("National Overview")
total_children = state_demo["child_population"].sum()
total_adults = state_demo["adult_population"].sum()

st.metric("Children (5–17)", f"{total_children:,}")
st.metric("Adults (18+)", f"{total_adults:,}")

st.header("State Demographic Summary")
st.dataframe(state_demo)

st.header("Top 10 Child-Dominant States")
st.dataframe(child_top.head(10))

st.header("Top 10 Adult-Dominant States")
st.dataframe(adult_top.head(10))
