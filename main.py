import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Moyo & Adjumani Schools UNEB 2024 Analysis",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel('moyo_adjumani_schools.xlsx', sheet_name='Sheet1')
    
    # Clean and prepare the data
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Calculate performance metrics
    df['Total_Students'] = df[['As', 'Bs', 'Cs', 'Ds', 'Es', 'Absent']].sum(axis=1)
    df['Pass_Rate'] = (df['As'] + df['Bs'] + df['Cs']) / (df['Total_Students'] - df['Absent']) * 100
    df['Excellent_Performance'] = (df['As'] + df['Bs']) / (df['Total_Students'] - df['Absent']) * 100
    df['Failure_Rate'] = (df['Ds'] + df['Es']) / (df['Total_Students'] - df['Absent']) * 100
    
    # Create district-specific dataframes
    moyo_df = df[df['DistrictName'] == 'MOYO']
    adjumani_df = df[df['DistrictName'] == 'ADJUMANI']
    
    return df, moyo_df, adjumani_df

df, moyo_df, adjumani_df = load_data()

# Main page
st.title("🏫 MADI SUB-REGION SCHOOL PERFORAMCE DASHBOARD")
st.markdown("""
This dashboard provides a comprehensive analysis of UNEB school performance in the Moyo and Adjumani districts for the year of 2024.
Use the sidebar to navigate between different analytical views.
""")

# Display key metrics
st.subheader("📊 Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Schools", len(df))
with col2:
    st.metric("Total Students", f"{df['Total_Students'].sum():,}")
with col3:
    st.metric("Average Pass Rate", f"{df['Pass_Rate'].mean():.1f}%")
with col4:
    st.metric("Average Failure Rate", f"{df['Failure_Rate'].mean():.1f}%")

# District comparison
st.subheader("🏛️ District Comparison")
col1, col2 = st.columns(2)

with col1:
    st.metric("Moyo Average Pass Rate", f"{moyo_df['Pass_Rate'].mean():.1f}%")
with col2:
    st.metric("Adjumani Average Pass Rate", f"{adjumani_df['Pass_Rate'].mean():.1f}%")

# Data preview
st.subheader("📋 Data Preview")
st.dataframe(df.head(10))

# Footer
st.markdown("---")
st.markdown("**Amani Transformational Foundation** - Madi Sub-Region 2024 UNEB Performance Analysis")