import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app import df, moyo_df, adjumani_df

st.title("🏠 OVERALL PERFORMANCE COMPARISION BY DISTRICT")

st.markdown("""
This page provides a high-level overview of how the two districts compare across key performance metrics, 
school distribution, student population, and school sizes.
""")

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "Performance Metrics", 
    "School Distribution", 
    "Student Population", 
    "School Sizes"
])

with tab1:
    st.subheader("📈 Average Performance Metrics by District")
    
    # Performance metrics by district
    metrics = ['Pass_Rate', 'Excellent_Performance', 'Failure_Rate']
    district_metrics = df.groupby('DistrictName')[metrics].mean()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    district_metrics.plot(kind='bar', ax=ax)
    ax.set_title('Average Performance Metrics by District')
    ax.set_ylabel('Percentage (%)')
    ax.legend(['Pass Rate (A-C)', 'Excellent Performance (A-B)', 'Failure Rate (D-E)'])
    ax.tick_params(axis='x', rotation=0)
    st.pyplot(fig)
    
    st.markdown("""
    This chart shows that Moyo district significantly outperforms Adjumani in all key metrics. 
    Moyo has a higher pass rate (A-C grades), more excellent performance (A-B grades), and a much lower failure rate (D-E grades). 
    This indicates a substantial performance gap between the two districts.
    """)

with tab2:
    st.subheader("📊 School Distribution by District")
    
    district_counts = df['DistrictName'].value_counts()
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(district_counts.values, labels=district_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('School Distribution by District')
    st.pyplot(fig)
    
    st.markdown("""
    The pie chart shows that schools are almost evenly distributed between the two districts, 
    with Adjumani having slightly more schools (52%) than Moyo (48%). 
    This means the performance differences are not due to an imbalance in the number of schools.
    """)

with tab3:
    st.subheader("👥 Total Students by District")
    
    students_by_district = df.groupby('DistrictName')['Total_Students'].sum()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(students_by_district.index, students_by_district.values, color=['skyblue', 'lightcoral'])
    ax.set_title('Total Students by District')
    ax.set_ylabel('Number of Students')
    st.pyplot(fig)
    
    st.markdown("""
    Adjumani serves a larger student population than Moyo, despite having a similar number of schools. 
    This means schools in Adjumani tend to be larger on average, which might impact resource allocation and teacher-student ratios.
    """)

with tab4:
    st.subheader("🏫 Average School Size by District")
    
    avg_size = df.groupby('DistrictName')['Total_Students'].mean()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(avg_size.index, avg_size.values, color=['skyblue', 'lightcoral'])
    ax.set_title('Average School Size by District')
    ax.set_ylabel('Average Students per School')
    st.pyplot(fig)
    
    st.markdown("""
    This confirms that schools in Adjumani are larger on average than those in Moyo. 
    Larger schools may face challenges like overcrowded classrooms and stretched resources, 
    which could contribute to performance issues.
    """)

# Key insights
st.subheader("💡 Key Insights")
st.info("""
1. **Performance Gap**: Moyo significantly outperforms Adjumani across all metrics
2. **School Distribution**: Schools are evenly distributed, ruling out quantity as a factor
3. **Student Population**: Adjumani serves more students with similar school count
4. **School Size**: Adjumani schools are larger on average, potentially straining resources

""")
