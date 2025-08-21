import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from app import df

st.title("🏫 ATF SUPPORTED SCHOOLS PERFORMANCE ANALYSIS")
st.subheader("Comparative Analysis: MOYO SECONDARY SCHOOL vs BEZZA AL-HIJJI SECONDARY SCHOOL")

st.markdown("""
This page provides a detailed comparative analysis of the two schools currently supported by 
Amani Transformational Foundation, highlighting their performance metrics, strengths, and areas for improvement.
""")

# Filter data for the two schools
moyo_school = df[df['CentreName'].str.contains('MOYO SECONDARY SCHOOL', case=False)]
bezza_school = df[df['CentreName'].str.contains('BEZZA AL-HIJJI SECONDARY SCHOOL', case=False)]

# Check if schools were found
if moyo_school.empty or bezza_school.empty:
    st.error("One or both schools not found in the dataset. Please check the school names.")
    st.stop()

# Display school information
st.header("📋 School Profiles")

col1, col2 = st.columns(2)

with col1:
    st.subheader("MOYO SECONDARY SCHOOL")
    st.write(f"**District:** {moyo_school['DistrictName'].iloc[0]}")
    st.write(f"**Total Students:** {moyo_school['Total_Students'].iloc[0]}")
    st.write(f"**Pass Rate:** {moyo_school['Pass_Rate'].iloc[0]:.1f}%")
    st.write(f"**Excellent Performance (A+B):** {moyo_school['Excellent_Performance'].iloc[0]:.1f}%")
    st.write(f"**Failure Rate (D+E):** {moyo_school['Failure_Rate'].iloc[0]:.1f}%")
    st.write(f"**Absenteeism:** {moyo_school['Absent'].iloc[0]} students ({moyo_school['Absent'].iloc[0]/moyo_school['Total_Students'].iloc[0]*100:.1f}%)")

with col2:
    st.subheader("BEZZA AL-HIJJI SECONDARY SCHOOL")
    st.write(f"**District:** {bezza_school['DistrictName'].iloc[0]}")
    st.write(f"**Total Students:** {bezza_school['Total_Students'].iloc[0]}")
    st.write(f"**Pass Rate:** {bezza_school['Pass_Rate'].iloc[0]:.1f}%")
    st.write(f"**Excellent Performance (A+B):** {bezza_school['Excellent_Performance'].iloc[0]:.1f}%")
    st.write(f"**Failure Rate (D+E):** {bezza_school['Failure_Rate'].iloc[0]:.1f}%")
    st.write(f"**Absenteeism:** {bezza_school['Absent'].iloc[0]} students ({bezza_school['Absent'].iloc[0]/bezza_school['Total_Students'].iloc[0]*100:.1f}%)")

# Performance comparison
st.header("📊 Performance Comparison")

# Create tabs for different comparison aspects
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overall Performance", 
    "Grade Distribution", 
    "District Context", 
    "Improvement Opportunities",
    "Recommendations"
])

