import streamlit as st
from main import df, moyo_df, adjumani_df

st.title("💡 COMPREHENSIVE INSIGHTS")

st.markdown("""
This page provides a comprehensive summary of key findings from the analysis 
and offers actionable recommendations for improving educational outcomes in the Madi sub-region.
""")

# Key statistics
st.header("📊 Key Statistics")

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
st.header("🏛️ District Comparison")

col1, col2 = st.columns(2)

with col1:
    st.metric("Moyo Average Pass Rate", f"{moyo_df['Pass_Rate'].mean():.1f}%")
    st.metric("Moyo Average Failure Rate", f"{moyo_df['Failure_Rate'].mean():.1f}%")
    
with col2:
    st.metric("Adjumani Average Pass Rate", f"{adjumani_df['Pass_Rate'].mean():.1f}%")
    st.metric("Adjumani Average Failure Rate", f"{adjumani_df['Failure_Rate'].mean():.1f}%")

st.metric("Performance Gap", 
          f"{moyo_df['Pass_Rate'].mean() - adjumani_df['Pass_Rate'].mean():.1f}%",
          delta_color="inverse")

# Top and bottom performers
st.header("🏆 Top and Bottom Performing Schools")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 5 Schools")
    top_5 = df.nlargest(5, 'Pass_Rate')[['CentreName', 'DistrictName', 'Pass_Rate', 'Total_Students']]
    for i, row in top_5.iterrows():
        st.write(f"**{row['CentreName']}** ({row['DistrictName']}): {row['Pass_Rate']:.1f}% Pass Rate")

with col2:
    st.subheader("Bottom 5 Schools")
    bottom_5 = df.nsmallest(5, 'Pass_Rate')[['CentreName', 'DistrictName', 'Pass_Rate', 'Total_Students']]
    for i, row in bottom_5.iterrows():
        st.write(f"**{row['CentreName']}** ({row['DistrictName']}): {row['Pass_Rate']:.1f}% Pass Rate")

# Absenteeism analysis
st.header("❌ Absenteeism Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Absent Students", df['Absent'].sum())
with col2:
    st.metric("Overall Absenteeism Rate", f"{df['Absent'].sum()/df['Total_Students'].sum()*100:.1f}%")
with col3:
    st.metric("Adjumani vs Moyo Absenteeism", 
              f"{adjumani_df['Absent'].sum()/adjumani_df['Total_Students'].sum()*100:.1f}% vs {moyo_df['Absent'].sum()/moyo_df['Total_Students'].sum()*100:.1f}%")

# Grade distribution insights
st.header("📝 Grade Distribution Insights")

grades = ['As', 'Bs', 'Cs', 'Ds', 'Es']
total_grades = df[grades].sum().sum()

col1, col2, col3, col4, col5 = st.columns(5)

for i, grade in enumerate(grades):
    count = df[grade].sum()
    with [col1, col2, col3, col4, col5][i]:
        st.metric(f"{grade} Grades", f"{count/total_grades*100:.1f}%")

# Key findings
st.header("🔍 Key Findings")

st.error("""
1. **Significant Performance Gap**: Moyo district outperforms Adjumani across all metrics
2. **Widespread Challenges in Adjumani**: Majority of schools in Adjumani are in Fair or Poor performance categories
3. **Absenteeism Problem**: Adjumani has higher absenteeism rates, contributing to performance issues
4. **Excellence Gap**: Moyo has over twice the percentage of top grades (A & B) than Adjumani
5. **Basic Competency Crisis**: Adjumani has over three times the percentage of failing grades (E)
""")

# Recommendations
st.header("🎯 Recommended Action Plan")

st.success("""
**I. IMMEDIATE INTERVENTIONS (0-6 months):**
- Target support for Adjumani schools in "Poor" performance category
- Implement absenteeism reduction programs with community involvement
- Establish peer learning between top Moyo schools and struggling Adjumani schools

**II. DISTRICT-SPECIFIC STRATEGIES:**
- **For ADJUMANI**: Intensive teacher training, resource allocation to highest-need schools, community engagement
- **For MOYO**: Maintain and share best practices, focus on reducing failure rates in moderate-performing schools

**III. SYSTEMIC IMPROVEMENTS (6-18 months):**
- Regular performance monitoring and data-driven interventions
- Infrastructure improvement in underperforming schools
- Scholarship programs to encourage academic excellence
- Parent-teacher partnerships to support student learning

**IV. LONG-TERM STRATEGIES (18+ months):**
- Curriculum review and alignment with regional needs
- Leadership development programs for school administrators
- Technology integration in teaching and learning
- Public-private partnerships for educational support
""")

# Conclusion
st.header("✅ Conclusion")

st.info("""
The analysis reveals a significant educational performance gap between Moyo and Adjumani districts, 
with Adjumani facing substantial challenges across multiple metrics. 
While Moyo serves as a model of relatively successful educational outcomes, 
Adjumani requires immediate and comprehensive intervention to address systemic issues 
related to teaching quality, student attendance, and academic support.

The recommendations provided offer a structured approach to addressing these challenges, 
with immediate actions focused on the most struggling schools and longer-term strategies 
aimed at creating sustainable improvement across the entire educational ecosystem of the Madi sub-region.
""")