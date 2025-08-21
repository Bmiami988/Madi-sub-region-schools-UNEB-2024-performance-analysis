import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from app import df, moyo_df, adjumani_df

st.title("📈 DETAILED GRADE DISTRIBUTION ANALYSIS")

st.markdown("""
This page provides a detailed breakdown of student performance by grade category, 
showing the distribution of A, B, C, D, and E grades across districts, 
along with analysis of absenteeism patterns.
""")

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "Total Grade Distribution", 
    "Percentage Grade Distribution", 
    "Total Absenteeism", 
    "Absenteeism Rate"
])

with tab1:
    st.subheader("📊 Total Grade Distribution by District")
    
    grades = ['As', 'Bs', 'Cs', 'Ds', 'Es']
    moyo_grades = moyo_df[grades].sum()
    adjumani_grades = adjumani_df[grades].sum()
    
    x = np.arange(len(grades))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, moyo_grades.values, width, label='Moyo', color='skyblue')
    ax.bar(x + width/2, adjumani_grades.values, width, label='Adjumani', color='lightcoral')
    ax.set_title('Total Grade Distribution by District')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Number of Students')
    ax.set_xticks(x)
    ax.set_xticklabels(grades)
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    This shows the actual number of students receiving each grade. 
    Both districts have most students in the 'C' grade range, but Adjumani has significantly more 'D' and 'E' grades than Moyo, 
    indicating more students are struggling academically.
    """)

with tab2:
    st.subheader("📈 Percentage Grade Distribution by District")
    
    moyo_percent = moyo_grades / moyo_grades.sum() * 100
    adjumani_percent = adjumani_grades / adjumani_grades.sum() * 100
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, moyo_percent.values, width, label='Moyo', color='skyblue')
    ax.bar(x + width/2, adjumani_percent.values, width, label='Adjumani', color='lightcoral')
    ax.set_title('Percentage Grade Distribution by District')
    ax.set_xlabel('Grade')
    ax.set_ylabel('Percentage (%)')
    ax.set_xticks(x)
    ax.set_xticklabels(grades)
    ax.legend()
    st.pyplot(fig)
    
    st.markdown("""
    When we look at percentages, the performance gap becomes even clearer. 
    Moyo has over twice the percentage of top grades (A & B) than Adjumani. 
    Conversely, Adjumani has over three times the percentage of failing grades (E). 
    This shows a crisis in both excellence and basic competency in Adjumani.
    """)

with tab3:
    st.subheader("❌ Total Absenteeism by District")
    
    absent_by_district = df.groupby('DistrictName')['Absent'].sum()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(absent_by_district.index, absent_by_district.values, color=['skyblue', 'lightcoral'])
    ax.set_title('Total Absenteeism by District')
    ax.set_ylabel('Number of Absent Students')
    st.pyplot(fig)
    
    st.markdown("""
    In raw numbers, absenteeism is a bigger problem in Adjumani. 
    These absent students represent a complete loss of learning assessment and are likely to have fallen behind academically, 
    contributing to the performance gap.
    """)

with tab4:
    st.subheader("📉 Absenteeism Rate by District")
    
    absent_rate = df.groupby('DistrictName')['Absent'].sum() / df.groupby('DistrictName')['Total_Students'].sum() * 100
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(absent_rate.index, absent_rate.values, color=['skyblue', 'lightcoral'])
    ax.set_title('Absenteeism Rate by District')
    ax.set_ylabel('Absenteeism Rate (%)')
    st.pyplot(fig)
    
    st.markdown("""
    The absenteeism rate is significantly higher in Adjumani. 
    This is a major red flag as students cannot learn if they are not in school. 
    High absenteeism is both a cause and symptom of educational problems, 
    often linked to poverty, child labor, or lack of engagement.
    """)

# Key insights
st.subheader("💡 Key Insights")
st.info("""
1. **Grade Disparity**: Adjumani has significantly more D and E grades than Moyo
2. **Excellence Gap**: Moyo has over twice the percentage of top grades (A & B)
3. **Absenteeism Problem**: Adjumani has higher absenteeism in both raw numbers and rates
4. **Competency Crisis**: The high percentage of E grades in Adjumani indicates a basic competency crisis

""")