with tab1:
    st.subheader("Overall Performance Metrics")
    
    metrics = ['Pass_Rate', 'Excellent_Performance', 'Failure_Rate']
    moyo_values = [moyo_school[metric].iloc[0] for metric in metrics]
    bezza_values = [bezza_school[metric].iloc[0] for metric in metrics]
    
    x = np.arange(len(metrics))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, moyo_values, width, label='MOYO SECONDARY SCHOOL', color='skyblue')
    ax.bar(x + width/2, bezza_values, width, label='BEZZA AL-HIJJI SECONDARY SCHOOL', color='lightcoral')
    ax.set_xlabel('Performance Metrics')
    ax.set_ylabel('Percentage (%)')
    ax.set_title('Performance Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(['Pass Rate (A-C)', 'Excellent (A-B)', 'Failure Rate (D-E)'])
    ax.legend()
    
    st.pyplot(fig)
    
    st.markdown("""
    Both schools show room for improvement, with MOYO SECONDARY SCHOOL performing slightly better 
    across all metrics. BEZZA AL-HIJJI has a significantly higher failure rate, indicating more students 
    are struggling academically.
    """)

with tab2:
    st.subheader("Grade Distribution Comparison")
    
    grades = ['As', 'Bs', 'Cs', 'Ds', 'Es']
    moyo_grades = [moyo_school[grade].iloc[0] for grade in grades]
    bezza_grades = [bezza_school[grade].iloc[0] for grade in grades]
    
    # Calculate percentages for fair comparison
    moyo_total = sum(moyo_grades)
    bezza_total = sum(bezza_grades)
    moyo_percent = [grade/moyo_total*100 for grade in moyo_grades]
    bezza_percent = [grade/bezza_total*100 for grade in bezza_grades]
    
    x = np.arange(len(grades))
    width = 0.35
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Absolute numbers
    ax1.bar(x - width/2, moyo_grades, width, label='MOYO', color='skyblue')
    ax1.bar(x + width/2, bezza_grades, width, label='BEZZA', color='lightcoral')
    ax1.set_xlabel('Grade')
    ax1.set_ylabel('Number of Students')
    ax1.set_title('Grade Distribution (Absolute Numbers)')
    ax1.set_xticks(x)
    ax1.set_xticklabels(grades)
    ax1.legend()
    
    # Percentages
    ax2.bar(x - width/2, moyo_percent, width, label='MOYO', color='skyblue')
    ax2.bar(x + width/2, bezza_percent, width, label='BEZZA', color='lightcoral')
    ax2.set_xlabel('Grade')
    ax2.set_ylabel('Percentage (%)')
    ax2.set_title('Grade Distribution (Percentage)')
    ax2.set_xticks(x)
    ax2.set_xticklabels(grades)
    ax2.legend()
    
    st.pyplot(fig)
    
    st.markdown("""
    **Analysis:** 
    - MOYO SECONDARY SCHOOL has a more balanced grade distribution with more students in the C grade range
    - BEZZA AL-HIJJI has a concerning percentage of students in the D and E ranges (over 34% combined)
    - Both schools have very few students achieving A grades, indicating a need for excellence programs
    """)

with tab3:
    st.subheader("Performance within District Context")
    
    # Get district averages for comparison
    moyo_district_avg = df[df['DistrictName'] == 'MOYO'][['Pass_Rate', 'Excellent_Performance', 'Failure_Rate']].mean()
    adjumani_district_avg = df[df['DistrictName'] == 'ADJUMANI'][['Pass_Rate', 'Excellent_Performance', 'Failure_Rate']].mean()
    
    # Create comparison data
    comparison_data = {
        'MOYO SS': [moyo_school['Pass_Rate'].iloc[0], moyo_school['Excellent_Performance'].iloc[0], moyo_school['Failure_Rate'].iloc[0]],
        'MOYO District Avg': [moyo_district_avg['Pass_Rate'], moyo_district_avg['Excellent_Performance'], moyo_district_avg['Failure_Rate']],
        'BEZZA SS': [bezza_school['Pass_Rate'].iloc[0], bezza_school['Excellent_Performance'].iloc[0], bezza_school['Failure_Rate'].iloc[0]],
        'Adjumani District Avg': [adjumani_district_avg['Pass_Rate'], adjumani_district_avg['Excellent_Performance'], adjumani_district_avg['Failure_Rate']]
    }
    
    metrics = ['Pass Rate', 'Excellent Performance', 'Failure Rate']
    x = np.arange(len(metrics))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x - width*1.5, comparison_data['MOYO SS'], width, label='MOYO SS', color='skyblue')
    ax.bar(x - width/2, comparison_data['MOYO District Avg'], width, label='MOYO District Avg', color='deepskyblue', alpha=0.7)
    ax.bar(x + width/2, comparison_data['BEZZA SS'], width, label='BEZZA SS', color='lightcoral')
    ax.bar(x + width*1.5, comparison_data['Adjumani District Avg'], width, label='Adjumani District Avg', color='indianred', alpha=0.7)
    
    ax.set_xlabel('Performance Metrics')
    ax.set_ylabel('Percentage (%)')
    ax.set_title('School Performance vs District Averages')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()
    
    st.pyplot(fig)
    
    st.markdown("""
    **Analysis:** 
    - MOYO SECONDARY SCHOOL performs below the MOYO district average in all metrics
    - BEZZA AL-HIJJI performs below the ADJUMANI district average, particularly in failure rate
    - Both schools need targeted interventions to reach district averages
    - BEZZA AL-HIJJI faces the additional challenge of being in a lower-performing district overall
    """)

