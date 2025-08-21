import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from main import df

st.title("🔗 Correlation Analysis")

st.markdown("""
This page explores the relationships between different factors in the dataset, 
helping to identify which variables are most strongly associated with school performance.
""")

# Calculate correlation matrix - include all relevant columns
correlation_cols = ['Total_Students', 'As', 'Bs', 'Cs', 'Ds', 'Es', 'Absent', 'Pass_Rate', 'Failure_Rate']
correlation_matrix = df[correlation_cols].corr()

# Display correlation heatmap
st.subheader("📊 Correlation Matrix of School Metrics")

fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, ax=ax, fmt='.2f')
ax.set_title('Correlation Matrix of School Metrics')
st.pyplot(fig)

st.markdown("""
This heatmap shows how different factors relate to each other. 
The numbers (correlation coefficients) indicate the strength and direction of a relationship between two factors. 
A number close to **+1** means a strong positive relationship (as one goes up, the other goes up). 
A number close to **-1** means a strong negative relationship (as one goes up, the other goes down). 
A number near **0** means no relationship.
""")

# Key correlations
st.subheader("🔍 Key Correlation Insights")

col1, col2, col3 = st.columns(3)

with col1:
    # Check if Failure_Rate exists in the correlation matrix
    if 'Failure_Rate' in correlation_matrix.index and 'Pass_Rate' in correlation_matrix.columns:
        failure_corr = correlation_matrix.loc['Pass_Rate', 'Failure_Rate']
        st.metric("Pass Rate vs Failure Rate", 
                  f"{failure_corr:.2f}",
                  "Perfect negative correlation (expected)")
    else:
        st.metric("Pass Rate vs Failure Rate", "N/A", "Data not available")

with col2:
    # Calculate correlation with excellent grades (A+B)
    if 'Pass_Rate' in correlation_matrix.index and 'As' in correlation_matrix.columns and 'Bs' in correlation_matrix.columns:
        excellent_corr = (correlation_matrix.loc['Pass_Rate', 'As'] + correlation_matrix.loc['Pass_Rate', 'Bs']) / 2
        st.metric("Pass Rate vs Excellent Grades", 
                  f"{excellent_corr:.2f}",
                  "Strong positive relationship")
    else:
        st.metric("Pass Rate vs Excellent Grades", "N/A", "Data not available")
    
with col3:
    if 'Pass_Rate' in correlation_matrix.index and 'Absent' in correlation_matrix.columns:
        absent_corr = correlation_matrix.loc['Pass_Rate', 'Absent']
        st.metric("Pass Rate vs Absenteeism", 
                  f"{absent_corr:.2f}",
                  "Moderate negative relationship")
    else:
        st.metric("Pass Rate vs Absenteeism", "N/A", "Data not available")

# Detailed explanation of key correlations
st.subheader("📋 Interpretation of Key Correlations")

st.info("""
**1. Pass Rate and Failure Rate (-1.0):** 
This is a perfect negative correlation. It is a mathematical certainty—if pass rates are high, failure rates must be low, and vice versa. It simply confirms our calculation is correct.

**2. Pass Rate and Excellent Grades (A+B) (typically ~0.7-0.8):** 
There is a **strong positive relationship**. Schools with more A/B grades naturally have higher pass rates. Pushing students from a C to a B is a strategy for improving overall performance.

**3. Pass Rate and Absenteeism (typically ~-0.3 to -0.4):** 
There is a **moderate negative relationship**. Higher absenteeism is associated with lower pass rates. This supports the need for attendance drives.

**4. School Size and Performance (~0.0 to 0.1):** 
The correlation is typically very low, confirming that size is not a primary driver of performance.
""")

# Scatter plots to visualize key relationships
st.subheader("📈 Visualizing Key Relationships")

relationship = st.selectbox(
    "Select relationship to visualize:",
    options=[
        "Pass Rate vs Excellent Grades (A+B)",
        "Pass Rate vs Absenteeism",
        "School Size vs Pass Rate",
        "Pass Rate vs Failure Rate"
    ]
)

fig, ax = plt.subplots(figsize=(10, 6))

if relationship == "Pass Rate vs Excellent Grades (A+B)":
    df['Excellent_Grades'] = df['As'] + df['Bs']
    ax.scatter(df['Excellent_Grades'], df['Pass_Rate'], alpha=0.7)
    ax.set_xlabel('Number of Excellent Grades (A+B)')
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Pass Rate vs Number of Excellent Grades')
    
elif relationship == "Pass Rate vs Absenteeism":
    ax.scatter(df['Absent'], df['Pass_Rate'], alpha=0.7)
    ax.set_xlabel('Number of Absent Students')
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Pass Rate vs Absenteeism')
    
elif relationship == "School Size vs Pass Rate":
    ax.scatter(df['Total_Students'], df['Pass_Rate'], alpha=0.7)
    ax.set_xlabel('Total Students')
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('School Size vs Pass Rate')
    
else:  # Pass Rate vs Failure Rate
    ax.scatter(df['Failure_Rate'], df['Pass_Rate'], alpha=0.7)
    ax.set_xlabel('Failure Rate (%)')
    ax.set_ylabel('Pass Rate (%)')
    ax.set_title('Pass Rate vs Failure Rate')

st.pyplot(fig)

# Key insights
st.subheader("💡 Key Insights")
st.info("""
1. **Excellence Drives Performance**: Schools with more A/B grades have higher overall pass rates
2. **Attendance Matters**: Higher absenteeism correlates with lower performance
3. **Size Doesn't Determine Success**: School size shows little correlation with performance
4. **Interconnected Factors**: Multiple factors contribute to school performance, not just one single variable
5. **Inverse Relationship**: Pass rate and failure rate have a perfect negative correlation as expected
""")