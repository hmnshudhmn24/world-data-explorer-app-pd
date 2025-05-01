import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 World Data Explorer App")

# Load default world dataset
default_df = pd.read_csv("data/world_data.csv")

# File uploader
user_file = st.file_uploader("📤 Upload your own country-level data (optional, must contain 'country')", type=['csv'])

if user_file:
    user_df = pd.read_csv(user_file)
    df = pd.merge(default_df, user_df, on='country', how='outer')
    st.success("✅ User data merged successfully!")
else:
    df = default_df

st.subheader("🔎 Filter Options")
countries = st.multiselect("Select countries", df['country'].unique(), default=df['country'].unique())
indicators = st.multiselect("Select indicators to explore", df.columns.drop('country'), default=[df.columns[1]])

filtered_df = df[df['country'].isin(countries)]

for indicator in indicators:
    if indicator in df.columns:
        st.subheader(f"📊 {indicator}")
        fig = px.bar(filtered_df, x='country', y=indicator, title=f"{indicator} by Country")
        st.plotly_chart(fig)