with tab4:
    st.subheader("Improvement Opportunities")
    
    # Calculate potential improvement areas
    moyo_improvement = {
        'Ds+Es to Cs': moyo_school['Ds'].iloc[0] + moyo_school['Es'].iloc[0],
        'Cs to Bs': moyo_school['Cs'].iloc[0],
        'Bs to As': moyo_school['Bs'].iloc[0]
    }
    
    bezza_improvement = {
        'Ds+Es to Cs': bezza_school['Ds'].iloc[0] + bezza_school['Es'].iloc[0],
        'Cs to Bs': bezza_school['Cs'].iloc[0],
        'Bs to As': bezza_school['Bs'].iloc[0]
    }
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # MOYO improvement opportunities
    ax1.bar(moyo_improvement.keys(), moyo_improvement.values(), color='skyblue')
    ax1.set_title('MOYO SS: Students for Potential Improvement')
    ax1.set_ylabel('Number of Students')
    ax1.tick_params(axis='x', rotation=45)
    
    # BEZZA improvement opportunities
    ax2.bar(bezza_improvement.keys(), bezza_improvement.values(), color='lightcoral')
    ax2.set_title('BEZZA SS: Students for Potential Improvement')
    ax2.set_ylabel('Number of Students')
    ax2.tick_params(axis='x', rotation=45)
    
    st.pyplot(fig)
    
    st.markdown("""
    **Improvement Opportunities:**
    
    **MOYO SECONDARY SCHOOL:**
    - **Priority 1:** Focus on 268 students with D+E grades to move them to C level
    - **Priority 2:** Help 291 C-grade students achieve B grades
    - **Priority 3:** Elevate 83 B-grade students to A level
    
    **BEZZA AL-HIJJI SECONDARY SCHOOL:**
    - **Priority 1:** Critical need to address 144 students with D+E grades
    - **Priority 2:** Support 213 C-grade students to achieve B grades
    - **Priority 3:** Help 54 B-grade students reach A level
    
    **Note:** BEZZA has a more urgent need for basic academic support given the high number of struggling students.
    """)

with tab5:
    st.subheader("Targeted Recommendations for Amani Foundation")
    
    st.success("""
    **For MOYO SECONDARY SCHOOL:**
    
    1. **Excellence Program** (Short-term: 3-6 months)
       - Implement advanced learning sessions for B students to reach A level
       - Establish peer tutoring program pairing A students with B students
       
    2. **Consolidation Program** (Medium-term: 6-12 months)
       - Focus on moving C students to B level through targeted workshops
       - Provide additional teaching resources for core subjects
       
    3. **Support Program** (Long-term: 12+ months)
       - Develop foundational skills program for D/E students
       - Implement regular progress monitoring and intervention system
    """)
    
    st.warning("""
    **For BEZZA AL-HIJJI SECONDARY SCHOOL:**
    
    1. **Foundation First** (Immediate: 1-3 months)
       - Emergency tutoring for students with D/E grades
       - Basic literacy and numeracy intervention programs
       
    2. **Stabilization Program** (Medium-term: 3-9 months)
       - Focus on moving D/E students to at least C level
       - Teacher training on differentiated instruction
       
    3. **Growth Program** (Long-term: 9-18 months)
       - Develop school-wide culture of academic excellence
       - Establish partnerships with higher-performing schools for mentorship
    """)
    
    st.info("""
    **Cross-Cutting Initiatives:**
    
    1. **Teacher Development**
       - Joint training sessions for teachers from both schools
       - Exchange program allowing teachers to observe classes at partner schools
       
    2. **Student Motivation**
       - Recognition programs for academic improvement
       - Career guidance sessions showing value of education
       
    3. **Community Engagement**
       - Parent education programs on supporting student learning
       - Community partnerships to reduce absenteeism
       
    4. **Monitoring & Evaluation**
       - Regular assessment of student progress
       - Data-driven adjustment of intervention strategies
    """)

# Footer with Amani Foundation info
st.markdown("---")
st.markdown("**Amani Transformational Foundation** - Transforming Education in the Madi Sub-Region")

st.markdown("*Supporting schools to achieve academic excellence and holistic student development*")
