import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from main import df, moyo_df, adjumani_df

st.title("📊 PERFORMANCE DISTRIBUTION ANALYSIS")

st.markdown("""
This page explores how performance is distributed across schools in each district, 
examining patterns in pass rates, failure rates, and the relationship between school size and performance.
""")

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "Pass Rate Distribution", 
    "Failure Rate Distribution", 
    "School Size vs Performance", 
    "Top Performing Schools"
])

with tab1:
    st.subheader("📈 Pass Rate Distribution by District")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist([moyo_df['Pass_Rate'], adjumani_df['Pass_Rate']], 
             bins=10, alpha=0.7, label=['Moyo', 'Adjumani'], color=['skyblue', 'lightcoral'])
    ax.set_title('Pass Rate Distribution by District')
    ax.set_xlabel('Pass Rate (%)')
    ax.set_ylabel('Number of Schools')
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    This histogram shows how schools are distributed across different pass rate ranges. 
    Most Moyo schools cluster at higher pass rates (60-100%), while Adjumani schools are spread across lower ranges, 
    with several schools having very low pass rates (below 40%).
    """)

with tab2:
    st.subheader("📉 Failure Rate Distribution by District")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist([moyo_df['Failure_Rate'], adjumani_df['Failure_Rate']], 
             bins=10, alpha=0.7, label=['Moyo', 'Adjumani'], color=['skyblue', 'lightcoral'])
    ax.set_title('Failure Rate Distribution by District')
    ax.set_xlabel('Failure Rate (%)')
    ax.set_ylabel('Number of Schools')
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    The failure rate distribution shows the opposite pattern. 
    Most Moyo schools have low failure rates (below 20%), while many Adjumani schools have high failure rates (20-60%). 
    This indicates widespread academic challenges in Adjumani schools.
    """)

with tab3:
    st.subheader("🏫 School Size vs Performance")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(moyo_df['Total_Students'], moyo_df['Pass_Rate'], alpha=0.7, label='Moyo', color='skyblue')
    ax.scatter(adjumani_df['Total_Students'], adjumani_df['Pass_Rate'], alpha=0.7, label='Adjumani', color='lightcoral')
    ax.set_title('School Size vs Pass Rate')
    ax.set_xlabel('Total Students')
    ax.set_ylabel('Pass Rate (%)')
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    This scatter plot shows no clear relationship between school size and performance. 
    Both large and small schools can be found among top and bottom performers. 
    This suggests that factors other than size (like teaching quality, resources, or leadership) are more important for success.
    """)

with tab4:
    st.subheader("🏆 Top 10 Performing Schools")
    
    top_schools = df.nlargest(10, 'Pass_Rate')[['CentreName', 'DistrictName', 'Pass_Rate']]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = ['skyblue' if x == 'MOYO' else 'lightcoral' for x in top_schools['DistrictName']]
    bars = ax.barh(range(len(top_schools)), top_schools['Pass_Rate'], color=colors)
    ax.set_yticks(range(len(top_schools)))
    ax.set_yticklabels([f"{row.CentreName} ({row.DistrictName})" for _, row in top_schools.iterrows()])
    ax.set_title('Top 10 Performing Schools by Pass Rate')
    ax.set_xlabel('Pass Rate (%)')
    
    # Add district color legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor='skyblue', label='Moyo'),
                       Patch(facecolor='lightcoral', label='Adjumani')]
    ax.legend(handles=legend_elements, loc='lower right')
    
    st.pyplot(fig)
    
    st.markdown("""
    Moyo dominates the top performers, taking 7 of the top 10 spots. 
    The top three schools are all in Moyo. These high-performing schools should be studied as models of excellence, 
    and their successful practices should be shared with lower-performing schools.
    """)

# Key insights
st.subheader("💡 Key Insights")
st.info("""
1. **Performance Distribution**: Moyo schools cluster at high performance levels, while Adjumani schools show wide variation
2. **Failure Patterns**: Adjumani has concerning clusters of schools with high failure rates
3. **Size Not Deterministic**: School size doesn't correlate strongly with performance
4. **Excellence Models**: Top-performing schools are predominantly in Moyo and should be studied for best practices
""")